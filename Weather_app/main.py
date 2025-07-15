from weather_api import fetch_weather
from db import init_db, insert_log, get_logs, delete_logs

def main():
    init_db() // initialize database
    while True:
        print("\nWeather Logger")
        print("1. Fetch & Store Weather")
        print("2. View Logs")
        print("3. Delete Old Logs")
        print("4. Exit")
        choice = input("Choose an option: ")

        if choice == "1":
            city = input("Enter city name: ")
            try:
                data = fetch_weather(city)
                insert_log(data)    //fetching data through Weather API
                print(f"Logged: {data}")
            except Exception as e:
                print(f"Error: {e}")

        elif choice == "2":
            city = input("Filter by city (leave blank for all): ")
            date = input("Filter by date (YYYY-MM-DD, leave blank for all): ")
            logs = get_logs(city or None, date or None)
            for log in logs:
                print(log)

        elif choice == "3":
            date = input("Delete logs before date (YYYY-MM-DD): ")
            delete_logs(date)
            print("Old logs deleted.")

        elif choice == "4":
            break

        else:
            print("Invalid choice.")

if __name__ == "__main__":
    main()
