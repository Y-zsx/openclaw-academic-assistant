---
name: academic-assistant
description: 学术科研助手技能。支持论文参考文献格式化（GB/T 7714）、文献管理、毕设进度跟踪、实验数据处理、查重降重建议。当用户需要处理学术论文、参考文献、毕业设计和科研相关任务时使用此技能。
---

# Academic Assistant - 学术助手

## 核心功能

本技能帮助大学生和科研人员高效处理学术写作和科研管理任务，主要支持：

1. **参考文献格式化** - 自动转换为 GB/T 7714 标准格式
2. **文献管理** - 解析 BibTeX/EndNote/NoteExpress 导出文件
3. **毕设进度管理** - 任务分解 + 时间节点提醒
4. **实验数据处理** - CSV/Excel 数据可视化
5. **查重降重** - 报告解读 + 修改建议

## 快速开始

### 参考文献格式化

用户发送文献列表，自动返回 GB/T 7714 格式：

```
用户：帮我格式化这些参考文献：
[1] Smith J, Johnson A. Deep Learning for NLP. Nature, 2023.
[2] 张三，李四。人工智能综述。计算机学报，2024.

助手：
[1] SMITH J, JOHNSON A. Deep Learning for NLP[J]. Nature, 2023.
[2] 张三，李四。人工智能综述 [J]. 计算机学报，2024.
```

### 文献文件解析

用户上传 BibTeX/EndNote 导出文件，自动解析并格式化。

### 毕设进度跟踪

```
用户：我 6 月 1 日答辩，现在 2 月 28 日，帮我规划毕设进度

助手：
距离答辩还有 93 天，建议时间节点：
- 3 月 15 日：完成文献综述
- 4 月 1 日：完成实验/开发
- 4 月 20 日：完成初稿
- 5 月 10 日：完成修改
- 5 月 25 日：定稿 + 查重
- 6 月 1 日：答辩
```

## 工作流程

### 1. 参考文献处理流程

```
用户提供文献 → 识别来源格式 → 解析字段 → 应用 GB/T 7714 模板 → 返回结果
```

**支持的文献类型：**
- 期刊论文 [J]
- 会议论文 [C]
- 学位论文 [D]
- 专著 [M]
- 专利 [P]
- 标准 [S]
- 电子资源 [EB/OL]

**必填字段检查：**
- 作者/译者
- 标题
- 来源（期刊名/会议名/出版社）
- 年份
- 卷期页码（如适用）

### 2. 毕设进度管理流程

```
用户输入答辩日期 → 倒推时间节点 → 生成任务清单 → 设置提醒
```

**标准时间分配（本科毕设）：**
| 阶段 | 占比 | 主要内容 |
|------|------|----------|
| 选题 + 开题 | 15% | 文献调研、开题报告 |
| 实验/开发 | 35% | 数据采集、系统实现 |
| 论文写作 | 30% | 初稿、修改、定稿 |
| 答辩准备 | 20% | PPT、预答辩、正式答辩 |

### 3. 实验数据处理流程

```
用户上传数据文件 → 自动识别列名 → 选择图表类型 → 生成可视化代码 → 输出图表
```

**支持的图表类型：**
- 折线图（趋势分析）
- 柱状图（对比分析）
- 散点图（相关性）
- 热力图（多维数据）
- 箱线图（分布分析）

## 使用示例

### 示例 1：单篇文献格式化

**用户输入：**
```
帮我格式化这篇文献：
Title: Attention Is All You Need
Authors: Vaswani A, Shazeer N, Parmar N, et al.
Journal: Advances in Neural Information Processing Systems
Year: 2017
Volume: 30
Pages: 5998-6008
```

**助手输出：**
```
[1] VASWANI A, SHAZEER N, PARMAR N, et al. Attention Is All You Need[C]//Advances in Neural Information Processing Systems. 2017, 30: 5998-6008.
```

### 示例 2：批量文献处理

