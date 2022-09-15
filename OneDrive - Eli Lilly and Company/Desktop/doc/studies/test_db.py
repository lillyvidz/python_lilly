
import mariadb
import sys
conn = mariadb.connect(
    user="root",
    password="Foodvidz1997!",
    host="localhost",
    port=3306,
    database="test_details"
)
cur=conn.cursor()
conn.autocommit = True

"""try:
    cur.execute("CREATE TABLE detailss(fname VARCHAR(30), lname VARCHAR(30),age INTEGER,pnum INTEGER,city VARCHAR(30),sal INTEGER)")
except Exception as y:
    print(y)"""
    
def data_add(conn, cursor):
    fname = input("Please define a 'fname':")
    lname = input("Please define a 'lname':")
    age = input("Please define a 'age':")
    pnum = input("Please define a 'pnum':")
    city = input("Please define a 'city':")
    sal = input("Please define a 'sal':")

    query = "INSERT INTO detailss(fname, lname, age,pnum,city,sal) VALUES(%s,%s,%d,%d,%s,%d)"
    value_tuple = (fname, lname, age,pnum,city,sal)
    cur.execute(query,value_tuple)

    
    
    
"""cur.execute("INSERT INTO detailss(fname,lname,age,pnum,city,sal) VALUES ('vid','pri',22,111,'bang',10000),('priya','vid',23,222,'pune',20000)")
cur.execute("DELETE FROM myemployees WHERE name=('priya')")"""
data_add(conn,cur)
cur.execute("SELECT fname,lname,age,pnum,city,sal FROM detailss")

for(fname,lname,age,pnum,city,sal) in cur:
    print("fName:",{fname},"lName:",{lname},"Age:",{age},"pnum:",{pnum},"city:",{city},"Sal:",{sal})

     
            

    
    
