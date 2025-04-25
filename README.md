# README.md
1. python -m venv venv # 创建虚拟环境
   - 在 Windows 上使用 python -m venv venv
   - 在 Linux 或 macOS 上使用 python3 -m venv venv
2. source venv/bin/activate # 激活虚拟环境
   - 在 Windows 上使用 venv\Scripts\activate
   - 在 Linux 或 macOS 上使用 source venv/bin/activate
3. pip install -r requirements.txt # 安装依赖
   - 这里的 requirements.txt 是一个文本文件，列出了项目所需的所有 Python 库和版本
   - 你可以使用 pip freeze > requirements.txt 命令来生成这个文件
   - 也可以手动创建并添加所需的库
   - 例如：fastapi、uvicorn、sqlalchemy、alembic 等
4. uvicorn main:app --reload --port 8080 # 启动项目
   - main:app 是指在 main.py 文件中有一个名为 app 的 FastAPI 实例
   - --reload 选项会在代码更改时自动重启服务器
   - --port 8080 指定服务器运行的端口号
5. pip freeze > requirements.txt # 生成依赖文件
   - 这个命令会将当前虚拟环境中安装的所有库及其版本输出到 requirements.txt 文件中
6. 目录结构

```
my_fastapi_project/
├── app/
│   ├── __init__.py
│   ├── main.py            # 入口文件
│   ├── core/              # 核心功能
│   │   ├── __init__.py
│   │   ├── config.py      # 配置文件
│   │   ├── security.py    # 安全相关
│   │   └── ...            # 其他核心功能
│   ├── api/               # API 路由
│   │   ├── __init__.py
│   │   ├── v1/
│   │   │   ├── __init__.py
│   │   │   ├── endpoints/
│   │   │   │   ├── __init__.py
│   │   │   │   ├── users.py     # 用户相关接口
│   │   │   │   ├── items.py     # 其他接口
│   │   │   │   └── ...
│   │   │   └── ...              # 其他版本的API
│   ├── models/             # 数据模型
│   │   ├── __init__.py
│   │   ├── user.py         # 用户模型
│   │   ├── item.py         # 其他模型
│   │   └── ...
│   ├── schemas/            # 数据验证模型
│   │   ├── __init__.py     
│   │   ├── user.py         # 用户数据模型
│   │   ├── item.py         # 其他数据模型
│   │   └── ...
│   ├── crud/               # 数据库操作
│   │   ├── __init__.py
│   │   ├── user.py         # 用户CRUD操作
│   │   ├── item.py         # 其他CRUD操作
│   │   └── ...
│   ├── db/                 # 数据库相关
│   │   ├── __init__.py
│   │   ├── base.py         # 数据库基础设置
│   │   ├── session.py      # 数据库会话
│   │   └── ...
│   ├── tests/
│   │   ├── __init__.py
│   │   ├── test_main.py    # 测试主文件
│   │   ├── test_users.py   # 用户相关测试
│   │   └── ...
│   └── utils/              # 工具函数
│       ├── __init__.py
│       ├── utils.py
│       └── ...
├── .env                    # 环境变量文件
├── alembic/                # 数据库迁移工具目录
│   ├── env.py              # Alembic 环境配置
│   ├── script.py.mako      # Alembic 脚本模板
│   └── versions/           # 版本迁移脚本
│       ├── 2023_10_01_0001_create_user_table.py # 示例迁移脚本
│       ├── 2023_10_01_0002_create_item_table.py # 示例迁移脚本
│       └── ...
├── alembic.ini             # Alembic 配置文件
├── requirements.txt        # 项目依赖
├── Dockerfile              # Docker 配置文件
├── docker-compose.yml      # Docker Compose 配置文件
├── .gitignore              # Git 忽略文件
└── README.md               # 项目说明文件
```

