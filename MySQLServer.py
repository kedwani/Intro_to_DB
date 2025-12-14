import mysql.connector
mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="kedwani-11566",
    database="alx_book_store"
)   
print(mydb.get_server_info)