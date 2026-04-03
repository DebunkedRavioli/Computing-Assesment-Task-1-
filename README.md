# Requirements Definition 

## Purpose of the System 

### What my application does  
My app uses an API to provide the user with weather information for any city around the world. It also logs previous searches so users can refer back to them if needed.  

### Who is it for  
My application targets individuals who want quick and simple weather information from a trusted source, without ads or distracting content.  

---

# Functional Requirements 

## User Actions

- The system must allow the user to enter a city name.  
- The system must allow the user to view previous searches.  
- The system must allow the user to exit the application safely without errors.  
- The system must allow the user to access a help menu at any time.  

---

## System Behaviour 

- The system must retrieve weather data from an external API based on user input.  
- The system must display temperature, humidity, and weather description clearly in the console.  
- The system must store user search data in a CSV file using the Pandas library.  

---

## Error Handling

- The help menu must guide users through common errors such as:
  - Invalid city name  
  - No internet connection  
  - API not responding  

- The system must handle invalid input and API errors without crashing. For example:
  - Use try and except to handle user input errors  
  - Evaluate API response status codes (e.g. 200 = success, 404 = not found)  

- The system must display appropriate error messages to guide the user.  

---

## Help Menu 

- The help menu must be accessible at any time if the user needs assistance with the application.  

---

# Non-Functional Requirements

## Performance

- The system should return API results within 2 seconds.  

---

## Usability 

- The system must be easy to access and navigate.  
- The system must provide clear prompts and a simple, easy-to-understand interface.  

---

## Reliability

- The system must run without runtime errors during normal operation.  

---

## Security

- The system must protect the API key by not exposing it in public repositories such as GitHub.  

---

## Maintainability

- The system must be written in a structured and modular way to allow future updates and maintenance.  
- The system must include docstrings and comments to explain functions and key parts of the code.  