print ("WELCOME TO COMPUTER BASE TEST FOR KIDTECH")
score = 0
question1 = "Who is the president of Nigeria?"
optionA = "Muhammadu Buhari"
optionB = "Abubakar Atiku"
optionC = "Olusegun Obasanjo"
optionD = "Wole Soyinka"

print("Question 1: ", question1)
print("A: " + optionA + "  " + "B: " + optionB)
print("C: " + optionC + "  " + "D: " + optionD)
print("--------------------------------------------------------")
print("Enter A, B, C, D to choose your answer")

useroption = input()
if useroption == "A":
    score = score + 2
    print("Correct")
else:
    score = score + 0
    print("Incorrect")
    
question2 = "Who is the executive governor of Kwara State?"
optionA = "Bukola Saraki"
optionB = "Abdulrahman Abdulrazaq"
optionC = "Tafawa Belewa"
optionD = "abubakar atiku"
print("Question 2: ", question2)
print("A: " + optionA + "  " + "B: " + optionB)
print("C: " + optionC + "  " + "D: " + optionD)
print("-----------------------------------------------------")
print("Enter A, B, C, D to choose your answer")

useroption = input()
if useroption == "B":
    score = score + 2
    print("Correct")
else:
    score = score + 0
    print("Incorrect")

question3 = "Who designed the nigeria flag?"
optionA = "Taiwo Akinkumi"
optionB = "Shawn white"
optionC = "Cooper bares"
optionD = "Meacheal D Cohen"
print("Question 3:", question3)
print("A: " + optionA + "  " + "B: " + optionB)
print("C: " + optionC + "  " + "D: " + optionD)
print("-----------------------------------------------------")
print("Enter A, B, C, D to choose your answer")

useroption = input()
if useroption == "A":
    score = score + 2
    print("correct")
else:
    score = score + 0
    print("Incorrect")

question4 = "Who is the first president Of Nigeria?"
optionA = "Nmadzi Azikwe"
optionB = "Tafawa Balewa "
optionC = "Wole Soyinka"
optionD = "Muhammadu Buhari "

print("Question 4: ", question4)
print("A: " + optionA + "  " + "B: " + optionB)
print("C: " + optionC + "  " + "D: " + optionD)
print("-----------------------------------------------------")
print("Enter A, B, C, D to choose your answer")

useroption = input()
if useroption == "A":
    score = score + 2
    print("correct")
else:
    score = score + 0
    print("Incorrect")

question5 = "What year did Nigeria gain independence?"
optionA = "1963"
optionB = "1960"
optionC = "1914"
optionD = "1810"
print("Question 5: ", question5)
print("A: " + optionA + "  " + "B: " + optionB)
print("C: " + optionC + "  " + "D: " + optionD)
print("-----------------------------------------------------")
print("Enter A, B, C, D to choose your answer")

useroption = input()
if useroption == "B":
    score = score + 2
    print("correct")
else:
    score = score + 0
    print("Incorrect")

question6 = "When did Nigeria celebrate her 60th anniversary?"
optionA = "2020"
optionB = "2016 "
optionC = "2012"
optionD = "2019 "
print("Question 6: ", question6)
print("A: " + optionA + "  " + "B: " + optionB)
print("C: " + optionC + "  " + "D: " + optionD)
print("-----------------------------------------------------")
print("Enter A, B, C, D to choose your answer")

useroption = input()
if useroption == "A":
    score = score + 2
    print("correct")
else:
    score = score + 0
    print("Incorrect")

question7 = "Who Stoped the Killing of Twins in Calabar?"
optionA = "Mary Slessor"
optionB = "Okonkwo amadi"
optionC = "Wole Soyinka"
optionD = "Lord Lugard "
print("Question 7: ", question7)
print("A: " + optionA + "  " + "B: " + optionB)
print("C: " + optionC + "  " + "D: " + optionD)
print("-----------------------------------------------------")
print("Enter A, B, C, D to choose your answer")

useroption = input()
if useroption == "A":
    score = score + 2
    print("correct")
else:
    score = score + 0
    print("Incorrect")

question8 = "How Many Geopolitical Zones are there in Nigeria?"
optionA = "9"
optionB = "5 "
optionC = "2"
optionD = "6 "
print("Question 8: ", question8)
print("A: " + optionA + "  " + "B: " + optionB)
print("C: " + optionC + "  " + "D: " + optionD)
print("-----------------------------------------------------")
print("Enter A,B,C,D to choose your answer")

useroption = input()
if useroption == "D":
    score = score + 2
    print("correct")
else:
    score = score + 0
    print("Incorrect")

question9 = "How Many Local Governments do we have In Ngeria?"
optionA = "500"
optionB = "720"
optionC = "774"
optionD = "180"
print("Question 9: ", question9)
print("A: " + optionA + "  " + "B: " + optionB)
print("C: " + optionC + "  " + "D: " + optionD)
print("-----------------------------------------------------")
print("Enter A, B, C, D to choose your answer")

useroption = input()
if useroption == "C":
    score = score + 2
    print("correct")
else:
    score = score + 0
    print("Incorrect")

question10 = "What Is The Full Meaning Of NTA "
optionA = "Nigerian Television Authority "
optionB = "National  Television Association "
optionC = "Nigeria Television Agenda "
optionD = "Nation Talking association "
print("Question 10: ", question10)
print("A: " + optionA + "  " + "B: " + optionB)
print("C: " + optionC + "  " + "D: " + optionD)
print("-----------------------------------------------------")
print("Enter A, B, C, D to choose your answer")

useroption = input()
if useroption == "A":
    score = score + 2
    print("correct")
else:
    score = score + 0
    print("Incorrect")

percentage = int((score/20)*100)
print("Your Percentage Score is : ", percentage,"%")
print("Your Score is : ", score)
print("Thank you for Taking this Test")
