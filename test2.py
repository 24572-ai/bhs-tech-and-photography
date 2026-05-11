import sqlite3

DATABASE = 'cars.db'

def print_all_cars():
    speed = input("What speed: ")
    with sqlite3.connect(DATABASE) as db:
        cursor = db.cursor()
        sql = "SELECT car_name, top_speed FROM cars WHERE top_speed >?;"
        cursor.execute(sql,(speed,))
        results = cursor.fetchall() 
        #printing them better
        for car in results:
            print(f"car: {car[0]} top speed : {car[1]}")



if __name__ == "__main__":
    print_all_cars()