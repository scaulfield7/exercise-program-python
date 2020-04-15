# Program which decides what exercise to do
import sys

print("Welcome. This program decides what exercise to do.")

exercisedYesterday = input("Did you exercise yesterday? (Yes/No) ")

if exercisedYesterday == "Yes" or exercisedYesterday == "yes":
    print("Today is a rest day. Take a break from exercise.")
elif exercisedYesterday == "No" or exercisedYesterday == "no":
    rain = input("Is is raining? (Yes/No) ")
    if rain == "Yes" or rain == "yes":
        print("Do circuits indoors.")
    else:
        print("Woohoo! Go for a run.")
else:
    print("Enter 'Yes' or 'No' as your answer.")
    
print("Program ended.")
sys.exit()