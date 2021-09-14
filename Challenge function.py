import random
dice = random.randint(1, 10)
Challenge_fun = input("Would you like to do the challenge?(for fun no reward)")
Challenge_answer = ["yes", "Yes", "YES", "y", "Y"]
if Challenge_fun in Challenge_answer:
    print("Try and write", dice, "chapters")
else:
    print("okay")
