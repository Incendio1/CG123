# Redefining interpretable graph representation learning for cancer gene identification via width scaling under heterophily

> **Code & data accompanying the manuscript submitted to _Nature Machine Intelligence_.**  
> This project provides implementation of CGMap for pan-cancer gene identifications. Graph representation learning, represented by graph neural networks (GNNs), is emerging as a promising alternative for identifying cancer genes (CGs). However, the pervasive heterophily in CG associations conflicts with their implicit homophily assumption, and the opaque polygenic synergies underlying tumorigenesis make it struggle to pinpoint CGs across diverse topological scales and interpret their dependencies. Here, we develop a streamlined GNN propagation framework, CGMap, which proposes a parallel diffusion paradigm that unlocks the hierarchical information flow in typical depth-oriented GNNs. Without relying on residual connections or regularization components, it can effectively solve the challenge of oversoothing and scale multi-order information in width. Meanwhile, a biologically inspired attention module maps local gene interactions to global pathway regulation and maintains interpretable synergy coefficients. To further improve efficiency, CGMap adopts a separate lightweight GNN backbone to eliminate redundant feature transformation loops. Experimental results demonstrate that CGMap outperforms state-of-the-art methods in prediction performance and improves computational efficiency by three orders of magnitude. After systematic verification, we identified 70 highly reliable CGs, including 6 novel candidates absent from established CG databases (e.g., COSMIC and OncoKB). The model’s interpretability also reveals multiscale regulatory patterns, providing cancer mechanistic insights and accelerating CG screening.

---

## Highlights
- **Path-aware, width-guided propagation** to capture multi-hop dependencies without cross-layer noise.
- **Heterophily-ready**: robust on networks where CGs are topologically sparse and dispersed.
- **Reproducible**: single-command experiments with fixed seeds and exact configs.
- **Lightweight**: modular PyTorch codebase; easy to extend for new datasets.

---

## 1. Installation

### Option A: Conda
```bash
conda env create -f environment.yml
conda activate cgmap




**Abstract:** Deciphering latent cancer driver genes is critical for advancing clinical interventions and therapeutic development. However, oncogenesis arises from cumulative genomic alterations and regulatory interactions, presenting challenges of topological heterophily, long-range dependency, and multiscale synergy. CGMap is a novel graph representation learning framework driven by width perspective and path awareness to address these challenges. It robustly identifies cancer genes under heterophily, outperforming 12 baseline methods, and achieves up to three orders of magnitude speedup, enabling large-scale molecular network analysis.

## 🚀 Key Features

- **Heterophily-Robust Learning:** Effectively captures cancer gene signals in topologically sparse, heterophilic graphs.
- **Path-Aware Architecture:** Leverages shortest-path-based hierarchical messaging to avoid redundancy and capture fine-grained dependencies.
- **Scalability & Efficiency:** Achieves superior computational performance, ideal for genome-scale networks.
- **Reproducibility:** All code, pre-processed data, and scripts to replicate the paper's figures and tables are provided.

## 📦 Repository Structure
