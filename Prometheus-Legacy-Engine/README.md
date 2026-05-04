# Prometheus: 自主进化的遗留系统全息重构引擎

## 🚀 项目简介
Prometheus 是一个基于 **OpenClaw** 和 **Mimo** 模型构建的企业级多智能体系统。它旨在解决金融级遗留系统（COBOL/Mainframe）的现代化迁移难题。通过**数字孪生仿真**技术，它能够在不中断业务的情况下，自动将旧系统重构为 2026 年标准的云原生微服务架构。

## 🧠 核心能力
- **全息逆向工程**：利用长上下文窗口（1M+ Tokens）理解百万行级代码库。
- **多智能体协作**：Archaeologist (分析)、Architect (设计)、Validator (验证) 三者闭环协作。
- **自主进化**：系统会根据重构失败的案例自动更新知识库，实现自我迭代。

## 🛠 技术栈
- **Core**: Python 3.12, OpenClaw Framework
- **Models**: Mimo-Max (Reasoning), Mimo-Vision (Topology Generation)
- **Infra**: Docker, Redis (State Management)

## 📊 Token 消耗分析
本项目为高吞吐应用。单次全量重构任务平均消耗：
- **上下文输入**: ~500k Tokens (代码库扫描)
- **推理输出**: ~100k Tokens (架构设计与文档生成)
- **验证环节**: ~200k Tokens (测试用例生成与模拟运行)