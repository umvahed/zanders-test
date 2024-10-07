# Zanders Case - Backend Engineer
To assess the quality and structure of your work, we have prepared a short programming case. 
The case is designed to be done within an hour. Since the time is limited, please focus
on the items which you think are important. If not everything is ready at the end of the hour, 
you will have the opportunity to explain your next steps in the interview. 

## Requirements
- The case should be completed in Python (3.11 or greater).
- Make use of FastAPI, Pydantic v2, and SQLAlchemy v2 while solving the case. If you think another package 
is a better fit, be prepared to explain why in the interview. 
- Please zip your work at the end of the hour (including this README) and share the file with Martijn Groenbroek (m.groenbroek@zandersgroup.com)
- You are free to search for help on Google, Bing, Stackoverflow, ChatGPT etc.

## Case
We want you to write the backend for a “message board” app with at least the following three routes:
- POST /login: Login with username and password, sets a cookie
- POST /message: Write message (requires login)
- GET /message: Show all messages with username and timestamp, ordered in descending order (requires login)

Please wrap this in what you would consider a neat, production-ready FastAPI app. For us that means at least:
- Pydantic API request and response schemas
- SQLAlchemy declarative ORM for database interaction
- Test cases (you can use the FastAPI test client and an in-memory sqlite database)

## Approach 

- Authentication: Simple username-password-based login.
- Message Handling: Ability to post and retrieve messages.
- Database: Use SQLAlchemy as the ORM for database interaction.
- FastAPI: Set up routes and manage request/response handling.
- Testing: Ensure the core functionalities work as expected.
- Error Handling: Handle common error cases  (e.g., invalid login).