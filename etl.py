from flask import Flask, jsonify
import psycopg2
import pg_cred


conn = psycopg2.connect(database = pg_cred.database,
                            user = pg_cred.user,
                            host = pg_cred.host,
                            password = pg_cred.password,
                            port = pg_cred.port)

queryGenderCount = ('SELECT age, COUNT(gender) FROM player GROUP BY age;')
#querySexualityCount = ('SELECT * FROM player RIGHT JOIN character ON player.id = character.id;')

cur = conn.cursor()
cur.execute(queryGenderCount)
genderdata = cur.fetchall()
conn.commit()
conn.close()


print(genderdata)



#initialize flast object
app = Flask(__name__)



#index page
@app.route("/")
def homepage():
    #List all available routes.
    return(
        f"Available Routes:<br/>"
        f"/api/v.1.0/players<br/>"
        f"/api/v.1.0/age/subdemographics<br/>"
        f"/api/v.1.0/faction/class"
    )




#player endpoint- showing complete player/ character profiles
@app.route("/api/v.1.0/players")
def getPlayers():
    conn = psycopg2.connect(database="warcraft_db",
                            user="postgres",
                            host="localhost",
                            password="postgres",
                            port=5432)

    query = ('SELECT * FROM player RIGHT JOIN character ON player.id = character.id;')

    cur = conn.cursor()
    cur.execute(query)
    rows = cur.fetchall()
    conn.commit()
    conn.close()

    list = []

    for row in rows:
        dict = {}
        dict['id'] = row[0]
        dict['age'] = row[1]
        dict['gender'] = row[2]
        dict['sexuality'] = row[3]
        dict['country'] = row[4]
        dict['server'] = row[5]
        dict['server'] = row[6]
        dict['faction'] = row[7]
        dict['main'] = row[8]
        dict['role'] = row[9]
        dict['class'] = row[10]
        dict['race'] = row[11]
        dict['type'] = row[12]
        list.append(dict)

    return jsonify(list)







# @app.route("/api/v.1.0/age/subdemographics")
# def subdemographicsByAge():
#
#     conn = psycopg2.connect(database="warcraft_db",
#                                 user="postgres",
#                                 host="localhost",
#                                 password="postgres",
#                                 port=5432)
#
#     queryGenderCount = ('SELECT age, COUNT(gender) FROM player GROUP BY age;')
#     querySexualityCount = ('SELECT * FROM player RIGHT JOIN character ON player.id = character.id;')
#
#     cur = conn.cursor()
#     cur.execute(queryGenderCount)
#     genderdata = cur.fetchall()
#     conn.commit()
#     conn.close()









# if __name__ == '__main__':
#     app.run(debug=True)


