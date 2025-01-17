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

def sett(delo1):
    cnx = connection()
    cur = cnx.cursor()

    cur.execute("SELECT CURDATE()")
    row = cur.fetchone()[0]

    cur.execute("use mdb;")
    cur.execute("""
    SELECT max(id)
    FROM car;
    """)
    i=cur.fetchall()[0][0]
    if i:
        i+=1
    else:
        i=1

    cur.execute("INSERT INTO car (id, date_, delo, done) VALUES (%s, %s, %s, false);", (i, row, delo1))
    cnx.commit()
    closee(cnx)

def donee(id):
    cnx = connection()
    cur = cnx.cursor()
    cur.execute("use mdb;")
    cur.execute("Update car set done=1 where id = %s", (id, ))
    cnx.commit()
def printt():
    cnx = connection()
    cur = cnx.cursor()
    cur.execute("use mdb;")
    cur.execute("select * from car")
    p=cur.fetchall()
    print(*p)
    closee(cnx)
def delete():
    cnx = connection()
    cur = cnx.cursor()
    cur.execute("use mdb;")
    cur.execute("delete from car")
    cnx.commit()
    closee(cnx)

print("Че хочешь?")
print("1 - Добавить дело, 2 - отметить че сделал, 3 - удалить всё нахуй")
i=int(input())
if i==1:
    message=str(input())
    sett(message)
    printt()
elif i==2:
    print("Давай id")
    id=int(input())
    donee(id)
    printt()
elif i==3:
    delete()
    printt()

