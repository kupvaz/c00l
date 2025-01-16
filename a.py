import mysql.connector
def connection():
    cnx = mysql.connector.connect(
        host="127.0.0.1",
        port=3306,
        user="root",
        password="jajaV5,")
    return cnx
def closee(cnx):
    if cnx:
        cnx.close()
cur = connection().cursor()
cur.execute("SELECT CURDATE()")
row = cur.fetchone()
i=0
cur.execute("SELECT GREATEST(id) AS max_value FROM car;")
delo1=str(input())
cur.execute("INSERT INTO car (id, date_, delo, done) VALUES ({}, {}, {}, false);".format(i, row[0], delo1))
closee(cur)
