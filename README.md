# Weather App

A command-line weather application that fetches real-time weather data using the OpenWeatherMap API. Users can search for current weather conditions, view past searches, and access a help menu.

## Requirements

- Python 3.x
- An OpenWeatherMap API key (free at https://openweathermap.org)

## Installation

1. Clone or download this repository.

2. Install dependencies:
   ```
   pip install -r requirements.txt
   ```

3. Create a `.env` file in the same folder as `app.py` and add your API key:
   ```
   API_KEY=your_api_key_here
   ```

## How to Run

Navigate to the project folder in your terminal and run:

```
python app.py
```

## Features

- Search current weather by city name
- Displays temperature, humidity and weather description
- Saves search history to `history.csv`
- View past searches
- Help menu with usage instructions
- Input validation and error handling

## Dependencies

See `requirements.txt`

## Files

- `app.py` — main application
- `requirements.txt` — required Python packages
- `history.csv` — generated automatically when a search is made
- `.env` — stores your API key (not included, create your own)
- `.gitignore` — prevents sensitive files from being uploaded to GitHub