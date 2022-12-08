#If the bill was $150.00, split between 5 people, with 12% tip.

#Each person should pay (150.00 / 5) * 1.12 = 33.6
#Format the result to 2 decimal places = 33.60

#Tip: There are 2 ways to round a number. You might have to do some Googling to solve this.💪

#Write your code below this line 👇

print ("Welcome to the tip calculator!")
total_bill = input ("What was the total bill? $")
percentage_tip = input ("What percentage tip would you like to give? 10, 12 or 15? ")
split_bill = input ("How many people to split the bill? ")

test_tip = float(percentage_tip)/100 #percentage of tip (e.g. 12% = 12/100)
test_total = float (total_bill) #to convert total_bill from string to float
total = test_tip * test_total + test_total #to calculate the total bill + tip (e.g. 10% of 100 is $10. Add it to the total bill is $110)

pay = total / int(split_bill) #total bill incl tip divided by the num of people splitting the bill

print (f"Each person should pay: ${pay: .2f}")

#Alt solution
# print("Welcome to the tip calculator!")
# bill = float(input("What was the total bill? $"))
# tip = int(input("How much tip would you like to give? 10, 12, or 15? "))
# people = int(input("How many people to split the bill?"))

# tip_as_percent = tip / 100
# total_tip_amount = bill * tip_as_percent
# total_bill = bill + total_tip_amount
# bill_per_person = total_bill / people
# final_amount = round(bill_per_person, 2)

# print(f"Each person should pay: ${final_amount}")
