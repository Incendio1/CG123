# Redefining interpretable graph representation learning for cancer gene identification 

>  **The implementation of CGMap & data accompanying the manuscript submitted to _Nature Machine Intelligence_.**   

---

## Abstract
Graph representation learning is emerging as a promising alternative for identifying cancer genes (CGs). However, the pervasive heterophily in CGs associations conflicts with their implicit homophily assumption, and the opaque polygenic synergies underlying tumorigenesis make it struggle to pinpoint CGs across diverse topological scales and interpret their dependencies. Here, we develop a streamlined GNN propagation framework, CGMap, which proposes a parallel diffusion paradigm that unlocks the hierarchical information flow in typical depth-oriented GNNs. Without relying on residual connections or regularization components, it can effectively solve the challenge of oversoothing and scale multi-order information in width. Meanwhile, a biologically inspired attention module maps local gene interactions to global pathway regulation and maintains interpretable synergy coefficients. To further improve efficiency, CGMap adopts a separate lightweight GNN backbone to eliminate redundant feature transformation loops. Experimental results demonstrate that CGMap outperforms state-of-the-art methods in prediction performance and improves computational efficiency by three orders of magnitude. After systematic verification, we identified 70 highly reliable CGs, including 6 novel candidates absent from established CG databases (e.g., COSMIC and OncoKB). The model’s interpretability also reveals multiscale regulatory patterns, providing cancer mechanistic insights and accelerating CG screening.
<img width="2128" height="1592" alt="image" src="https://github.com/user-attachments/assets/cbf11ba6-fc90-4ae9-bb31-d90f54653a96" />



---

## 1. Installation and Requirements

### Requirements
```bash
Python Version: 3.8
PyTorch Version: 1.12.1, 
CUDA Version: 11.3

### Installation
```bash
pip install torch-scatter -f https://pytorch-geometric.com/whl/torch-1.12.1+cu113.html
pip install torch-sparse -f https://pytorch-f https://pytorch-geometric.com/whl/torch-1.12.1+cu113.html
pip install torch-spline-conv -f https://pytorch-geometric.com/whl/torch-1.12.1+cu113.html
pip install pytorch-geometric




