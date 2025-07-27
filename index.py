Age = int(input("Enter your age "))
print("Age=",Age)
if 10 <= Age <= 13:
    print("You are eligible to write this exam.")
else:
    print("You are not eligible to write this exam.")
from datetime import datetime, time
cutoff_time = time(21, 0)  
current_time = datetime.now().time()
if current_time < cutoff_time:
    print("It's before 9 PM. Continue .")
else:
    print("It's after 9 PM. Stop .")