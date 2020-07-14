import psycopg2 as psyCon

# connect to my db
con = psyCon.connect(
    host="localhost",
    database="prime_app",
    user="postgres",
    password="postgres",
    port=5432
)
#cursor
cur = con.cursor()

# execute query
cur.execute("select id, veggie_name from veggies")

rows = cur.fetchall()

#loop through results
for r in rows:
    print(f"id {r[0]} veggie_name {r[0]}")

# close the connection
con.close()