import mysql.connector

myconn = mysql.connector.connect(
    host = "localhost", 
    user = "root", 
    passwd = "Thoai12309@")
   
print(myconn)
