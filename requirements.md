# Requirements Definition 

## Purpose of the   System 

### What my application does- 
My app uses an API to inform the user about the weather in any city around the world and it logs their previous searches if they need to check back on it. 

### Who is it for 

My application targets individuals who want quick and simple weather alerts from a trusted source without wanting to see ads and other distracting content.

# Functional Requirements 

## User Actions

- Enter city name
- View history
- Exit application
- Open Help Menu

## System Behaviour 

- Access API - whiat api>
- Display Data - in console
- Store Data - how?

## Error Handling

- Help Menu guides through common errors that the user may encounter. Such as?

- The system must handle invalid input and API errors without crashing. For example
    - Use Try and Execpt to handle user data input (does not crash)
    - Evaluate Error codes from the API - for example: 200, 400 ...

- The system must display appropriate error messages to guide the user.

## Help Menu 

- Menu can be accesible at any time if the user needs help with the application

# Non-Functional Requirements


## Performance

- Speed of response must be quick - pants

## Usability 
- User must be able to access at all times 
- Clear interface - improved doesn't make sense

## Reliability
- Application should operate without run time errors (look up what errors are: logic, runtime, syntax)

## Security

- Store the API securely. This means figuring out how to no display it on GitHib to the public. (Ask Gemini) - do you need an key? - key and secret (have to hide). Open end point doesn't need a key.

## Maintainability

- Code is maintained by (read up in the text book about maintenance)
- DocStrings which explain functions and comments which explain various points in the code to help future developers.




