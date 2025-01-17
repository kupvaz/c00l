import mysql.connector

def get_connection():
    connection = mysql.connector.connect(
        host="127.0.0.1",
        port=3306,
        user="root",
        password="jajaV5,")
    return connection

def close_connection(connection):
    if connection:
        connection.close()

def get_doctor_detail(doctor_id):
    try:
        cnx=get_connection()
        cur=cnx.cursor()
        cur.execute("use mdb")
        cur.execute("select * from doctor where Doctor_Id=%s", (doctor_id, ))
        p=cur.fetchall()[0]
        print(*p)
    except (Exception, mysql.connector.Error) as error:
        print("Error while getting data", error)
        close_connection(cnx)

def get_hosp(id):
    try:
        cnx=get_connection()
        cur=cnx.cursor()
        cur.execute("use mdb")
        cur.execute("select * from hospital where Hospital_Id=%s", (id, ))
        p=cur.fetchall()[0]
        print(*p)
    except (Exception, mysql.connector.Error) as error:
        print("Error while getting data", error)
        close_connection(cnx)
def get_specialist_doctors_list(speciality, salary):
    try:
        cnx=get_connection()
        cur=cnx.cursor()
        cur.execute("use mdb")
        cur.execute("select * from doctor where Salary>=%s and Speciality=%s", (salary, speciality))
        p=cur.fetchall()
        print(p)
    except (Exception, mysql.connector.Error) as error:
        print("Error while getting data", error)
        close_connection(cnx)

def docbol(id):
    try:
            cnx=get_connection()
            cur=cnx.cursor()
            cur.execute("use mdb")
            cur.execute("select * from hospital where Hospital_Id=%s", (id,))
            p=cur.fetchall()[0][1]
            cur.execute("select * from doctor where Hospital_Id=%s", (id,))
            d=cur.fetchall()
            for i in d:
                print(*i, p)
    except (Exception, mysql.connector.Error) as error:
        print("Error while getting data", error)
        close_connection(cnx)

def update_doctor_experience(doctor_id):
    try:
        cnx=get_connection()
        cur=cnx.cursor()
        cur.execute("use mdb")
        cur.execute("Update doctor set Experience = 1 where Doctor_Id = %s", (doctor_id, ))
        cnx.commit()
    except (Exception, mysql.connector.Error) as error:
        print("Error while getting data", error)
        close_connection(cnx)
    
get_doctor_detail(102)
update_doctor_experience(102)
get_doctor_detail(102)

