# 🚨 Don't change the code below 👇
age = input("What is your current age? ")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇
#Counts how many days, weeks and months you have left until you are 90

ninety_years_days = 365*90
ninety_years_weeks = 52*90
ninety_years_months = 12*90

days = 365*int(age)
weeks = 52*int(age)
months = 12*int(age)

days_left = ninety_years_days-days
weeks_left = ninety_years_weeks-weeks
months_left = ninety_years_months-months

print (f"You have {days_left} days, {weeks_left} weeks and {months_left} months left")
