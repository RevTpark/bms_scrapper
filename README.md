# About
This BookMyShow scrapper informs when advance movie tickets are available in your provided location.

# How to use
- Clone the repo locally to your system. 
- Open command prompt  ```pip install requirements.txt``` 
- Run the script in a new terminal, 
  The program takes four user inputs: 
  1. *Name* of the Movie
  2. *Date* of the movie when it releases
  3. *Location* of the theater  
  4. *Theater preference type*
  
  The *movie code* is dynamically scrapped for future reference but if the code is not found the closet matches are obtained or user can enter the code manually.
- Let the script run in the background
  The script makes loud noise for a certain duration of time when the bookings are open for the particular area. So make sure:
  - System is awake the entire time or the script will sleep with the system.
  - System volume is loud enough so that you can be alerted.

# Known issues
- Script is blocked by BookMyShow serves and connection is refused and exception occurs in terminal log.\
**FIX**: Reruning the script manually should fix the issue.
