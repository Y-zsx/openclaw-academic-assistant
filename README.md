# Academic Assistant - 学术助手技能

> OpenClaw Skill Plugin - Academic Writing Assistant for Students and Researchers
>
> OpenClaw 技能插件 - 为大学生和科研人员提供学术写作辅助工具

[![Version](https://img.shields.io/badge/version-1.2.0-blue.svg)](https://github.com/Y-zsx/openclaw-academic-assistant)
[![License](https://img.shields.io/badge/license-MIT-blue.svg)](LICENSE)
[![OpenClaw](https://img.shields.io/badge/OpenClaw-Skill-green.svg)](https://github.com/openclaw/openclaw)

---

## 📖 简介 | Introduction

学术助手是专为 OpenClaw 开发的技能插件，帮助大学生和科研人员高效处理学术写作和科研管理任务。

Academic Assistant is an OpenClaw skill plugin that helps students and researchers efficiently handle academic writing and research management tasks.

**核心功能 | Core Features:**
- ✅ 参考文献格式化（GB/T 7714-2015 标准）| Reference Formatting (GB/T 7714-2015)
- ✅ BibTeX 批量解析（支持知网/Google Scholar 导出）| BibTeX Batch Parsing (CNKI/Google Scholar)
- ✅ 毕设/论文时间规划 | Thesis Timeline Planning
- ✅ 实验数据可视化 | Data Visualization
- ✅ 论文写作模板 | Thesis Writing Template
- 🔄 查重降重建议（开发中）| Plagiarism Check (In Development)

---

## 🚀 快速开始 | Quick Start

### 安装 | Installation

#### Method 1: Direct Copy (Recommended) | 方法 1：直接复制（推荐）
```bash
# Download skill package
cp academic-assistant.skill ~/.openclaw/skills/

# Restart OpenClaw Gateway
openclaw gateway restart
```

#### Method 2: Development Mode | 方法 2：开发模式
```bash
# Clone repository
git clone https://github.com/Y-zsx/openclaw-academic-assistant.git
cd openclaw-academic-assistant

# Add skill path in openclaw.json
# "skills": ["./openclaw-academic-assistant"]
```

### 使用示例 | Usage Examples

#### Method 1: One-Click Runner (Recommended) | 方式 1：一键运行（推荐）

```bash
# Interactive mode | 交互模式
python3 run.py

# CLI mode | 命令行模式
python3 run.py --mode bib -i references.bib
python3 run.py --mode ref -i "作者：张三，标题：测试，期刊：学报，年份：2024"
python3 run.py --mode plan -i 2026-06-15
```

#### Method 2: Direct Script Calls | 方式 2：直接调用脚本

**1. Reference Formatting | 参考文献格式化**

```bash
python3 scripts/format_reference.py -i "作者：张三，李四，标题：深度学习，期刊：计算机学报，年份：2024"
```

**Output | 输出:**
```
张三，李四. 深度学习研究进展 [J]. 计算机学报，2024, 47(3): 123-135.
```

**2. BibTeX Batch Parsing | BibTeX 批量解析**

```bash
python3 scripts/bibtex_parser.py -i references.bib
```

**3. Thesis Timeline | 毕设时间规划**

```bash
python3 scripts/thesis_timeline.py -d 2026-06-15
```

**Output | 输出:**
```
📅 本科毕设计划（距离答辩还有 108 天）

【第 1 阶段】开题 + 文献综述（02-28 - 03-15）
- 确定选题方向
- 完成文献检索和阅读（至少 20 篇）
- 撰写开题报告
- 开题答辩
...
```

**4. Data Visualization | 数据可视化**

```bash
python3 scripts/data_visualize.py -i experiment.csv -t line
```

---

## 📁 项目结构 | Project Structure

```
academic-assistant/
├── SKILL.md                          # Skill definition (OpenClaw)
├── README.md                         # This file
├── CHANGELOG.md                      # Version history
├── run.py                            # One-click runner
├── scripts/
│   ├── format_reference.py          # Reference formatting
│   ├── bibtex_parser.py             # BibTeX parser
│   ├── thesis_timeline.py           # Thesis planning
│   └── data_visualize.py            # Data visualization
├── references/
│   ├── gbt7714-standard.md          # GB/T 7714 standard
│   └── thesis-template.md           # Thesis template
└── assets/                          # Templates and resources
```

---

## 📋 功能清单 | Feature List

| Feature | Status | Version |
|---------|--------|---------|
| 中文文献格式化 | ✅ | v1.0 |
| English Reference Formatting | ✅ | v1.2 |
| BibTeX 批量解析 | ✅ | v1.2 |
| 毕设时间规划 | ✅ | v1.0 |
| 数据可视化 | ✅ | v1.0 |
| 论文模板 | ✅ | v1.1 |
| 一键运行脚本 | ✅ | v1.2 |
| 查重报告解读 | 🔄 | v1.3 (Planned) |

---

## 🛠️ 开发 | Development

### 环境要求 | Requirements
- Python 3.8+
- OpenClaw Gateway

### 依赖安装 | Dependencies
```bash
# For data visualization
pip install pandas matplotlib openpyxl seaborn
```

### 打包技能 | Package Skill
```bash
cd /opt/openclaw/skills/skill-creator
python3 scripts/package_skill.py /path/to/academic-assistant
```

### 测试 | Testing
```bash
# Test reference formatting
python3 scripts/format_reference.py -i "作者：张三，标题：测试，期刊：学报，年份：2024"

# Test BibTeX parsing
python3 scripts/bibtex_parser.py -i test.bib

# Test thesis planning
python3 scripts/thesis_timeline.py -d 2026-06-15

# Test data visualization
python3 scripts/data_visualize.py -i test.csv -t line
```

---

## 📊 支持格式 | Supported Formats

### 文献类型 | Reference Types
- Journal papers [J] | 期刊论文
- Conference papers [C] | 会议论文
- Theses [D] | 学位论文
- Books [M] | 专著
- Patents [P] | 专利
- Standards [S] | 标准
- Electronic resources [EB/OL] | 电子资源

### 导出来源 | Export Sources
- CNKI (EndNote format) | 知网
- Wanfang (RefWorks format) | 万方
- Google Scholar (BibTeX) | 谷歌学术
- DBLP
- arXiv
- EndNote
- NoteExpress

---

## 🤝 贡献 | Contributing

Welcome Issues and Pull Requests!

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

---

## 📄 许可证 | License

MIT License - See [LICENSE](LICENSE) file for details.

---

## 📞 联系方式 | Contact

- **Project**: https://github.com/Y-zsx/openclaw-academic-assistant
- **Issues**: https://github.com/Y-zsx/openclaw-academic-assistant/issues
- **OpenClaw**: https://github.com/openclaw/openclaw
- **Discord**: https://discord.com/invite/clawd
- **ClawHub**: https://clawhub.com

---

## 🙏 致谢 | Acknowledgments

- [OpenClaw](https://github.com/openclaw/openclaw) - Powerful AI gateway framework
- GB/T 7714-2015 National Standard

---

**Made with 🦞 by Academic Assistant Team**
