import mysql.connector
mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="kedwani-11566",
)   
except mysql.connector.Error as err:
    print(f"Error: {err}")

    
mycrs = mydb.cursor()
mycrs.execute("CREATE DATABASE IF NOT EXISTS alx_book_store")
mycrs.close()
mydb.close()