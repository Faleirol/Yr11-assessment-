print("Welcome to Story Generator!")
All_answer = ["All", "all", "ALL", "All questions", "all questions", "ALL QUESTIONS"]
Single_answer = ["Single", "single", "SINGLE", "One", "one", "ONE"]
Choice_for_questions = input("Would you like to run all the questions or just one?")
print(Choice_for_questions)
if Choice_for_questions in All_answer:
    print("All function")
elif Choice_for_questions in Single_answer:
    print("Single function")
else:
    print("Pick the 2 options")
