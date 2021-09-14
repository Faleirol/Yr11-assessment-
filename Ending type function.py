Ending_list = ["Happy ending", "Sad ending", "Cliffhanger ending", "Abrupt ending", "Plot twist ending"]
print(Ending_list)
End_answer = ["Happy ending", "happy ending", "Happy Ending", "HAPPY ENDING", "Happy", "happy", "HAPPY", "Sad ending", "sad ending", "Sad Ending", "SAD ENDING", "Sad", "sad", "SAD", "Cliffhanger ending", "cliffhanger ending", "Cliffhanger Ending", "CLIFFHANGER ENDING", "Cliffhanger", "cliffhanger", "CLIFFHANGER", "Abrupt ending", "abrupt ending", "Abrupt Ending", "ABRUPT ENDING", "Abrupt", "abrupt", "ABRUPT", "Plot twist ending", "Plot Twist Ending", "plot twist ending", "PLOT TWIST ENDING", "Plot twist", "plot twist", "Plot Twist", "PLOT TWIST"]
Ending_fun = input("Pick a type of ending")
if Ending_fun in End_answer:
    print("Data stored")
else:
    print("Please pick from the list")
