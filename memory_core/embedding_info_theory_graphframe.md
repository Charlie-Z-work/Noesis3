### [Semantic Anchor]: SIMLR as an Information Bottleneck

**Context Paragraph**:
在 SIMLR 的降维过程中，我尝试将其类比为信息瓶颈模型，即从高维原始特征中提取尽可能多的聚类相关信息，同时压缩冗余结构。此类比有助于解释不同核函数和降维方法在信息保留上的差异。未来计划绘制“聚类信息残存曲线”，展示不同核组合下嵌入对类别结构的保持程度。

**Knowledge Tag**: SIMLR, Information Theory
**Related Concepts**: information bottleneck, embedding fidelity, clustering relevance
**Use Case**: 博士论文 - 信息论分析章节
**Memory Weight**: 0.93
**Source ID**: `simlr_info_bottleneck_20250607`

---

### [Semantic Anchor]: Clustering Fidelity and Information Loss

**Context Paragraph**:
我尝试量化降维后的相似度矩阵与原始类别标签之间的 mutual information，作为信息保真度的度量方式。该值越高，表示嵌入越成功保留了原始聚类结构。此外，也提出以信息损失率（1 - preserved mutual information）来评估不同核函数、降维技术的相对优劣。

**Knowledge Tag**: Mutual Information, Dimensionality Reduction
**Related Concepts**: information loss, mutual information, dimensional fidelity
**Use Case**: 指标设计草稿，计划用于论文方法章节
**Memory Weight**: 0.91
**Source ID**: `info_fidelity_metric_20250608`

---

### [Semantic Anchor]: Embedding Fidelity Visualization Plan

**Context Paragraph**:
我构思了一种新的可视化方式：在多核聚类过程中，记录每一组核函数生成的嵌入，并以嵌入维度与聚类信息保持率为横纵坐标，绘制“信息残存图”。图中不同方法的曲线走向将揭示哪些方法在保留聚类结构信息方面更有效，从而指导后续核函数设计。

**Knowledge Tag**: Visualization, Kernel Comparison
**Related Concepts**: embedding visualization, fidelity plot, clustering retention
**Use Case**: 信息论图像草案（未实现）
**Memory Weight**: 0.88
**Source ID**: `embedding_fidelity_plot_20250607`

---
