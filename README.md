# 福建地区碳汇量可视化系统

这是一个用于可视化展示福建地区碳汇量数据的Web应用系统。该系统使用Python作为后端，Tailwind CSS作为前端样式框架。

## 项目概述

本项目旨在通过数据可视化技术，直观地展示福建省各地区的碳汇量数据，帮助用户了解不同地区的碳汇情况、变化趋势以及相关环境指标。

## 技术栈

- 后端：Python, Flask, Pandas, NumPy, GeoPandas
- 前端：HTML5, JavaScript, Tailwind CSS, Chart.js, Leaflet.js
- 数据：福建省各地区碳汇量监测数据

## 功能特点

- 福建省碳汇量地图可视化
- 各地区碳汇量数据对比
- 历史数据趋势分析
- 碳汇量与相关环境因素关联分析

## 安装与使用

### 安装依赖

```bash
# 安装后端依赖
cd backend
pip install -r requirements.txt

# 安装前端依赖
cd ../frontend
npm install
```

### 启动应用

```bash
# 启动后端服务
cd backend
python app.py

# 前端开发模式（可选）
cd ../frontend
npm run dev
```

默认情况下，应用将在 http://localhost:5000 启动。

## 项目结构

```
fujian_carbon_sink/
├── backend/             # Python后端代码
│   ├── app.py           # Flask应用主文件
│   ├── data/            # 数据文件和处理模块
│   └── models/          # 数据模型
├── frontend/            # 前端代码
│   ├── src/             # 源代码
│   ├── public/          # 静态资源
│   └── index.html       # 主页面
└── README.md            # 项目文档
```

## 数据来源

- 福建省自然资源调查数据
- 国家碳汇监测平台
- 福建省生态环境厅公开数据

## 贡献指南

欢迎对本项目提出改进建议或直接贡献代码。请遵循以下步骤：

1. Fork 本仓库
2. 创建您的特性分支 (`git checkout -b feature/AmazingFeature`)
3. 提交您的更改 (`git commit -m 'Add some AmazingFeature'`)
4. 推送到分支 (`git push origin feature/AmazingFeature`)
5. 打开一个 Pull Request

## 许可证

本项目采用 MIT 许可证 - 详情请参阅 LICENSE 文件。