num_character_list = ["1 character", "A duo", "3 character", "A group (4+)"]
print(num_character_list)
num_answer = ["1 character", "one character", "One Character", "One character", " ONE CHARACTER", "1 CHARACTER", "A duo", "a duo", "A DUO", "a Duo", "duo", "Duo", "DUO", "3 character", "3 Character", "3 CHARACTER", "Three character", "three character", "Three Character", "three Character", "THREE CHARACTER", "A group", "a group", "A Group", "A GROUP"]
num_character_fun = ""
while num_character_fun not in num_answer:
    num_character_fun = 'z'
    num_character_fun = input("Pick an amount of main character(s)")

    print("In loop")

print("Out of loop")
