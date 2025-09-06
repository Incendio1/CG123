# CGMap: Path-Aware, Width-Guided Graph Representation Learning for Cancer Gene Identification

> **Code & data accompanying the manuscript submitted to _Nature Machine Intelligence_.**  
> This repository provides a minimal, reproducible implementation of CGMap for cancer gene (CG) prioritization on biomolecular networks (PPI, PathNet, GGNet), along with scripts for training, evaluation, ablation, and interpretability analyses.

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
