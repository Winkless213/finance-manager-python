高级记账簿

基于 Python Tkinter 的轻量级个人财务管理系统，帮助你高效记录收支、管理账目并掌握财务动态。

主要功能

收支记录：支持添加收入与支出条目，包含金额、类别、日期和备注。
分类管理：可自定义支出/收入类别（如餐饮、交通、工资等），便于分类统计。
数据持久化：使用 SQLite 数据库存储数据，程序重启后记录不丢失。
记录查询：支持按日期范围、类别或关键词搜索历史账单。
数据统计：提供月度收支汇总，直观展示消费趋势。
增删改查：完整支持对账目条目的创建、查看、修改与删除操作。

快速开始

克隆项目
   bash
   git clone https://github.com/你的用户名/finance-manager-python.git
   cd finance-manager-python
   
运行程序
   bash
   python app.py
   
无需额外安装依赖，程序启动后将自动创建 finance.db 数据库文件。

项目结构

app.py        - 程序入口，启动主应用
gui.py        - 图形用户界面实现（Tkinter）
service.py    - 业务逻辑处理（数据操作与验证）
database.py   - 数据库连接与初始化
data.json     - 示例数据文件（可选）

说明

项目使用 Python 内置库（如 tkinter、sqlite3），无需额外安装依赖。
首次运行会自动生成数据库和表结构，开箱即用。
