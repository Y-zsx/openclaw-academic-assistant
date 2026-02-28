---
name: academic-assistant
description: 学术科研助手 | Academic Research Assistant. 当用户提到：参考文献格式化、GB/T 7714、BibTeX 解析、.bib 文件、论文写作、毕业设计、文献管理、知网、万方、Google Scholar、EndNote、NoteExpress、数据可视化、查重降重、论文模板、学术写作、期刊格式、学位论文、引用格式化、参考文献列表 | When user mentions: reference formatting, GB/T 7714, BibTeX parsing, .bib files, thesis writing, graduation project, literature management, CNKI, Wanfang, Google Scholar, EndNote, NoteExpress, data visualization, plagiarism check, paper template, academic writing, journal format, dissertation, citation formatting, reference list. 支持运行 Python 脚本自动处理 | Supports running Python scripts for automatic processing.
---

# Academic Assistant - 学术助手

## 核心功能 | Core Features

本技能帮助大学生和科研人员高效处理学术写作和科研管理任务 | This skill helps students and researchers efficiently handle academic writing and research management tasks.

**主要支持 | Main Features:**

1. **参考文献格式化** - 自动转换为 GB/T 7714 标准格式 | Reference Formatting - Auto-convert to GB/T 7714 standard
2. **BibTeX 批量解析** - 解析 .bib 文件，支持知网/万方/Google Scholar 导出 | BibTeX Batch Parsing - Parse .bib files from CNKI/Wanfang/Google Scholar
3. **文献管理** - 解析 EndNote/NoteExpress/RefWorks 导出文件 | Literature Management - Parse EndNote/NoteExpress/RefWorks exports
4. **毕设进度管理** - 任务分解 + 时间节点提醒 | Thesis Planning - Task breakdown + timeline reminders
5. **实验数据处理** - CSV/Excel 数据可视化 | Data Visualization - CSV/Excel chart generation
6. **查重降重** - 报告解读 + 修改建议 | Plagiarism Check - Report analysis + revision suggestions

---

## Quick Start | 快速开始

### BibTeX File Parsing | BibTeX 文件解析

Parse all references from .bib file:

**Input:**
```
Help me parse this bib file
@article{vaswani2017attention,
  title={Attention is all you need},
  author={Vaswani, Ashish and Shazeer, Noam and Parmar, Niki},
  journal={Advances in neural information processing systems},
  volume={30},
  year={2017}
}
```

**Output:**
```
[1] VASWANI A, SHAZEER N, PARMAR N, et al. Attention is all you need[J]. Advances in neural information processing systems, 2017, 30.
```

### Reference Formatting | 参考文献格式化

**Input:**
```
作者：张三，李四，标题：深度学习研究进展，期刊：计算机学报，年份：2024, 卷：47, 期：3, 页码：123-135
```

**Output:**
```
张三，李四. 深度学习研究进展 [J]. 计算机学报，2024, 47(3): 123-135.
```

### Thesis Timeline | 毕设时间规划

**Input:**
```
我 6 月 15 日答辩，帮我规划毕设进度 | My defense is on June 15, help me plan my thesis timeline
```

**Output:**
```
📅 本科毕设计划 | Undergraduate Thesis Plan（距离答辩还有 106 天 | 106 days until defense）

【第 1 阶段】开题 + 文献综述（02-28 - 03-15）| Phase 1: Proposal + Literature Review
- 确定选题方向 | Determine research topic
- 完成文献检索和阅读（至少 20 篇）| Complete literature search and reading (at least 20 papers)
- 撰写开题报告 | Write proposal report
- 开题答辩 | Proposal defense

【第 2 阶段】实验/开发（03-15 - 04-21）| Phase 2: Experiment/Development
...
```

---

## Scripts | 脚本工具

### format_reference.py
Reference formatting script, supports multiple input formats to GB/T 7714.

**Usage | 使用方法:**
```bash
python scripts/format_reference.py -i "作者：张三，标题：深度学习，期刊：计算机学报，年份：2024"
```

### bibtex_parser.py
BibTeX file parser, batch convert .bib files to GB/T 7714 format.

**Usage | 使用方法:**
```bash
python scripts/bibtex_parser.py -i references.bib -o formatted.txt
```

**Options | 选项:**
- `-i, --input`: Input .bib file path | 输入文件路径
- `-o, --output`: Output file path | 输出文件路径
- `--with-citekey`: Show citation keys | 显示引用键
- `--count`: Show count only | 只显示数量

### thesis_timeline.py
Thesis timeline planner, generate schedule based on defense date.

**Usage | 使用方法:**
```bash
python scripts/thesis_timeline.py -d 2026-06-15 -t undergraduate
```

**Options | 选项:**
- `-d, --defense-date`: Defense date (YYYY-MM-DD) | 答辩日期
- `-t, --type`: Thesis type (undergraduate/master) | 论文类型

### data_visualize.py
Data visualization script, generate charts from CSV/Excel files.

**Usage | 使用方法:**
```bash
python scripts/data_visualize.py -i data.csv -t line -o plot.png
```

