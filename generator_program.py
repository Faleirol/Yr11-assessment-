def all_question():
    genre_answer = ["Horror", "horror", "HORROR", "Sci-fi", "sci-fi", "SCI-FI", "sci fi", "Sci fi", "SCI FI", "Comedy", "comedy", "COMEDY", "Thriller", "thriller", "THRILLER", "Drama", "drama", "DRAMA", "Fantasy", "fantasy", "FANTASY", "Action", "action", "ACTION", "Crime", "crime", "CRIME"]
    genre_list = ["Horror", "Sci-fi", "Comedy", "Thriller", "Drama", "Fantasy", "Action", "Crime"]
    print(genre_list)
    genre_fun = input("Pick a genre")
    if genre_fun in genre_answer:
        print("your data stored")
    else:
        print("pick a genre in the list")

    main_character_list = ["Criminal", "Hero", "Villain", "Teenager", "Mythical character", "Alien", "Human", "Animal"]
    print(main_character_list)
    main_answer = ["Criminal", "criminal", "CRIMINAL", "Hero", "hero", "HERO", "Villain", "villain", "VILLAIN", "Teenager", "teenager", "TEENAGER", "Mythical character", "mythical character", "MYTHICAL CHARACTER", "Alien", "alien", "ALIEN", "Human", "human", "HUMAN", "Animal", "animal", "ANIMAL"]
    main_character_fun = input("Pick a main character")
    if main_character_fun in main_answer:
        print("data stored")
    else:
        print("pick one in the list")

    num_character_list = ["1 character", "A duo", "3 character", "A group (4+)"]
    print(num_character_list)
    num_answer = ["1 character", "one character", "One Character", "One character", " ONE CHARACTER", "1 CHARACTER", "A duo", "a duo", "A DUO", "a Duo", "duo", "Duo", "DUO", "3 character", "3 Character", "3 CHARACTER", "Three character", "three character", "Three Character", "three Character", "THREE CHARACTER", "A group", "a group", "A Group", "A GROUP"]
    num_character_fun = input("Pick an amount of main character(s)")
    if num_character_fun in num_answer:
        print("Data stored")
    else:
        print("pick one in the list")

    ending_list = ["Happy ending", "Sad ending", "Cliffhanger ending", "Abrupt ending", "Plot twist ending"]
    print(ending_list)
    end_answer = ["Happy ending", "happy ending", "Happy Ending", "HAPPY ENDING", "Happy", "happy", "HAPPY", "Sad ending", "sad ending", "Sad Ending", "SAD ENDING", "Sad", "sad", "SAD", "Cliffhanger ending", "cliffhanger ending", "Cliffhanger Ending", "CLIFFHANGER ENDING", "Cliffhanger", "cliffhanger", "CLIFFHANGER", "Abrupt ending", "abrupt ending", "Abrupt Ending", "ABRUPT ENDING", "Abrupt", "abrupt", "ABRUPT", "Plot twist ending", "Plot Twist Ending", "plot twist ending", "PLOT TWIST ENDING", "Plot twist", "plot twist", "Plot Twist", "PLOT TWIST"]
    ending_fun = input("Pick a type of ending")
    if ending_fun in end_answer:
        print("Data stored")
    else:
        print("Please pick from the list")


def challenge():
    import random
    dice = random.randint(1, 10)
    challenge_fun = input("Would you like to do the challenge?(for fun no reward)")
    challenge_answer = ["yes", "Yes", "YES", "y", "Y"]
    if challenge_fun in challenge_answer:
        print(f"Try and write {dice} chapters!")
    else:
        print("okay")


def single_questions():
    choice = ["Genre", "Main character", "Amount of main characters", "Type of ending"]
    print(choice)
    choice_fun = input("Pick which question you would like to run")
    while True:
        if choice_fun in choice:
            print("function")
        else:
            print("pick choice from list")


def genre():
    genre_answer = ["Horror", "horror", "HORROR", "Sci-fi", "sci-fi", "SCI-FI", "sci fi", "Sci fi", "SCI FI", "Comedy", "comedy", "COMEDY", "Thriller", "thriller", "THRILLER", "Drama", "drama", "DRAMA", "Fantasy", "fantasy", "FANTASY", "Action", "action", "ACTION", "Crime", "crime", "CRIME"]
    genre_list = ["Horror", "Sci-fi", "Comedy", "Thriller", "Drama", "Fantasy", "Action", "Crime"]
    print(genre_list)
    genre_fun = input("Pick a genre")
    if genre_fun in genre_answer:
        print("your data stored")
    else:
        print("pick a genre in the list")


def main_cha():
    main_character_list = ["Criminal", "Hero", "Villain", "Teenager", "Mythical character", "Alien", "Human", "Animal"]
    print(main_character_list)
    main_answer = ["Criminal", "criminal", "CRIMINAL", "Hero", "hero", "HERO", "Villain", "villain", "VILLAIN", "Teenager", "teenager", "TEENAGER", "Mythical character", "mythical character", "MYTHICAL CHARACTER", "Alien", "alien", "ALIEN", "Human", "human", "HUMAN", "Animal", "animal", "ANIMAL"]
    main_character_fun = input("Pick a main character")
    if main_character_fun in main_answer:
        print("data stored")
    else:
        print("pick one in the list")


def num_cha():
    num_character_list = ["1 character", "A duo", "3 character", "A group (4+)"]
    print(num_character_list)
    num_answer = ["1 character", "one character", "One Character", "One character", " ONE CHARACTER", "1 CHARACTER", "A duo", "a duo", "A DUO", "a Duo", "duo", "Duo", "DUO", "3 character", "3 Character", "3 CHARACTER", "Three character", "three character", "Three Character", "three Character", "THREE CHARACTER", "A group", "a group", "A Group", "A GROUP"]
    num_character_fun = input("Pick an amount of main character(s)")
    if num_character_fun in num_answer:
        print("Data stored")
    else:
        print("pick one in the list")


def end():
    ending_list = ["Happy ending", "Sad ending", "Cliffhanger ending", "Abrupt ending", "Plot twist ending"]
    print(ending_list)
    end_answer = ["Happy ending", "happy ending", "Happy Ending", "HAPPY ENDING", "Happy", "happy", "HAPPY", "Sad ending", "sad ending", "Sad Ending", "SAD ENDING", "Sad", "sad", "SAD", "Cliffhanger ending", "cliffhanger ending", "Cliffhanger Ending", "CLIFFHANGER ENDING", "Cliffhanger", "cliffhanger", "CLIFFHANGER", "Abrupt ending", "abrupt ending", "Abrupt Ending", "ABRUPT ENDING", "Abrupt", "abrupt", "ABRUPT", "Plot twist ending", "Plot Twist Ending", "plot twist ending", "PLOT TWIST ENDING", "Plot twist", "plot twist", "Plot Twist", "PLOT TWIST"]
    ending_fun = input("Pick a type of ending")
    if ending_fun in end_answer:
        print("Data stored")
    else:
        print("Please pick from the list")


# main code


print("Welcome to Story Generator!")
All_answer = ["All", "all", "ALL", "All questions", "all questions", "ALL QUESTIONS"]
Single_answer = ["Single", "single", "SINGLE", "One"]
Choice_for_questions = input("Would you like to run all the questions or just one?")
print(Choice_for_questions)
if Choice_for_questions in All_answer:
    print("All function")
    all_question()
elif Choice_for_questions in Single_answer:
    print("Single function")

else:
    print("Pick the 2 options")
