
# All the list information
Genre_list = ["Horror", "Sci-fi", "Comedy", "Thriller", "Drama", "Fantasy", "Action", "Crime"]
Main_character_list = ["Criminal", "Hero", "Villain", "Teenager", "Mythical character", "Alien", "Human", "Animal"]
Num_character_list = ["1 character", "A duo", "3 friends", "A group (4+)"]
Ending_list = ["Happy ending", "Sad ending", "Cliffhanger ending", "Abrupt ending", "Plot twist ending"]
Choice_list = ["Genre", "Main character", "Amount of main characters", "Type of ending"]
# Beginning of the program
print("Welcome to Story Generator!")
All_answer = ["All", "all", "ALL", "All questions", "all questions", "ALL QUESTIONS"]
Single_answer = ["Single", "single", "SINGLE", "One"]
Choice_for_questions = input("Would you like to run all the questions or just one?")
print(Choice_for_questions)
if Choice_for_questions in All_answer:
    print("All function")
elif Choice_for_questions in Single_answer:
    print("Single function")
else:
    print("Pick the 2 options")
