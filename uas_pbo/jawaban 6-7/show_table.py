import mysql.connector

mydb = mysql.connector.connect(
  host="127.0.0.1",
  port=33306,
  user="root",
  password="p455w0rd",
  database="kebunku"
)

db = mydb.cursor()

db.execute("SHOW TABLES")

for x in db:
  print(x)