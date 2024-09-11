# Defining variables

weight= int(input("Hey please give your weight in kgs:"))
height= input("Hey please give your height in meters:")


bmi=weight/(height*height)

if bmi<18.5:
    print("You are under weight")
elif 18.5<= bmi < 24.9:
    print("You are healthy weight")
elif 25.0<=bmi<29.9:
    print("You are overweight")
else: # bmi>=30.0:
    print("You are obese")
