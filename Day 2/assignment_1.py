# 🚨 Don't change the code below 👇
two_digit_number = input("Type a two digit number: ")
# 🚨 Don't change the code above 👆

####################################
#Write your code below this line 👇
tens = int(two_digit_number) // 10
units = int(two_digit_number) % 10

print(tens + units)