val = input("Enter your Height(cm) and Weight(kg) :").split()
cm = int(val[0])
mass = int(val[1])
meter = cm/100
bmi = mass/(meter**2)
if bmi < 16:
        print("Ur Severely")
elif 16 < bmi < 18.5:
        print("Ur Underweight")
elif 18.5 < bmi < 25:
        print("Ur Normal")
elif 25 < bmi < 30:
        print("Ur OverWeight")
else:
        print("Ur Obese")

