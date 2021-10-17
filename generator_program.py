# all the questions function
def all_question():
    genre_answer = ["Horror", "horror", "HORROR", "Sci-fi", "sci-fi", "SCI-FI", "sci fi", "Sci fi", "SCI FI", "Comedy", "comedy", "COMEDY", "Thriller", "thriller", "THRILLER", "Drama", "drama", "DRAMA", "Fantasy", "fantasy", "FANTASY", "Action", "action", "ACTION", "Crime", "crime", "CRIME"]
    genre_list = ["Horror", "Sci-fi", "Comedy", "Thriller", "Drama", "Fantasy", "Action", "Crime"]
    print(genre_list)
    User_genre = input("Pick a genre")
    while User_genre not in genre_answer:
        User_genre = input("Pick a genre")

    print("Data stored")

    main_character_list = ["Criminal", "Hero", "Villain", "Teenager", "Mythical character", "Alien", "Human", "Animal"]
    print(main_character_list)
    main_answer = ["Criminal", "criminal", "CRIMINAL", "Hero", "hero", "HERO", "Villain", "villain", "VILLAIN", "Teenager", "teenager", "TEENAGER", "Mythical character", "mythical character", "MYTHICAL CHARACTER", "Alien", "alien", "ALIEN", "Human", "human", "HUMAN", "Animal", "animal", "ANIMAL"]
    User_main = input("Pick a main character")
    while User_main not in main_answer:
        User_main = input("Pick a main character")

    print("Data stored")

    num_character_list = ["1 character", "A duo", "3 character", "A group (4+)"]
    print(num_character_list)
    num_answer = ["1 character", "one character", "One Character", "One character", " ONE CHARACTER", "1 CHARACTER", "A duo", "a duo", "A DUO", "a Duo", "duo", "Duo", "DUO", "3 character", "3 Character", "3 CHARACTER", "Three character", "three character", "Three Character", "three Character", "THREE CHARACTER", "A group", "a group", "A Group", "A GROUP"]
    User_num = input("Pick an amount of main character(s)")
    while User_num not in num_answer:
        User_num = input("Pick an amount of main character(s)")

    print("Data stored")

    ending_list = ["Happy ending", "Sad ending", "Cliffhanger ending", "Abrupt ending", "Plot twist ending"]
    print(ending_list)
    end_answer = ["Happy ending", "happy ending", "Happy Ending", "HAPPY ENDING", "Happy", "happy", "HAPPY", "Sad ending", "sad ending", "Sad Ending", "SAD ENDING", "Sad", "sad", "SAD", "Cliffhanger ending", "cliffhanger ending", "Cliffhanger Ending", "CLIFFHANGER ENDING", "Cliffhanger", "cliffhanger", "CLIFFHANGER", "Abrupt ending", "abrupt ending", "Abrupt Ending", "ABRUPT ENDING", "Abrupt", "abrupt", "ABRUPT", "Plot twist ending", "Plot Twist Ending", "plot twist ending", "PLOT TWIST ENDING", "Plot twist", "plot twist", "Plot Twist", "PLOT TWIST"]
    User_end = input("Pick a type of ending")
    while User_end not in end_answer:
        User_end = input("Pick a type of ending")

    print("Data stored")
    return User_end, User_genre, User_main, User_num


# Challenge function
def challenge():
    import random
    dice = random.randint(1, 10)
    user_choice = input("Would you like to do the challenge?(for fun no reward)")
    challenge_answer = ["yes", "Yes", "YES", "y", "Y"]
    if user_choice in challenge_answer:
        print(f"Try and write {dice} chapters!")
        return user_choice
    else:
        print("okay")



# Single question function
def single_question():

    choice_list = ["Type of genre (type genre)", "Type of main character (type main_cha)", "Amount of main character (type num_cha)", "Type of ending (type end)"]
    question_choice = input("Pick which question you would like to run")
    choice = [genre_choice, main_cha_choice, num_cha_choice, end_choice]
    print(question_choice)
    if question_choice == "genre":
        choice[0]()
    elif question_choice == "main_cha":
        choice[1]()
    elif question_choice == "num_cha":
        choice[2]()
    elif question_choice == "end":
        choice[3]()

    else:
        print("Pick choice from list")
    return genre_choice, main_cha_choice, num_cha_choice, end_choice, question_choice


