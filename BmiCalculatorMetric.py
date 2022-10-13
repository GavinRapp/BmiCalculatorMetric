#BMI Index Calculator Meters/Kilograms
print("This program is for entertainment purposes only. \n Please consult your doctor if you have questions about your weight.")

gender = input("Are you male or female? Male/Female ").lower()
height = float(input("Enter your height in meters: "))
weight = float(input("Enter your weight in kilograms: "))
bmi = round(weight / float(height) ** 2)

#categorize bmi status
if bmi <= 18.4:
  print(f"Your bmi is: {bmi}, you are underweight. ")
elif bmi <18.5:
  print(f"Your bmi is {bmi}, you are a normal weight. ")
elif bmi <25:
 print(f"Your bmi is {bmi}, you are overweight. ")
elif bmi <30:
  print(f"Your bmi is{bmi}, you are, by definition, obese class 1. ")
elif bmi <35:
  print(f"Your bmi is {bmi}, you are, by definition, obsese class 2. ")
elif bmi <40:
  print(f"Your bmi is {bmi}, you are, by definition, obese class 3. ")
#source: https://en.wikipedia.org/wiki/Body_mass_index