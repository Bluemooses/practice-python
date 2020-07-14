import psycopg2 as psyCon

# connect to my db
con = psyCon.connect(
    host="localhost",
    database="prime_app",
    user="postgres",
    password="postgres",
    port=5432
)
# cursor
cur = con.cursor()

# execute query
cur.execute("insert into veggies(id, veggie_name) values(%s, %s)", (1, 'Beet'))
# cur.execute("insert into veggies(id, veggie_name) values(%s, %s), (1, "Beet")")

cur.execute("select id, veggie_name from veggies")

rows = cur.fetchall()

# loop through results
for r in rows:
    print(f"id {r[0]} veggie_name {r[1]}")

# commit the transaction
con.commit()

# close the cursor
cur.close()

# close the connection
con.close()
