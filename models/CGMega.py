import torch as t
import torch.nn.functional as F
from torch_geometric.nn.conv import TransformerConv
from torch_geometric.nn.norm import LayerNorm
from torch_geometric.nn.dense import Linear
from torch_geometric.utils import dropout_adj
from torch.nn import Dropout, MaxPool1d


class CGMega(t.nn.Module):
    def __init__(self,args):
        super(CGMega, self).__init__()
        self.drop_rate = 0.4
        self.convs = t.nn.ModuleList()
        mid_channels = 32
        self.convs.append(
            TransformerConv(58, 32, heads=3,
                            dropout=0.1, concat=False, beta=True)
        )
        self.convs.append(
            TransformerConv(32, 32, heads=3,
                            dropout=0.1, concat=True, beta=True)
        )

        self.ln1 = LayerNorm(in_channels=mid_channels)
        self.ln2 = LayerNorm(in_channels=32 * 3)
        self.pool = MaxPool1d(2, 2)
        self.dropout = Dropout(0.4)
        self.lins = t.nn.ModuleList()
        self.lins.append(
            Linear(int(32 * 3 / 2), 32, weight_initializer="kaiming_uniform")
        )
        self.lins.append(
            Linear(32, 1, weight_initializer="kaiming_uniform")
        )

    def forward(self, data):
        x = data.x
        edge_index = data.edge_index
        edge_index, _ = dropout_adj(edge_index, p=self.drop_rate, force_undirected=True, training=self.training)
        x = self.convs[0](x, edge_index)
        x = F.leaky_relu(x, negative_slope=0.2, inplace=True)
        x = self.ln1(x)
        edge_index, _ = dropout_adj(edge_index, p=self.drop_rate, force_undirected=True, training=self.training)
        x = self.convs[1](x, edge_index)
        x = self.ln2(x)
        x = F.leaky_relu(x, negative_slope=0.2)
        x = t.unsqueeze(x, 1)
        x = self.pool(x)
        x = t.squeeze(x)
        x = self.lins[0](x).relu()
        x = self.dropout(x)
        x = self.lins[1](x)
        return x