def genre_choice():
    genre_answer = ["Horror", "horror", "HORROR", "Sci-fi", "sci-fi", "SCI-FI", "sci fi", "Sci fi", "SCI FI", "Comedy", "comedy", "COMEDY", "Thriller", "thriller", "THRILLER", "Drama", "drama", "DRAMA", "Fantasy", "fantasy", "FANTASY", "Action", "action", "ACTION", "Crime", "crime", "CRIME"]
    genre_list = ["Horror", "Sci-fi", "Comedy", "Thriller", "Drama", "Fantasy", "Action", "Crime"]
    print(genre_list)
    genre_choice = input("Pick a genre")
    while genre_choice not in genre_answer:
        genre_choice = input("Pick a genre")

    print("Data stored")
    return genre_choice


def main_cha_choice():
    main_character_list = ["Criminal", "Hero", "Villain", "Teenager", "Mythical character", "Alien", "Human", "Animal"]
    print(main_character_list)
    main_answer = ["Criminal", "criminal", "CRIMINAL", "Hero", "hero", "HERO", "Villain", "villain", "VILLAIN", "Teenager", "teenager", "TEENAGER", "Mythical character", "mythical character", "MYTHICAL CHARACTER", "Alien", "alien", "ALIEN", "Human", "human", "HUMAN", "Animal", "animal", "ANIMAL"]
    main_cha_choice = input("Pick a main character")
    while main_cha_choice not in main_answer:
        main_cha_choice = input("Pick a main character")

    print("Data stored")
    return main_cha_choice


def num_cha_choice():
    num_character_list = ["1 character", "A duo", "3 character", "A group (4+)"]
    print(num_character_list)
    num_answer = ["1 character", "one character", "One Character", "One character", " ONE CHARACTER", "1 CHARACTER", "A duo", "a duo", "A DUO", "a Duo", "duo", "Duo", "DUO", "3 character", "3 Character", "3 CHARACTER", "Three character", "three character", "Three Character", "three Character", "THREE CHARACTER", "A group", "a group", "A Group", "A GROUP"]
    num_cha_choice = input("Pick an amount of main character(s)")
    while num_cha_choice not in num_answer:
        num_cha_choice = input("Pick an amount of main character(s)")

    print("Data stored")
    return num_cha_choice


def end_choice():
    ending_list = ["Happy ending", "Sad ending", "Cliffhanger ending", "Abrupt ending", "Plot twist ending"]
    print(ending_list)
    end_answer = ["Happy ending", "happy ending", "Happy Ending", "HAPPY ENDING", "Happy", "happy", "HAPPY", "Sad ending", "sad ending", "Sad Ending", "SAD ENDING", "Sad", "sad", "SAD", "Cliffhanger ending", "cliffhanger ending", "Cliffhanger Ending", "CLIFFHANGER ENDING", "Cliffhanger", "cliffhanger", "CLIFFHANGER", "Abrupt ending", "abrupt ending", "Abrupt Ending", "ABRUPT ENDING", "Abrupt", "abrupt", "ABRUPT", "Plot twist ending", "Plot Twist Ending", "plot twist ending", "PLOT TWIST ENDING", "Plot twist", "plot twist", "Plot Twist", "PLOT TWIST"]
    end_choice = input("Pick a type of ending")
    while end_choice not in end_answer:
        end_choice = input("Pick a type of ending")

    print("Data stored")
    return end_choice


# main code


print("Welcome to Story Generator!")
All_answer = ["All", "all", "ALL", "All questions", "all questions", "ALL QUESTIONS"]
Single_answer = ["Single", "single", "SINGLE", "one"]
Choice_for_questions = input("Would you like to run all the questions or just one?")
print(Choice_for_questions)
if Choice_for_questions.lower() in All_answer:
    print("All function")
    User_end, User_genre, User_main, User_num = all_question()
elif Choice_for_questions in Single_answer:
    print("Single function")
    genre_choice, main_cha_choice, num_cha_choice, end_choice, question_choice = single_question()

else:
    print("Pick the 2 options")

user_choice = challenge()
if Choice_for_questions == All_answer:
    print("Genre:"User_genre /n)
else:
     print(question_choice)

print("Enjoy writing!")
