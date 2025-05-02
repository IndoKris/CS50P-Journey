'''
Objective:
Create a Python program that asks the user for their birth date (day and month), and calculates how many days are left until their next birthday. If today is their birthday, display a special birthday message.
'''
from datetime import datetime, date 

def birthday_countdown():
    # Step 1: Get today's date
    today_date = date.today()

    # Step 2: Ask user for their birthday (MM-DD format)
    birth_date = input("Enter your birthday (MM-DD): ")

    try:
        # Step 3: Parse the input string into a datetime object
       

        # Step 4: Create a date object for this year's birthday
        

        # Step 5: If birthday has passed this year, use next year


        # Step 6: Calculate difference in days
        

        # Step 7: Output
        if days_left == 0:
            print("🎉 Happy Birthday! 🎉")
        else:
            print(f"Your birthday is in {days_left} day(s).")

    except ValueError:
        print("Invalid date format. Please use MM-DD format (e.g., 08-10).")

# Run the function
birthday_countdown()
