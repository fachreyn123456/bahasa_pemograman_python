import mysql.connector

mydb = mysql.connector.connect(
  host="127.0.0.1",
  port=33306,
  user="root",
  password="p455w0rd",
  #database="Kebunku"
)

#print(mydb)

db = mydb.cursor()

db.execute("CREATE DATABASE kebunku")