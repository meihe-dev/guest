from pymysql import cursors, connect

# 连接数据库
conn = connect(host='127.0.0.1',
               user='root',
               password='passw0rd',
               db='guest',
               charset='utf8mb4',
               cursorsclass=cursors.DictCursor)

try:
    with conn.cursor() as cursor:
        # 创建嘉宾数据
        sql = 'INSERT INTO sign_guest(realname, phone, email, sign, event_id, create_time) VALUES' \
              '("tom", 13312341237, "tom@qq.com", 0, 1, NOW());'
        # 提交事务
        conn.commit()

        with conn.cursor() as cursor:
            # 查询添加的嘉宾
            sql = 'SELECT realname, phone, email, sign FROM sign_guest WHERE phone=%s'
            cursor.execute(sql, ('13312341237',))
            result = cursor.fetchone()
            print(result)

finally:
    conn.close()