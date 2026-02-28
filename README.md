# Academic Assistant - 学术助手技能

> OpenClaw 技能插件 - 为大学生和科研人员提供学术写作辅助工具

[![Version](https://img.shields.io/badge/version-1.2-blue.svg)](https://github.com/Y-zsx/openclaw-academic-assistant)
[![License](https://img.shields.io/badge/license-MIT-blue.svg)](LICENSE)
[![OpenClaw](https://img.shields.io/badge/OpenClaw-Skill-green.svg)](https://github.com/openclaw/openclaw)

## 📖 简介

学术助手是专为 OpenClaw 开发的技能插件，帮助大学生和科研人员高效处理学术写作和科研管理任务。

**核心功能：**
- ✅ 参考文献格式化（GB/T 7714-2015 标准）
- ✅ BibTeX 批量解析（支持知网/Google Scholar 导出）
- ✅ 毕设/论文时间规划
- ✅ 实验数据可视化
- ✅ 论文写作模板
- 🔄 查重降重建议（开发中）

## 🚀 快速开始

### 安装

#### 方法 1：直接复制（推荐）
```bash
# 下载技能包
cp academic-assistant.skill ~/.openclaw/skills/

# 重启 OpenClaw Gateway
openclaw gateway restart
```

#### 方法 2：开发模式
```bash
# 克隆仓库
git clone https://github.com/YOUR_USERNAME/academic-assistant.git
cd academic-assistant

# 在 openclaw.json 中添加技能路径
# "skills": ["./academic-assistant"]
```

### 使用示例

#### 方式 1：一键运行脚本（推荐）

```bash
# 交互模式
python3 run.py

# 命令行模式
python3 run.py --mode bib -i references.bib
python3 run.py --mode ref -i "作者：张三，标题：测试，期刊：学报，年份：2024"
python3 run.py --mode plan -i 2026-06-15
```

#### 方式 2：直接调用脚本

**1. 参考文献格式化**

```bash
python3 scripts/format_reference.py -i "作者：张三，李四，标题：深度学习，期刊：计算机学报，年份：2024"
```

**输出：**
```
张三，李四. 深度学习研究进展 [J]. 计算机学报，2024, 47(3): 123-135.
```

**2. BibTeX 批量解析**

```bash
python3 scripts/bibtex_parser.py -i references.bib
```

**3. 毕设时间规划**

```bash
python3 scripts/thesis_timeline.py -d 2026-06-15
```

**输出：**
```
📅 本科毕设计划（距离答辩还有 108 天）

【第 1 阶段】开题 + 文献综述（02-28 - 03-15）
- 确定选题方向
- 完成文献检索和阅读（至少 20 篇）
...
```

**4. 数据可视化**

```bash
python3 scripts/data_visualize.py -i experiment.csv -t line
```

## 📁 项目结构

```
academic-assistant/
├── SKILL.md                          # 技能说明（OpenClaw 加载）
├── scripts/
│   ├── format_reference.py          # 参考文献格式化
│   ├── thesis_timeline.py           # 毕设时间规划
│   └── data_visualize.py            # 数据可视化
├── references/
│   └── gbt7714-standard.md          # GB/T 7714 标准文档
├── assets/                          # 资源文件（模板等）
├── README.md                        # 本文件
└── academic-assistant.skill         # 打包文件
```

## 🛠️ 开发

### 环境要求
- Python 3.8+
- OpenClaw Gateway

### 依赖安装
```bash
# 数据可视化需要
pip install pandas matplotlib openpyxl seaborn
```

### 打包技能
```bash
cd /opt/openclaw/skills/skill-creator
python3 scripts/package_skill.py /path/to/academic-assistant
```

### 测试
```bash
# 测试参考文献格式化
python3 scripts/format_reference.py -i "作者：张三，标题：测试，期刊：测试学报，年份：2024"

# 测试毕设规划
python3 scripts/thesis_timeline.py -d 2026-06-15

# 测试数据可视化
python3 scripts/data_visualize.py -i test.csv -t line
```

## 📋 功能清单

| 功能 | 状态 | 版本 |
|------|------|------|
| 中文文献格式化 | ✅ | v1.0 |
| 英文文献格式化 | ✅ | v1.2 |
| 批量处理 | ✅ | v1.0 |
| 毕设时间规划 | ✅ | v1.0 |
| 数据可视化 | ✅ | v1.0 |
| BibTeX 解析 | ✅ | v1.2 |
| 论文模板 | ✅ | v1.1 |
| 一键运行脚本 | ✅ | v1.2 |
| 查重报告解读 | 🔄 | v1.3 规划 |

## 🤝 贡献

欢迎提交 Issue 和 Pull Request！

1. Fork 本仓库
2. 创建特性分支 (`git checkout -b feature/AmazingFeature`)
3. 提交更改 (`git commit -m 'Add some AmazingFeature'`)
4. 推送到分支 (`git push origin feature/AmazingFeature`)
5. 开启 Pull Request

## 📄 许可证

MIT License - 详见 [LICENSE](LICENSE) 文件

## 📞 联系方式

- 项目地址：https://github.com/YOUR_USERNAME/academic-assistant
- 问题反馈：https://github.com/YOUR_USERNAME/academic-assistant/issues
- OpenClaw 社区：https://discord.com/invite/clawd

## 🙏 致谢

- [OpenClaw](https://github.com/openclaw/openclaw) - 强大的 AI 网关框架
- GB/T 7714-2015 国家标准

---

**Made with 🦞 by Academic Assistant Team**
