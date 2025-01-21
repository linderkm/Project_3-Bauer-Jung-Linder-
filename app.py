from flask import Flask, jsonify
import psycopg2
import pg_cred

#initialize flast object
app = Flask(__name__)


#standard query format
def query (query):
    conn = psycopg2.connect(database=pg_cred.database,
                            user=pg_cred.user,
                            host=pg_cred.host,
                            password=pg_cred.password,
                            port=pg_cred.port)
    cur = conn.cursor()
    cur.execute(query)
    out = cur.fetchall()


    list = []
    for row in out:
        list.append(row)

    return list



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


#player endpoint showing complete player/ character profiles
@app.route("/api/v.1.0/players")
def getPlayers():
    conn = psycopg2.connect(database=pg_cred.database,
                            user=pg_cred.user,
                            host=pg_cred.host,
                            password=pg_cred.password,
                            port=pg_cred.port)

    query = ('SELECT * FROM player RIGHT JOIN character ON player.id = character.id;')

    cur = conn.cursor()
    cur.execute(query)
    rows = cur.fetchall()

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

    conn.commit()
    conn.close()

    return jsonify(list)


#endpoint to show the count of gender and sexuality, by age group
@app.route("/api/v.1.0/age/subdemographics")
def subdemographicsByAge():
    conn = psycopg2.connect(database=pg_cred.database,
                            user=pg_cred.user,
                            host=pg_cred.host,
                            password=pg_cred.password,
                            port=pg_cred.port)

    cur = conn.cursor()

    #Get unique age groups to iterate over for bulk queries
    queryUniqueAge = ('SELECT DISTINCT age FROM player;')
    cur.execute(queryUniqueAge)
    uniqueAgeOutput = cur.fetchall()

    uniqueAgelist = []
    for row in uniqueAgeOutput:
        uniqueAgelist.append(row[0])

    ageData = []
    for group in uniqueAgelist:
        qDict = {}
        qDict["Age"] = group

        genderQueryString = (f"SELECT gender, COUNT(gender) FROM player WHERE age = '{group}' GROUP BY gender;")
        output = query(genderQueryString)
        genderDict = {}
        for row in output:
            genderDict[row[0]] = row[1]
        qDict["Gender"] = genderDict

        count = 0
        for row in output:
            count += row[1]
        qDict["Count"] = count

        sexualityQueryString = (f"SELECT sexuality, COUNT(sexuality) FROM player WHERE age = '{group}' GROUP BY sexuality;")
        output = query(sexualityQueryString)
        sexualityDict = {}
        for row in output:
            sexualityDict[row[0]] = row[1]
        qDict["Sexuality"] = sexualityDict

        ageData.append(qDict)

    conn.commit()
    conn.close()

    return jsonify(ageData)




if __name__ == '__main__':
    app.run(debug=True)


