import sqlite3

db = sqlite3.connect('cars.db')
cursor = db.cursor()
sql = "SELECT * FROM cars;"
cursor.execute(sql)
results = cursor.fetchall() 
print(results)             
#close the db
db.close