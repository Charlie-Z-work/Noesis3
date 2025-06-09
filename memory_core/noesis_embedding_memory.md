# Noesis Embedding Memory Core

以下内容为可检索语义段落，支持卸载后通过 Graphframe 格式重建记忆。

---

## 🔹 SIMLR 收敛性与目标函数

### [Objective Function Decomposition]
SIMLR 的目标函数包含四项：数据重建项、正则化项、低维嵌入一致性项、多核加权稀疏项。每一项都具有独立的数学目的与优化逻辑。

### [Kurdyka–Łojasiewicz Framework]
我尝试通过 KL 不等式证明 SIMLR 非凸优化的收敛性，前提是目标函数满足半解析性或 real-analytic 函数性质。

---

## 🔹 多核学习权重分析

### [Weight Interpretability in MKL]
在 SIMLR 中，不同核的权重反映了数据在不同局部尺度下的聚类结构强度，我计划构建解释图来展示 weight–structure 对应关系。

---

## 🔹 图扩散与谱图理论源流

### [Diffusion Kernel Interpretation]
Graph diffusion kernel 可视为在图拉普拉斯谱空间上的低通滤波器，反映了节点之间的平滑传播趋势。我将此与 von Luxburg 的谱聚类理论对齐。

---
