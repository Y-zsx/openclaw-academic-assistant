# ClawHub Submission | ClawHub 提交材料

## Skill Information | 技能信息

**Name | 名称:** academic-assistant

**Version | 版本:** 1.2.1

**Description | 描述:**
```
Academic Research Assistant for reference formatting, BibTeX parsing, thesis planning, and data visualization. Supports GB/T 7714, CNKI, Google Scholar, EndNote. 学术科研助手，支持参考文献格式化、BibTeX 解析、毕设规划、数据可视化。
```

**Category | 分类:** Productivity / Education / Research

**Tags | 标签:**
```
academic, research, reference, bibliography, bibtex, thesis, paper, writing, formatting, gbt7714, cnki, google-scholar, endnote, citation, student, university, graduation
```

**Author | 作者:** Y-zsx

**License | 许可证:** MIT

**Repository | 仓库:** https://github.com/Y-zsx/openclaw-academic-assistant

---

## Features | 功能特性

### Core Features | 核心功能
1. **Reference Formatting** - GB/T 7714-2015 standard (Chinese & English)
   参考文献格式化 - GB/T 7714-2015 标准（中英文）

2. **BibTeX Batch Parsing** - Support CNKI, Wanfang, Google Scholar, EndNote exports
   BibTeX 批量解析 - 支持知网、万方、Google Scholar、EndNote 导出

3. **Thesis Timeline Planning** - Automatic schedule generation based on defense date
   毕设时间规划 - 根据答辩日期自动生成计划

4. **Data Visualization** - Generate charts from CSV/Excel files
   数据可视化 - 从 CSV/Excel 生成图表

5. **Thesis Template** - Complete writing guide and structure
   论文模板 - 完整的写作指南和结构

### Supported Formats | 支持格式
- Journal papers [J], Conference papers [C], Theses [D], Books [M]
- Electronic resources [EB/OL], Patents [P], Standards [S]

### Export Sources | 导出来源
- CNKI (知网), Wanfang (万方), Google Scholar, DBLP, arXiv
- EndNote, NoteExpress, RefWorks

---

## Screenshots | 截图

### Reference Formatting | 参考文献格式化
```
Input: 作者：张三，李四，标题：深度学习，期刊：计算机学报，年份：2024
Output: 张三，李四. 深度学习 [J]. 计算机学报，2024.
```

### BibTeX Parsing | BibTeX 解析
```
Input: references.bib (6 references)
Output: 
[1] VASWANI A, SHAZEER N, PARMAR N, et al. Attention is all you need[J]. 2017, 30.
[2] GOODFELLOW I, BENGIO Y, COURVILLE A. Deep learning[M]. MIT press, 2016.
...
📊 共 6 篇文献，成功 6 篇
```

### Thesis Planning | 毕设规划
```
Input: 我 6 月 15 日答辩，帮我规划毕设
Output:
📅 本科毕设计划（距离答辩还有 106 天）
【第 1 阶段】开题 + 文献综述（02-28 - 03-15）
【第 2 阶段】实验/开发（03-15 - 04-21）
【第 3 阶段】论文写作（04-21 - 05-22）
【第 4 阶段】答辩准备（05-22 - 06-12）
```

---

## Installation | 安装

### Method 1: Direct Install | 方法 1：直接安装
```bash
cp academic-assistant.skill ~/.openclaw/skills/
openclaw gateway restart
```

### Method 2: Git Clone | 方法 2：Git 克隆
```bash
git clone https://github.com/Y-zsx/openclaw-academic-assistant.git
# Add to openclaw.json: "skills": ["./openclaw-academic-assistant"]
```

---

## Usage Examples | 使用示例

### One-Click Runner | 一键运行
```bash
python3 run.py
```

### CLI Mode | 命令行模式
```bash
# Reference formatting
python3 run.py --mode ref -i "作者：张三，标题：测试，期刊：学报，年份：2024"

# BibTeX parsing
python3 run.py --mode bib -i references.bib

# Thesis planning
python3 run.py --mode plan -i 2026-06-15
```

### Direct Script Calls | 直接调用脚本
```bash
python3 scripts/format_reference.py -i "文献信息"
python3 scripts/bibtex_parser.py -i references.bib
python3 scripts/thesis_timeline.py -d 2026-06-15
python3 scripts/data_visualize.py -i data.csv -t line
```

---

## Requirements | 环境要求

- Python 3.8+
- OpenClaw Gateway

### Optional Dependencies | 可选依赖
```bash
pip install pandas matplotlib openpyxl seaborn
```

---

## Target Users | 目标用户

- Undergraduate students (graduation projects)
- Graduate students (thesis writing)
- Researchers (paper formatting)
- Academic institutions

- 本科生（毕业设计）
- 研究生（论文写作）
- 科研人员（论文格式化）
- 高校/研究机构

---

## Why This Skill? | 为什么需要这个技能？

### Problems Solved | 解决的问题
1. **Time-consuming formatting** - Manual reference formatting takes hours
   耗时的格式化 - 手动格式化参考文献需要数小时

2. **Multiple database exports** - Different formats from CNKI, Google Scholar, etc.
   多数据库导出 - 知网、Google Scholar 等格式不统一

3. **Thesis planning** - Students don't know how to schedule their work
   毕设规划 - 学生不知道如何安排时间

4. **Format standards** - GB/T 7714 compliance is complex
   格式标准 - GB/T 7714 标准复杂难懂

### Benefits | 带来的好处
- **Save 80%+ time** on reference formatting
  节省 80%+ 的参考文献格式化时间
- **Automatic scheduling** for thesis work
  自动生成毕设计划
- **Standard compliance** with GB/T 7714-2015
  符合 GB/T 7714-2015 国家标准
- **Batch processing** for large reference lists
  批量处理大量参考文献

---

## Changelog | 更新日志

See [CHANGELOG.md](CHANGELOG.md) for detailed version history.

---

## Contact | 联系方式

- **GitHub**: https://github.com/Y-zsx/openclaw-academic-assistant
- **Issues**: https://github.com/Y-zsx/openclaw-academic-assistant/issues
- **OpenClaw**: https://github.com/openclaw/openclaw
- **Discord**: https://discord.com/invite/clawd

---

## License | 许可证

MIT License

---

**Submission Date | 提交日期:** 2026-02-28

**Skill Version | 技能版本:** 1.2.1

**Status | 状态:** ✅ Ready for Submission | 准备提交
