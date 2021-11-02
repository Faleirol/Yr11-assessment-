# version 2 branch
# all the questions function

Generator_Ans = []


# Challenge function - this function ask the user if they want to do a challenge if yes it will pick a random number to have the user write that amount of chapters
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


# Single question function - the user is able to choose a specific function to run from the list. The answer is returned to single_ans1
def single_question():
    # noinspection PyGlobalUndefined
    global question_choice, single_ans1
    choice_list = ["Type of genre (Genre)", "Type of main character (type main_cha)",
                   "Amount of main character (type num_cha)", "Type of ending (type end)"]
    print(choice_list)
    question_choice = input("Pick which question you would like to run")
    choice = [genre, main_cha, num_cha, end_fun]
    print(question_choice)
    if question_choice == "genre":
        single_ans1 = choice[0]()
    elif question_choice == "main_cha":
        single_ans1 = choice[1]()
    elif question_choice == "num_cha":
        single_ans1 = choice[2]()
    elif question_choice == "end":
        single_ans1 = choice[3]()

    else:
        print("Pick choice from list")
    return single_ans1
    pass


def genre():
    genre_answer = ["Horror", "horror", "HORROR", "Sci-fi", "sci-fi", "SCI-FI", "sci fi", "Sci fi", "SCI FI", "Comedy",
                    "comedy", "COMEDY", "Thriller", "thriller", "THRILLER", "Drama", "drama", "DRAMA", "Fantasy",
                    "fantasy", "FANTASY", "Action", "action", "ACTION", "Crime", "crime", "CRIME"]
    genre_list = ["Horror", "Sci-fi", "Comedy", "Thriller", "Drama", "Fantasy", "Action", "Crime"]
    print(genre_list)
    genre_choice = input("Pick a genre")
    while genre_choice not in genre_answer:
        genre_choice = input("Pick a genre")

    print("Data stored")
    return genre_choice


def main_cha():
    main_character_list = ["Criminal", "Hero", "Villain", "Teenager", "Mythical character", "Alien", "Human", "Animal"]
    print(main_character_list)
    main_answer = ["Criminal", "criminal", "CRIMINAL", "Hero", "hero", "HERO", "Villain", "villain", "VILLAIN",
                   "Teenager", "teenager", "TEENAGER", "Mythical character", "mythical character", "MYTHICAL CHARACTER",
                   "Alien", "alien", "ALIEN", "Human", "human", "HUMAN", "Animal", "animal", "ANIMAL"]
    main_cha_choice = input("Pick a main character")
    while main_cha_choice not in main_answer:
        main_cha_choice = input("Pick a main character")

    print("Data stored")
    return main_cha_choice


def num_cha():
    num_character_list = ["1 character", "A duo", "3 character", "A group (4+)"]
    print(num_character_list)
    num_answer = ["1 character", "one character", "One Character", "One character", " ONE CHARACTER", "1 CHARACTER",
                  "A duo", "a duo", "A DUO", "a Duo", "duo", "Duo", "DUO", "3 character", "3 Character", "3 CHARACTER",
                  "Three character", "three character", "Three Character", "three Character", "THREE CHARACTER",
                  "A group", "a group", "A Group", "A GROUP"]
    num_cha_choice = input("Pick an amount of main character(s)")
    while num_cha_choice not in num_answer:
        num_cha_choice = input("Pick an amount of main character(s)")

    print("Data stored")
    return num_cha_choice


def end_fun():
    ending_list = ["Happy ending", "Sad ending", "Cliffhanger ending", "Abrupt ending", "Plot twist ending"]
    print(ending_list)
    end_answer = ["Happy ending", "happy ending", "Happy Ending", "HAPPY ENDING", "Happy", "happy", "HAPPY",
                  "Sad ending", "sad ending", "Sad Ending", "SAD ENDING", "Sad", "sad", "SAD", "Cliffhanger ending",
                  "cliffhanger ending", "Cliffhanger Ending", "CLIFFHANGER ENDING", "Cliffhanger", "cliffhanger",
                  "CLIFFHANGER", "Abrupt ending", "abrupt ending", "Abrupt Ending", "ABRUPT ENDING", "Abrupt", "abrupt",
                  "ABRUPT", "Plot twist ending", "Plot Twist Ending", "plot twist ending", "PLOT TWIST ENDING",
                  "Plot twist", "plot twist", "Plot Twist", "PLOT TWIST"]
    end_choice = input("Pick a type of ending")
    while end_choice not in end_answer:
        end_choice = input("Pick a type of ending")

    print("Data stored")
    return end_choice


# main code - This is where all the functions are called and where in program they ask which function to run (single or all) then ask if they want to run the challenge function
global question_choice
Choice_for_questions = 0
print("Welcome to Story Generator!")
print("Do you want to answer all questions or a single question?")
print("Press 1 for all\nPress 2 for single\nPress 3 to quit")

while Choice_for_questions != 1 or Choice_for_questions != 2 or Choice_for_questions != 3:
    try:
        Choice_for_questions = int(input("Enter your choice [1 or 2] to quit press 3"))
        if Choice_for_questions == 1:
            print("All function")
            genre = genre()
            main_character = main_cha()
            num_char = num_cha()
            ending = end_fun()
            print(
                f"Genre: {genre} \n Main character: {main_character} \n Amount of main characters: {num_char} \n  Type of ending: {ending} \n")
            challenge()
        elif Choice_for_questions == 2:
            print("Single function")
            single_ans = single_question()
            Generator_Ans.append(single_ans)
            print(Generator_Ans)
            challenge()

        elif Choice_for_questions == 3:
            print("Enjoy writing!")
            quit()
    except ValueError:
        print("Press 1 for all\nPress 2 for single\nPress 3 to quit")
