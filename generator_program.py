# all the questions function
def all_question():
    genre_answer = ["Horror", "horror", "HORROR", "Sci-fi", "sci-fi", "SCI-FI", "sci fi", "Sci fi", "SCI FI", "Comedy", "comedy", "COMEDY", "Thriller", "thriller", "THRILLER", "Drama", "drama", "DRAMA", "Fantasy", "fantasy", "FANTASY", "Action", "action", "ACTION", "Crime", "crime", "CRIME"]
    genre_list = ["Horror", "Sci-fi", "Comedy", "Thriller", "Drama", "Fantasy", "Action", "Crime"]
    print(genre_list)
    genre_choice = input("Pick a genre")
    while genre_choice not in genre_answer:
        genre_choice = input("Pick a genre")

    print("Data stored")

    main_character_list = ["Criminal", "Hero", "Villain", "Teenager", "Mythical character", "Alien", "Human", "Animal"]
    print(main_character_list)
    main_answer = ["Criminal", "criminal", "CRIMINAL", "Hero", "hero", "HERO", "Villain", "villain", "VILLAIN", "Teenager", "teenager", "TEENAGER", "Mythical character", "mythical character", "MYTHICAL CHARACTER", "Alien", "alien", "ALIEN", "Human", "human", "HUMAN", "Animal", "animal", "ANIMAL"]
    main_character_choice = input("Pick a main character")
    while main_character_choice not in main_answer:
        main_character_choice = input("Pick a main character")

    print("Data stored")

    num_character_list = ["1 character", "A duo", "3 character", "A group (4+)"]
    print(num_character_list)
    num_answer = ["1 character", "one character", "One Character", "One character", " ONE CHARACTER", "1 CHARACTER", "A duo", "a duo", "A DUO", "a Duo", "duo", "Duo", "DUO", "3 character", "3 Character", "3 CHARACTER", "Three character", "three character", "Three Character", "three Character", "THREE CHARACTER", "A group", "a group", "A Group", "A GROUP"]
    num_character_choice = input("Pick an amount of main character(s)")
    while num_character_choice not in num_answer:
        num_character_choice = input("Pick an amount of main character(s)")

    print("Data stored")

    ending_list = ["Happy ending", "Sad ending", "Cliffhanger ending", "Abrupt ending", "Plot twist ending"]
    print(ending_list)
    end_answer = ["Happy ending", "happy ending", "Happy Ending", "HAPPY ENDING", "Happy", "happy", "HAPPY", "Sad ending", "sad ending", "Sad Ending", "SAD ENDING", "Sad", "sad", "SAD", "Cliffhanger ending", "cliffhanger ending", "Cliffhanger Ending", "CLIFFHANGER ENDING", "Cliffhanger", "cliffhanger", "CLIFFHANGER", "Abrupt ending", "abrupt ending", "Abrupt Ending", "ABRUPT ENDING", "Abrupt", "abrupt", "ABRUPT", "Plot twist ending", "Plot Twist Ending", "plot twist ending", "PLOT TWIST ENDING", "Plot twist", "plot twist", "Plot Twist", "PLOT TWIST"]
    end_choice = input("Pick a type of ending")
    while end_choice not in end_answer:
        end_choice = input("Pick a type of ending")

    print("Data stored")


# Challenge function
def challenge():
    import random
    dice = random.randint(1, 10)
    user_choice = input("Would you like to do the challenge?(for fun no reward)")
    challenge_answer = ["yes", "Yes", "YES", "y", "Y"]
    if user_choice in challenge_answer:
        print(f"Try and write {dice} chapters!")
    else:
        print("okay")


# Single question function
def single_question():
    choice_list = ["Type of genre (type genre)", "Type of main character (type main_cha)", "Amount of main character (type num_cha)", "Type of ending (type end)"]
    print(choice_list)
    choice = [genre, main_cha, num_cha, end]
    user_choice = input("Pick which question you would like to run")
    while True:
        if user_choice == "genre":
            choice[0]()

        else:
            print("pick choice from list")

        if user_choice == "main_cha":
            choice[1]()

        else:
            print("Pick choice from list")

        if user_choice == "num_cha":
            choice[2]()

        else:
            print("Pick choice from list")

        if user_choice == "end":
            choice[3]()

        else:
            print("Pick choice from list")


