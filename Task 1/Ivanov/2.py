import mysql.connector as sql
try:
    connection = sql.connect(host = "localhost", user  = "root", passwd = "", database = "users")
    print("OK!")
except:
    print("Error!")