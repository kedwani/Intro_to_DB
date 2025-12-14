import mysql.connector
mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="kedwani-11566",
)   
mycrs = mydb.cursor()
mycrs.execute("CREATE DATABASE IF NOT EXISTS alx_book_store")
mycrs.close()
mydb.close()