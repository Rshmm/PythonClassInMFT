import mysql.connector

def create_connection():
    connection = mysql.connector.connect(
        host="localhost",
        database = "person",
        user = "root",
        password = "root123"
    )
    return connection


def close_connection(connection):
    connection.close()



def save_person(name,lastName,age,city,addres):
    connection = create_connection()
    cursor = connection.cursor()
    sql = "INSERT INTO person_info (name,lastName,age,city,addres) VALUES (%s,%s,%s,%s,%s)"
    values = (name,lastName,age,city,addres)
    cursor.execute(sql,values)
    connection.commit()
    cursor.close()
    close_connection(connection)


def remove_person(person_code):
    connection = create_connection()
    cursor = connection.cursor()
    sql = "delete from person_info where code = %s"
    values = (person_code,)
    cursor.execute(sql,values)
    connection.commit()
    cursor.close()
    close_connection(connection)



def edit_person(person_code,name,lastName,age,city,addres):
    connection = create_connection()
    cursor = connection.cursor()
    sql = "update person_info set name=%s,lastName=%s,age=%s,city=%s,addres=%s where code=%s"
    values = (name,lastName,age,city,addres,person_code)
    cursor.execute(sql,values)
    connection.commit()
    cursor.close()
    close_connection(connection)


def get_all_persons():
    connection = create_connection()
    cursor = connection.cursor()
    sql = "select * from person_info"
    cursor.execute(sql)
    results = cursor.fetchall()
    cursor.close()
    close_connection(connection)
    return results