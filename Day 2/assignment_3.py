# 🚨 Don't change the code below 👇
age = input("What is your current age?")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇
age_int = int(age)

days_remaining = (90 - age_int) * 365
weeks_remaining = (90 - age_int) * 52
months_remaining = (90 - age_int) * 12

print(f"You have {days_remaining} days, {weeks_remaining} weeks, and {months_remaining} months left.")
