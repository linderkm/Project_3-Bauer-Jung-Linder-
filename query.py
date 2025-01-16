import psycopg2
import pandas as pd


conn = psycopg2.connect(database = "warcraft_db",
                        user = "postgres",
                        host = "localhost",
                        password = "postgres",
                        port = 5432)


cur = conn.cursor()
cur.execute('SELECT * FROM player;')
rows = cur.fetchall()
conn.commit()
conn.close()


df = pd.DataFrame(rows, columns=["ID","Age","Gender", "Sexuality", "Country", "Server"])

print(df.head())






