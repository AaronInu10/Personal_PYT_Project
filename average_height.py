# 🚨 Don't change the code below 👇
student_heights = input("Input a list of student heights ").split()
for n in range(0, len(student_heights)):
  student_heights[n] = int(student_heights[n])
# 🚨 Don't change the code above 👆
#Write your code below this row 👇
#Don't use sum () and len ()
total = 0

for i in student_heights:
   total += i
#since n is the total number of numbers in a list via index e.g. 172, 173, 174 and 175 is 3 (172(0),173(1),174(2),175(3)) -rmb indexes start from 0; so you have to make it n+1 to find the total number of numbers you include in the input
print (round(total/(n+1)))
