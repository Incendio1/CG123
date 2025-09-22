import torch
from torch_geometric.nn import ChebConv
import torch.nn.functional as F


class EMOGINet(torch.nn.Module):
    def __init__(self, args):
        super(EMOGINet, self).__init__()
        self.args = args
        self.num_layers = args.num_layers
        if self.num_layers == 1:
            hidden_dims = []
        elif self.num_layers == 2:
            hidden_dims = [100]
        else:
            hidden_dims = [300] * (self.num_layers - 2) + [100]

        self.convs = torch.nn.ModuleList()
        if not hidden_dims:
            self.convs.append(ChebConv(58, 1, K=2))
        else:
            self.convs.append(ChebConv(58, hidden_dims[0], K=2))
            for i in range(1, len(hidden_dims)):
                self.convs.append(ChebConv(hidden_dims[i - 1], hidden_dims[i], K=2))
            self.convs.append(ChebConv(hidden_dims[-1], 1, K=2))

    def forward(self, data):
        edge_index = data.edge_index
        x = F.dropout(data.x, p=self.args.dropout, training=self.training)
        for i, conv in enumerate(self.convs):
            x = conv(x, edge_index)
            if i != len(self.convs) - 1:
                x = torch.relu(x)
                x = F.dropout(x, p=self.args.dropout, training=self.training)

        return x