def genre():
    genre_answer = ["Horror", "horror", "HORROR", "Sci-fi", "sci-fi", "SCI-FI", "sci fi", "Sci fi", "SCI FI", "Comedy", "comedy", "COMEDY", "Thriller", "thriller", "THRILLER", "Drama", "drama", "DRAMA", "Fantasy", "fantasy", "FANTASY", "Action", "action", "ACTION", "Crime", "crime", "CRIME"]
    genre_list = ["Horror", "Sci-fi", "Comedy", "Thriller", "Drama", "Fantasy", "Action", "Crime"]
    print(genre_list)
    genre_choice = input("Pick a genre")
    while genre_choice not in genre_answer:
        genre_choice = input("Pick a genre")

    print("Data stored")


def main_cha():
    main_character_list = ["Criminal", "Hero", "Villain", "Teenager", "Mythical character", "Alien", "Human", "Animal"]
    print(main_character_list)
    main_answer = ["Criminal", "criminal", "CRIMINAL", "Hero", "hero", "HERO", "Villain", "villain", "VILLAIN", "Teenager", "teenager", "TEENAGER", "Mythical character", "mythical character", "MYTHICAL CHARACTER", "Alien", "alien", "ALIEN", "Human", "human", "HUMAN", "Animal", "animal", "ANIMAL"]
    main_character_choice = input("Pick a main character")
    while main_character_choice not in main_answer:
        main_character_choice = input("Pick a main character")

    print("Data stored")


def num_cha():
    num_character_list = ["1 character", "A duo", "3 character", "A group (4+)"]
    print(num_character_list)
    num_answer = ["1 character", "one character", "One Character", "One character", " ONE CHARACTER", "1 CHARACTER", "A duo", "a duo", "A DUO", "a Duo", "duo", "Duo", "DUO", "3 character", "3 Character", "3 CHARACTER", "Three character", "three character", "Three Character", "three Character", "THREE CHARACTER", "A group", "a group", "A Group", "A GROUP"]
    num_character_choice = input("Pick an amount of main character(s)")
    while num_character_choice not in num_answer:
        num_character_choice = input("Pick an amount of main character(s)")

    print("Data stored")


def end():
    ending_list = ["Happy ending", "Sad ending", "Cliffhanger ending", "Abrupt ending", "Plot twist ending"]
    print(ending_list)
    end_answer = ["Happy ending", "happy ending", "Happy Ending", "HAPPY ENDING", "Happy", "happy", "HAPPY", "Sad ending", "sad ending", "Sad Ending", "SAD ENDING", "Sad", "sad", "SAD", "Cliffhanger ending", "cliffhanger ending", "Cliffhanger Ending", "CLIFFHANGER ENDING", "Cliffhanger", "cliffhanger", "CLIFFHANGER", "Abrupt ending", "abrupt ending", "Abrupt Ending", "ABRUPT ENDING", "Abrupt", "abrupt", "ABRUPT", "Plot twist ending", "Plot Twist Ending", "plot twist ending", "PLOT TWIST ENDING", "Plot twist", "plot twist", "Plot Twist", "PLOT TWIST"]
    end_choice = input("Pick a type of ending")
    while end_choice not in end_answer:
        end_choice = input("Pick a type of ending")

    print("Data stored")


# main code


print("Welcome to Story Generator!")
All_answer = ["All", "all", "ALL", "All questions", "all questions", "ALL QUESTIONS"]
Single_answer = ["Single", "single", "SINGLE", "one"]
Choice_for_questions = input("Would you like to run all the questions or just one?")
print(Choice_for_questions)
if Choice_for_questions.lower() in All_answer:
    print("All function")
    all_question()
elif Choice_for_questions in Single_answer:
    print("Single function")
    single_question()

else:
    print("Pick the 2 options")

challenge()

print("user choice list here")
print("Enjoy writing!")
