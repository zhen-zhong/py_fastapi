import pymysql
from pymysql.cursors import DictCursor


def get_db_connection():
    """
    创建并返回数据库连接
    """
    connection = pymysql.connect(
        host="localhost",  # 数据库主机地址
        user="root",  # 数据库用户名
        password="123456",  # 数据库密码
        database="test_server",  # 数据库名称
        port=3306,  # 指定端口号
        charset="utf8mb4",  # 字符集
        cursorclass=DictCursor,  # 返回字典类型的结果集
    )
    return connection


# 测试数据库连接是否成功
if __name__ == "__main__":
    try:
        connection = get_db_connection()
        with connection.cursor() as cursor:
            cursor.execute("SELECT VERSION()")
            result = cursor.fetchone()
            print("Database version:", result)
    finally:
        connection.close()
        print("Database connection closed.")
