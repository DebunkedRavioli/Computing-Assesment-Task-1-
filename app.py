import requests
import pandas as pd
import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()
 # temporary debug line

# Get API key from environment variable (stored in .env, never uploaded to GitHub)
from dotenv import load_dotenv
import os

load_dotenv()
# env file wont work for some reason use your own api key 
API_KEY = os.getenv("API_KEY")
BASE_URL = "https://api.openweathermap.org/data/2.5/weather"

# File to store search history
HISTORY_FILE = "history.csv"


def display_menu():
    # Displays the main menu options to the user
    print("\n--- WEATHER APP ---")
    print("1. Search Weather")
    print("2. View History")
    print("3. Help")
    print("4. Exit")


def search_weather():
    # Gets city input from user, validates it, fetches weather data from API,
    # displays results and saves to history CSV

    city = input("\nEnter city name: ")

    # Check if city input is empty
    if city.strip() == "":
        print("Error: City cannot be empty.")
        return

    # Convert city to lowercase for consistency
    city = city.strip().lower()

    try:
        # Send request to OpenWeatherMap API
        params = {
            "q": city,
            "appid": API_KEY,
            "units": "metric"
        }
        response = requests.get(BASE_URL, params=params)

        # Check if API response was successful
        if response.status_code != 200:
            print("Error: City not found or API error.")
            return

        data = response.json()

        # Extract relevant weather data from response
        temperature = data["main"]["temp"]
        humidity = data["main"]["humidity"]
        description = data["weather"][0]["description"]

        # Display weather results
        print("\n--- Weather Results ---")
        print(f"City: {city.title()}")
        print(f"Temperature: {temperature}°C")
        print(f"Humidity: {humidity}%")
        print(f"Description: {description.title()}")

        # Save record to CSV history file
        record = pd.DataFrame([{
            "city": city.title(),
            "temperature": temperature,
            "humidity": humidity,
            "description": description.title()
        }])

        if os.path.exists(HISTORY_FILE):
            record.to_csv(HISTORY_FILE, mode="a", header=False, index=False)
        else:
            record.to_csv(HISTORY_FILE, index=False)

    except requests.exceptions.ConnectionError:
        # Handle network errors
        print("Error: Network issue, please try again.")
    except (KeyError, ValueError):
        # Handle unexpected data from API
        print("Error: Unexpected data received.")


def view_history():
    # Loads and displays past weather searches from the history CSV file

    try:
        # Check if history file exists and has data
        if not os.path.exists(HISTORY_FILE):
            print("No history file exists yet.")
            return

        history = pd.read_csv(HISTORY_FILE)

        if history.empty:
            print("No history found.")
            return

        # Display all past searches
        print("\n--- Search History ---")
        print(history.to_string(index=False))

    except FileNotFoundError:
        print("No history file exists yet.")
    except Exception:
        print("Error reading history data.")


def help_menu():
    # Displays help instructions to the user
    print("\n--- Help Menu ---")
    print("1. Enter a city name to get weather data.")
    print("2. View History to see past searches.")
    print("3. Exit to close the application.")
    print("4. Ensure correct spelling of all city names.")


def exit_program():
    # Exits the application
    print("\nExiting program. Goodbye!")
    exit()


def main():
    # Main loop - displays menu and routes user to selected function
    while True:
        display_menu()
        choice = input("Enter choice: ").strip()

        if choice == "1":
            search_weather()
        elif choice == "2":
            view_history()
        elif choice == "3":
            help_menu()
        elif choice == "4":
            exit_program()
        else:
            print("Invalid option. Please enter 1, 2, 3 or 4.")


if __name__ == "__main__":
    main()