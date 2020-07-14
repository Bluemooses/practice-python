from flask import request, jsonify
import psycopg2 as psyCon
import flask
app = flask.Flask(__name__)
app.config["DEBUG"] = True

# connect to my db
con = psyCon.connect(
    host="localhost",
    database="prime_app",
    user="postgres",
    password="postgres",
    port=5432
)
cur = con.cursor()

# get me veggies *crunch*


@app.route('/', methods=['GET'])
def home():
    cur.execute("select * from veggies")
    rows = cur.fetchall()
    for r in rows:
        print(f"id {r[0]} veggie_name {r[1]}")
    cur.close()
    con.close()
    return 'Hello'


@app.route('/best', methods=['POST', 'GET'])
def api_all():
    cur.execute(
        "insert into 'gardenbed' ('user_id') values(%s) returning 'id';", (1))
    rows = cur.fetchall()
    for r in rows:
        print(f"id {r[0]} garden_bed_id{r[1]}")
    cur.close()
    con.close()
    return 'Aloha'


@app.route('/:{id}', methods=['DELETE'])
def api_delete():
    cur.execute(
        "delete from 'gardenbed' ('user_id), ('gardenbed_id') where gardenbed_id = '%s';", f"{id}")
    cur.close()
    con.close()
    return print('success')



@app.errorhandler(404)
def page_not_found(e):
    return "<h1>404</h1><p>The resource could not be found.</p>", 404


# cursor

# execute query
# cur.execute("insert into veggies(id, veggie_name) values(%s, %s)", (1, 'Beet'))

# select veggies from table
# cur.execute("select * from veggies")

# cur("delete from veggies(veggie_name) where gardenbed_id={})


# print(rows)

# loop through results


# commit the transaction
# con.commit()

# close the cursor

# close the connection
# con.close()
app.run()
