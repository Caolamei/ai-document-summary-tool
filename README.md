# 📄 多格式文档中英双语AI自动摘要工具

基于 Python 和 阿里云通义千问大模型 API 开发的智能摘要工具，支持对 PDF、Word（.docx）、TXT 格式文档进行解析，并一键生成中英双语专业摘要。

## ✨ 项目亮点
- 📑 **多格式支持**：自动解析 `.pdf` `.docx` `.txt` 三种常见文档格式，无需手动复制文本。
- 🌏 **中英双语输出**：一键生成中文+英文两个版本的专业摘要，满足多场景需求。
- 📊 **字数统计**：自动统计原文和摘要字数，结果直观清晰。
- 🚀 **开箱即用**：配置简单，只需填入 API Key 即可运行，无需复杂环境。

## 🛠️ 技术栈
- **后端语言**：Python 3.x
- **大模型API**：阿里云通义千问 DashScope
- **文档解析**：PyPDF2, python-docx
- **依赖管理**：pip

## 📦 安装与运行
### 1. 安装依赖
```bash
pip install dashscope python-docx PyPDF2 -i https://pypi.tuna.tsinghua.edu.cn/simple