**用户输入：**
```
这些文献帮我按 GB/T 7714 格式化：
1. Goodfellow I, Bengio Y, Courville A. Deep Learning[M]. MIT Press, 2016.
2. 周志华。机器学习 [M]. 清华大学出版社，2016.
3. He K, Zhang X, Ren S, et al. Deep Residual Learning for Image Recognition[C]//CVPR. 2016: 770-778.
```

**助手输出：**
```
[1] GOODFELLOW I, BENGIO Y, COURVILLE A. Deep Learning[M]. MIT Press, 2016.
[2] 周志华。机器学习 [M]. 清华大学出版社，2016.
[3] HE K, ZHANG X, REN S, et al. Deep Residual Learning for Image Recognition[C]//Proceedings of the IEEE Conference on Computer Vision and Pattern Recognition. 2016: 770-778.
```

### 示例 3：毕设规划

**用户输入：**
```
我是软件工程专业的，6 月 15 日答辩，做一个毕设时间规划
```

**助手输出：**
```
📅 软件工程专业毕设计划（距离答辩还有 108 天）

【第一阶段】开题 + 文献综述（2 月 28 日 - 3 月 20 日）
- 确定选题方向
- 完成文献检索和阅读（至少 20 篇）
- 撰写开题报告
- 开题答辩

【第二阶段】系统开发（3 月 21 日 - 4 月 25 日）
- 需求分析 + 系统设计
- 编码实现
- 单元测试 + 集成测试
- 完成核心功能

【第三阶段】论文写作（4 月 26 日 - 5 月 20 日）
- 撰写初稿（建议 1.5 万字以上）
- 导师修改意见
- 二稿修改
- 格式审查

【第四阶段】答辩准备（5 月 21 日 - 6 月 15 日）
- 论文定稿 + 查重（重复率<15%）
- 制作答辩 PPT
- 预答辩演练
- 正式答辩

⚠️ 关键节点提醒：
- 4 月 25 日：完成所有开发工作
- 5 月 20 日：提交论文终稿
- 6 月 1 日：查重截止
```

## 脚本工具

### scripts/format_reference.py
参考文献格式化核心脚本，支持多种输入格式转换为 GB/T 7714。

**使用方法：**
```bash
python scripts/format_reference.py --input "文献信息" --style gbt7714
```

### scripts/thesis_timeline.py
毕设时间规划脚本，根据答辩日期倒推各阶段节点。

**使用方法：**
```bash
python scripts/thesis_timeline.py --defense-date 2026-06-15 --type undergraduate
```

### scripts/data_visualize.py
实验数据可视化脚本，支持 CSV/Excel 文件生成图表。

**使用方法：**
```bash
python scripts/data_visualize.py --input data.csv --type line --output plot.png
```

## 参考文献格式标准

### GB/T 7714-2015 核心规则

详见 `references/gbt7714-standard.md`

**快速参考：**

**期刊论文 [J]：**
```
[序号] 主要责任者。题名 [J]. 期刊名，年，卷 (期): 起止页码.
```

**会议论文 [C]：**
```
[序号] 主要责任者。题名 [C]//会议录名。出版地：出版者，出版年：起止页码.
```

**学位论文 [D]：**
```
[序号] 主要责任者。题名 [D]. 保存地点：保存单位，年份.
```

**专著 [M]：**
```
[序号] 主要责任者。题名 [M]. 版本。出版地：出版者，出版年：起止页码.
```

## 常见问题

### Q: 如何处理英文文献的作者姓名？
A: 英文作者姓全大写，名缩写（无标点），如：SMITH J

### Q: 超过 3 个作者怎么处理？
A: 列出前 3 位，后加", et al."（英文）或", 等"（中文）

### Q: 电子资源怎么标注？
A: 使用 [EB/OL] 类型，需包含 URL 和访问日期

### Q: 如何检查格式是否正确？
A: 使用技能内置的格式检查功能，或参考 `references/gbt7714-standard.md`

## 扩展资源

- `references/gbt7714-standard.md` - GB/T 7714 完整标准文档
- `references/thesis-template.md` - 毕业论文通用模板
- `references/common-journals.md` - 常见期刊 abbreviations
- `assets/thesis-ppt-template.pptx` - 答辩 PPT 模板
