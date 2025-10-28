# how many weeks do we have in lifelong time?
# what this task does is that it takes the input of user's age and tells them how many weeks have they lived so far.
import math

users_age = int(input("you age: "))
age = users_age
def life_in_weeks(age):
    years_remaining = 90 - age
    weeks_remaining = years_remaining * 52
    print(f"You have {weeks_remaining} weeks left.")


life_in_weeks(age)
