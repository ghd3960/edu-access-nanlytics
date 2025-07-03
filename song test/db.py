import sqlite3

# 데이터베이스 파일 연결 (파일이 없으면 생성됨)
conn = sqlite3.connect('mydatabase.db')
cursor = conn.cursor()

# 테이블 생성 (존재하지 않는 경우)
cursor.execute('''
    CREATE TABLE IF NOT EXISTS users (
        id INTEGER PRIMARY KEY,
        name TEXT,
        age INTEGER
    )
''')
conn.commit()

# 데이터 삽입
cursor.execute("INSERT INTO users (name, age) VALUES (?, ?)", ('Alice', 30))
conn.commit()

# 데이터 조회
cursor.execute("SELECT * FROM users")
rows = cursor.fetchall()
for row in rows:
    print(row)

# 연결 종료
conn.close()