**Chart Types | 图表类型:**
- `line` - Line chart | 折线图
- `bar` - Bar chart | 柱状图
- `scatter` - Scatter plot | 散点图
- `heatmap` - Heatmap | 热力图
- `box` - Box plot | 箱线图

### run.py (Recommended | 推荐)
One-click runner with interactive and CLI modes.

**Usage | 使用方法:**
```bash
# Interactive mode | 交互模式
python run.py

# CLI mode | 命令行模式
python run.py --mode bib -i references.bib
python run.py --mode ref -i "作者：张三，标题：测试"
python run.py --mode plan -i 2026-06-15
```

---

## Supported Formats | 支持格式

### Reference Types | 文献类型
- Journal papers [J] | 期刊论文
- Conference papers [C] | 会议论文
- Theses [D] | 学位论文
- Books [M] | 专著
- Patents [P] | 专利
- Standards [S] | 标准
- Electronic resources [EB/OL] | 电子资源

### Export Sources | 导出来源
- CNKI (EndNote format) | 知网
- Wanfang (RefWorks format) | 万方
- Google Scholar (BibTeX) | 谷歌学术
- DBLP
- arXiv
- EndNote
- NoteExpress
- RefWorks

---

## Examples | 使用示例

### Example 1: Single Reference | 单篇文献

**Input | 输入:**
```
帮我格式化这篇文献：
Title: Attention Is All You Need
Authors: Vaswani A, Shazeer N, Parmar N, et al.
Journal: Advances in Neural Information Processing Systems
Year: 2017
Volume: 30
Pages: 5998-6008
```

**Output | 输出:**
```
VASWANI A, SHAZEER N, PARMAR N, et al. Attention Is All You Need[J]. Advances in Neural Information Processing Systems, 2017, 30: 5998-6008.
```

### Example 2: Batch Processing | 批量处理

**Input | 输入:**
```python
# references.bib
@article{vaswani2017attention,
  title={Attention is all you need},
  author={Vaswani, Ashish and Shazeer, Noam and Parmar, Niki},
  journal={Advances in neural information processing systems},
  volume={30},
  year={2017}
}

@book{goodfellow2016deep,
  title={Deep learning},
  author={Goodfellow, Ian and Bengio, Yoshua and Courville, Aaron},
  year={2016},
  publisher={MIT press}
}
```

**Command | 命令:**
```bash
python scripts/bibtex_parser.py -i references.bib
```

**Output | 输出:**
```
[1] VASWANI A, SHAZEER N, PARMAR N, et al. Attention is all you need[J]. 2017, 30.
[2] GOODFELLOW I, BENGIO Y, COURVILLE A. Deep learning[M]. MIT press, 2016.

📊 共 2 篇文献，成功 2 篇 | Total: 2 references, 2 succeeded
```

### Example 3: Thesis Planning | 毕设规划

**Input | 输入:**
```
我是软件工程专业的，6 月 15 日答辩，做一个毕设时间规划
I'm a software engineering major, defense on June 15, create a thesis timeline
```

**Output | 输出:**
```
📅 本科毕设计划 | Undergraduate Thesis Plan（距离答辩还有 108 天 | 108 days until defense）

【第 1 阶段】开题 + 文献综述（02-28 - 03-20）| Phase 1: Proposal + Literature Review
- 确定选题方向 | Determine research topic
- 完成文献检索和阅读（至少 20 篇）| Complete literature review (at least 20 papers)
- 撰写开题报告 | Write proposal report
- 开题答辩 | Proposal defense

【第 2 阶段】系统开发（03-21 - 04-25）| Phase 2: System Development
...
```

---

## Requirements | 环境要求

- Python 3.8+
- OpenClaw Gateway

### Optional Dependencies | 可选依赖

For data visualization:
```bash
pip install pandas matplotlib openpyxl seaborn
```

---

## Resources | 资源文件

- `references/gbt7714-standard.md` - GB/T 7714 complete standard | 完整标准文档
- `references/thesis-template.md` - Thesis writing template | 论文写作模板

---

## FAQ | 常见问题

### Q: How to handle English author names? | 如何处理英文作者姓名？
A: Surname in uppercase, given names abbreviated (no periods). Example: SMITH J

### Q: What if more than 3 authors? | 超过 3 个作者怎么处理？
A: List first 3 authors, then add ", et al." (English) or ", 等" (Chinese)

### Q: How to check format correctness? | 如何检查格式是否正确？
A: Use the built-in format check feature or refer to `references/gbt7714-standard.md`

### Q: Can I process multiple files at once? | 可以批量处理多个文件吗？
A: Yes, put all references in one .bib file and use `bibtex_parser.py`

---

## Version | 版本

Current: v1.2.0

See [CHANGELOG.md](CHANGELOG.md) for details.

---

## License | 许可证

MIT License

---

## Contact | 联系方式

- GitHub: https://github.com/Y-zsx/openclaw-academic-assistant
- Issues: https://github.com/Y-zsx/openclaw-academic-assistant/issues
- OpenClaw Community: https://discord.com/invite/clawd

---

**Made with 🦞 by Academic Assistant Team**
