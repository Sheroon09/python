Name = input("Enter the Name: ")
age = int(input("Enter the Age : "))
score = float(input("Enter the Score : "))

print(f"User given name as : {Name}")
print(f"User given his age as : {age}")
print(f"User given his score as : {score}")

if age >= 18:
    print(f"{Name} is Adult")
else:
    print(f"{Name} is Minor")

if score >= 90:
    print(f"{Name} Grade is A")
elif score >=70:
    print(f"{Name} Grade is B")
elif score >=50:
    print(f"{Name} Grade is C")
elif score <35:
    print(f"{Name} has failed to get the Good Score")

if age >= 20:
    if score >= 75:
        print(f"{Name} is eligible scholarship with student loan")
    else:
        print(f"{Name} is eligible only for scholarship")
else:
    print(f"{Name} is not eligible for scholarship")

subjects = [f'{input("Enter three Subject: Subject1  ")}', f'{input("subject 2 ")}', f'{input("Subject 3 ")}']
for subject in subjects:
    print(f"{Name} has intrest in {subject}")

count = int(input("enter the value to itretate upto 5 "))
while count < 6:
    print(count)
    count += 1


