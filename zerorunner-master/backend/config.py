# -*- coding: utf-8 -*-
# @author: xiaobai
import os
import typing
from pathlib import Path

from pydantic import BaseSettings, AnyHttpUrl, Field


project_banner = """
███████╗███████╗██████╗  ██████╗ ██████╗ ██╗   ██╗███╗   ██╗███╗   ██╗███████╗██████╗
╚══███╔╝██╔════╝██╔══██╗██╔═══██╗██╔══██╗██║   ██║████╗  ██║████╗  ██║██╔════╝██╔══██╗
  ███╔╝ █████╗  ██████╔╝██║   ██║██████╔╝██║   ██║██╔██╗ ██║██╔██╗ ██║█████╗  ██████╔╝
 ███╔╝  ██╔══╝  ██╔══██╗██║   ██║██╔══██╗██║   ██║██║╚██╗██║██║╚██╗██║██╔══╝  ██╔══██╗
███████╗███████╗██║  ██║╚██████╔╝██║  ██║╚██████╔╝██║ ╚████║██║ ╚████║███████╗██║  ██║
╚══════╝╚══════╝╚═╝  ╚═╝ ╚═════╝ ╚═╝  ╚═╝ ╚═════╝ ╚═╝  ╚═══╝╚═╝  ╚═══╝╚══════╝╚═╝  ╚═╝
"""
__version__ = "2.1.5"

project_desc = """
    🎉 zerorunner 管理员接口汇总 🎉
"""

class Configs(BaseSettings):
    PROJECT_DESC: str = project_desc  # 描述
    PROJECT_BANNER: str = project_banner  # 描述
    PROJECT_VERSION: typing.Union[int, str] = __version__  # 版本
    BASE_URL: AnyHttpUrl = "http://127.0.0.1:8100"  # 开发环境

    API_PREFIX: str = "/api"  # 接口前缀
    STATIC_DIR: str = 'static'  # 静态文件目录
    GLOBAL_ENCODING: str = 'utf8'  # 全局编码
    CORS_ORIGINS: typing.List[typing.Any] = ["*"]  # 跨域请求
    WHITE_ROUTER: list = ["/api/user/login", "/api/file"]  # 路由白名单，不需要鉴权

    SECRET_KEY: str = "kPBDjVk0o3Y1wLxdODxBpjwEjo7-Euegg4kdnzFIRjc"  # 密钥(每次重启服务密钥都会改变, token解密失败导致过期, 可设置为常量)
    ACCESS_TOKEN_EXPIRE_MINUTES: int = 60 * 24 * 1  # token过期时间: 60 minutes * 24 hours * 1 days = 1 days

    # redis
    REDIS_URI: str = "redis://:@localhost:6379/4"  # 直接写入redis URI

    # DATABASE_URI: str = "sqlite+aiosqlite:///./sql_app.db?check_same_thread=False"  # Sqlite(异步)
    DATABASE_URI: str = "mysql+aiomysql://root:yyklmq511657310@localhost:3306/zerorunner?charset=UTF8MB4"
  # 直接写入MySQL URI
    DATABASE_ECHO: bool = False  # 是否打印数据库日志 (可看到创建表、表数据增删改查的信息)

    # logger
    LOGGER_DIR: str = "logs"  # 日志文件夹名
    LOGGER_NAME: str = 'zerorunner.log'  # 日志文件名  (时间格式 {time:YYYY-MM-DD_HH-mm-ss}.log)
    LOGGER_LEVEL: str = 'INFO'  # 日志等级: ['DEBUG' | 'INFO']
    LOGGER_ROTATION: str = "10 MB"  # 日志分片: 按 时间段/文件大小 切分日志. 例如 ["500 MB" | "12:00" | "1 week"]
    LOGGER_RETENTION: str = "7 days"  # 日志保留的时间: 超出将删除最早的日志. 例如 ["1 days"]

    # dir
    BASEDIR: str = os.path.join(os.path.abspath(os.path.dirname(os.path.dirname(__file__))))

    # celery worker
    broker_url: str = "redis://localhost:6379/0"  # 直接写入Celery broker URL
    task_serializer: str = "pickle"
    result_serializer: str = "pickle"
    accept_content: typing.Tuple = ("pickle", "json",)
    task_protocol: int = 2
    timezone: str = "Asia/Shanghai"
    enable_utc: bool = False
    broker_connection_retry_on_startup: bool = True
    worker_concurrency: int = 10
    worker_prefetch_multiplier: int = 4
    worker_max_tasks_per_child: int = 100
    broker_pool_limit: int = 10
    result_backend_transport_options: typing.Dict[str, typing.Any] = {'visibility_timeout': 3600}
    worker_cancel_long_running_tasks_on_connection_loss: bool = True
    include: typing.List[str] = [
        'celery_worker.tasks.test_case',
        'celery_worker.tasks.common',
        'celery_worker.tasks.task_run',
        'celery_worker.tasks.ui_case',
    ]

    TEST_FILES_DIR: str = Path(__file__).parent.joinpath("static", "files").as_posix()
    PROJECT_ROOT_DIR: str = Path(__file__).parent.as_posix()

    task_run_pool: int = 3

    # job beat
    beat_db_uri: str = "mysql+pymysql://root:123456@localhost:3306/zerorunner?charset=UTF8MB4"  # 直接写入beat DB URI

    # jacoco service
    JACOCO_SERVER_URL: str = None

    # gitlab
    GITLAB_URL: str = None
    GITLAB_TOKEN: str = None
    GITLAB_USER: str = None
    GITLAB_PASSWORD: str = None

    class Config:
        case_sensitive = True  # 区分大小写
        env_file = None  # 禁用.env文件

config = Configs()

