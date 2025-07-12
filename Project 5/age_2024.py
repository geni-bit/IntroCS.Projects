def current_age():
    """ The function current age  prompts the user to enter their birthday in the format mm/dd/yyyy,
    and computes and returns their age as of the start date for this project, 10/17/2024."""

    #user input for thier date of birth in mm/dd/yyyy:
    birth_date = input("Enter your bday in the form mm/dd/yyyy: ")

    #spliting the str from the user birthday by flashfoward 
    birthday_list = birth_date.split("/")

    #variable for the the current year 
    current_year = 2024

    #variable for the  current month 
    curent_month = 10

    #variable for the the current day 
    current_day = 17

    #variable for the user birth month at the postion 0 of birth list
    birth_month = birthday_list[0]

    #variable for the user birth day at the postion 1 of birth list
    birth_day = birthday_list[1]
    
    #variable for the user birth year at the postion 2 of birth list
    birth_year = birthday_list[2]
    
    #variable formula to determine user's age by subtracting current year by their birth year
    age = current_year - int(birth_year)
    
    #if the user's birthdate has passed than current date then it will return with the user's age 
    if int(birth_month) < curent_month:
        return age
    
    #if the user's hasn't passed yet than current date then it will return with the user's age subtracted by 1
    elif int(birth_month) > curent_month:
        return age - 1
    
    #if the user's birthday is on current date despite the birth year then it will print Happy birthday to the user and return with the user's age
    elif int(birth_month) == curent_month and int(birth_day) == current_day:
         print("Happy Birthday")
         return age
        
    #else birthday doesn't fit in the other situations then it will return with the user's age - 1
    else:
        return age - 1
        







