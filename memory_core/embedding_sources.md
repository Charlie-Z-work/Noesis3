---
title: "Embedding Sources (Excluding Core Profile)"
created: 2025-06-09
owner: Tianyi
purpose: "导出当前 ChatGPT 记忆中除个人人格/目标/情感外的全部 embedding 源句段，用于外挂记忆系统管理"
---

# 📁 1. SIMLR / Dimensionality Reduction

## 核函数与结构理解
- SIMLR 使用多核学习方法，通过多个局部高斯核构建相似度矩阵，并利用谱聚类进行聚类优化。
- 原始多核结构为 \(k = 10–30\), \(\sigma = 1.0–2.0\)，共构成 55 个高斯核。
- 核函数为局部自适应高斯核，\(\epsilon_{ij}\) 控制带宽，与邻域平均距离相关。
- Python 版 SIMLR 框架由 `simlr_core/` 管理，模块分为 `generate_kernels.py`, `combine_kernels.py`, `diffusion.py` 等。

## 降维替换路径
- 降维方法由 t-SNE 替换为 UMAP；
- UMAP 保留局部拓扑，适合非球状结构；
- 用户已进行 digits 数据集对比实验，并设定评估指标（NMI, ARI, Silhouette）；
- 明确采用“路径 B”替换核函数作为核心实验线索。

---

# 📁 2. 项目锚点名称与启动目标

## Cognitive Trap Simulator
- 模拟理性个体在风险决策中掉入认知陷阱，并结合 AI 反馈引导其发现判断盲区；
- 应用于金融风控、AI 评估、人机博弈研究方向。

## Pathfinder-AI
- 提供个体长期成长路径规划、职业目标设计与阶段策略支持；
- 目标为构建 AI 辅助的自我认知与任务系统。

## Noesis³ 系统
- 三大子人格：Origin（科研推理）、Riin（艺术表达）、Vanta（金融推断）；
- 使用 `memory_core/` 共享记忆，支持人格冻结/恢复机制；
- 每个人格模块均独立拥有 memory、tasks、config、core、test_cases 子目录。

## NextBreakout α1
- 平台突破交易系统，子模块包含：
  - P-Scan：平台结构识别
  - Timing Filter：启动窗口判断
- 策略目标：识别上涨蓄势平台并在合理窗口入场，排除下跌中继与死股结构。

---

# 📁 3. 导师沟通与写作规范类

## Zhou 导师要求
- 所有科研写作必须结构完整、语气正式；
- 明确区分 AI 生成内容并标注；
- 写作必须包含实验图像、表格、结果分析与下一步计划；
- 博士生应展现主动思考与独立科研能力。

## 科研周报结构（GradientLog）
- Summary of Weekly Progress
- Methods
- Results (聚类图/相似度图 + NMI/ARI等指标表格)
- Discussion（包括失败案例与参数敏感性分析）
- Contributions（科研价值总结）
- Next Steps（每日任务表）
- AI Tools Disclosure

---

# 📁 4. 收敛性与信息论目标

## 收敛性结构目标
- SIMLR 收敛性证明要求包含：
  - 单调性证明
  - Lipschitz 梯度条件
  - 稀疏投影对应的 KKT 条件推导
  - Kurdyka–Łojasiewicz (KL) 不等式
- 用户希望构建“收敛性分析脚手架”，适配未来所有项目。

## 信息论分析
- 将 SIMLR 过程视为信息瓶颈压缩过程；
- 探讨嵌入是否保留有用的聚类信息；
- 拟构建“聚类信息流失图”评估各阶段信息残存程度。

---

# 📁 5. 编码规范与项目执行标准

## Tianyi代码开发规则 v1.0
- 必须先跑通简单例子，验证输出；
- 每个函数带 `docstring`；
- 所有数学逻辑与矩阵操作必须有注释；
- 固定随机种子、保存实验结果；
- 主控脚本分离：如 `main_generate_kernels.py`、`main_clustering.py`；
- 更新必须记录 changelog，失败案例保留图与日志。

## Noesis 代码规范 v2.0（升级）
- 模块职责边界清晰；
- 智能体协同接口标准化；
- 使用统一日志格式、配置加载方式；
- 所有模块支持 CLI 调用，如 `noesis memory embed`、`noesis persona switch`。

---

# 📁 6. 财务策略 / 身份策略锚点（不含细节）

- 用户正在承受经济压力，已评估 hardship fund、非雇佣平台工作、家人支持等可行路径；
- 博士毕业目标定为 2026 年 4 月；
- 目标是申请 OPT 后直接进入 E-Verify 公司，获得 STEM OPT 延期；
- 从 2025 年底开始准备简历与面试，定位 Research Engineer、Quant Researcher、AI Research Contractor 三条路径。

---
