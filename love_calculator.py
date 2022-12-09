# 🚨 Don't change the code below 👇
print("Welcome to the Love Calculator!")
name1 = input("What is your name? \n")
name2 = input("What is their name? \n")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇
lowercase_you = name1.lower()
lowercase_crush = name2.lower()

true_count_you = lowercase_you.count ('t') + lowercase_you.count ('r') + lowercase_you.count ('u') + lowercase_you.count ('e')

true_count_crush = lowercase_crush.count ('t') + lowercase_crush.count ('r') + lowercase_crush.count ('u') + lowercase_crush.count ('e')

love_count_you = lowercase_you.count ('l') + lowercase_you.count ('o') + lowercase_you.count ('v') + lowercase_you.count ('e')

love_count_crush = lowercase_crush.count ('l') + lowercase_crush.count ('o') + lowercase_crush.count ('v') + lowercase_crush.count ('e')

total_true_count = str(true_count_you + true_count_crush)
total_love_count = str (love_count_you + love_count_crush)
true_love = total_true_count + total_love_count

love_score = int(true_love)

if love_score <= 10 or love_score >= 90:
  print (f"Your score is {love_score}, you go together like coke and mentos.")
elif love_score >=40 and love_score <= 50:
  print (f"Your score is {love_score}, you are alright together.")
else:
   print (f"Your score is {love_score}.")

#Angela's Code
# combined_string = name1 + name2
# lower_case_string = combined_string.lower()

# t = lower_case_string.count ("t")
# r = lower_case_string.count ("r")
# u = lower_case_string.count ("u")
# e = lower_case_string.count ("e")

# true = t + r + u + e

# l = lower_case_string.count ("l")
# o = lower_case_string.count ("o")
# v = lower_case_string.count ("v")
# e = lower_case_string.count ("e")

# love = l + o + v + e

# love_score = str(true) + str(love)
# print (love_score)
