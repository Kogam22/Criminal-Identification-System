import pymysql
import os
from dotenv import load_dotenv

load_dotenv()

host = os.environ.get("db-host") or "localhost"
user = os.environ.get("username")
password = os.environ.get("password")
database = os.environ.get("database")

def firstTime():
    db = pymysql.connect(host, user, password, database)
    cursor = db.cursor()

    try:
        checkTable = "show tables like 'criminaldata'"
        cursor.execute(checkTable)
        result = cursor.fetchone()
    except Exception as e:
        print(e)
        
    if not result:
        print("First time")
        createTable = "create table criminaldata(id int primary key auto_increment, `name` varchar(20) not null, `father name` varchar(25), `mother name` varchar(25), gender varchar(6) not null, dob varchar(10), `blood group` varchar(5), `identity mark` varchar(30) not null, nationality varchar(15) not null, `religion` varchar(15) not null, `crimes` text not null);"

        try:
            cursor.execute(createTable)
            db.commit()
            
        except Exception as e:
            print(e)
            db.rollback()
            print("Unable to create table criminaldata, try in client")
    
    else:
        print("Not first time")

    db.close()

def insertData(data):
    rowId = 0

    db = pymysql.connect(host, user, password, database)
    cursor = db.cursor()
    print("database connected")

    query = "INSERT INTO criminaldata VALUES(0, '%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s');" % \
            (data["Name"], data["Father's Name"], data["Mother's Name"], data["Gender"],
             data["DOB(yyyy-mm-dd)"], data["Blood Group"], data["Identification Mark"],
             data["Nationality"], data["Religion"], data["Crimes Done"])

    try:
        cursor.execute(query)
        db.commit()
        rowId = cursor.lastrowid
        print("data stored on row %d" % rowId)
    except:
        db.rollback()
        print("Data insertion failed")


    db.close()
    print("connection closed")
    return rowId

def retrieveData(name):
    id = None
    crim_data = None

    db = pymysql.connect(host, user, password, database)
    cursor = db.cursor()
    print("database connected")

    query = "SELECT * FROM criminaldata WHERE name='%s'"%name

    try:
        cursor.execute(query)
        result = cursor.fetchone()

        id=result[0]
        crim_data = {
            "Name" : result[1],
            "Father's Name" : result[2],
            "Mother's Name" : result[3],
            "Gender" : result[4],
            "DOB(yyyy-mm-dd)" : result[5],
            "Blood Group" : result[6],
            "Identification Mark" : result[7],
            "Nationality" : result[8],
            "Religion" : result[9],
            "Crimes Done" : result[10]
        }

        print("data retrieved")
    except:
        print("Error: Unable to fetch data")

    db.close()
    print("connection closed")

    return (id, crim_data)
