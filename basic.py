#Basic Quiz Application without GUI

#Taking Quetions Input
questions =(
    "Who is known as the “Father of Modern Physics” ?",
    "Who painted “The Starry Night”? ",
    "Who discovered penicillin?",
    "What is the largest bird in the world?",
    "Which gas makes up the majority of Earth's atmosphere?"
)

#Choices Available 
choices =(
    ("A.Albert Einstein ","B.Isaac Newton ","C.Marie Curie ","D.Niels Bohr "),
    ("A.Michelangelo ","B.Leonardo da Vinci ","C.Pablo Picasso ","D.Vincent van Gogh "),
    ("A.Alexander Fleming ","B.Dmitri Ivanovsky ","C.Louis Pasteur ","D.Joseph Lister "),
    ("A.Eagle ","B.Chicken ","C.Ostrich","D.Owl "),
    ("A.Oxygen ","B.Nitrogen ","C.Carbon-di-oxide ","D.Argon")
)

#Actual Answers 
answers =( "A", "D", "A", "C", "B")

correct_ans=(
    "Albert Einstein, a German-born physicist, is widely recognized as the 'Father of Modern Physics.' Born in 1879 in Ulm, Germany, Einstein revolutionized our understanding of space, time, and the nature of light with his groundbreaking theories of relativity and his contributions to quantum physics.",
    "'The Starry Night' is one of the most famous paintings by the Dutch post-impressionist artist Vincent van Gogh. Created in 1889, it depicts a swirling night sky filled with stars over a small town with a prominent cypress tree in the foreground.Van Gogh painted it while staying at the Saint-Paul-de-Mausole asylum in Saint-Rémy-de-Provence, France, following a period of intense mental health struggles.",
    "Alexander Fleming, a Scottish bacteriologist, is credited with discovering penicillin, the world's first antibiotic, in 1928. This discovery marked a significant milestone in medical history, revolutionizing the treatment of bacterial infections and saving countless lives.",
    "The ostrich (Struthio camelus) holds the title of the world's largest bird. Native to Africa, ostriches are notable for their remarkable size, speed, and distinctive features. ",
    "Nitrogen is the most abundant gas in Earth's atmosphere, comprising about 78percent of the air we breathe. It is a colorless, odorless, and inert gas essential for all living organisms, playing a critical role in the formation of amino acids, proteins, and nucleic acids."
)

#intialising score and iterating questions  
score = 0
ques_num =0 

print("Lets Take a General Knowledge Quiz")
print("__________________________________________")

#Showing the Question 
for question in questions :
    print (question)

    #Printing the Choices
    print("The Options Are:")
    for choice in choices[ques_num] :
        print(choice) 
    print("---------------------------------")

    #Taking the Option input of the user
    opt = input("Enter The answer :").upper()

    #Checking the chosen option
    #If the Answer is correct
    if opt ==answers[ques_num]:
        print("You have given the correct answers")
        #Incrementing the score if the answer is correct
        score +=1

    #If Answer is wrong
    else:
        print("Sorry The Answer is wrong")
        print(f"{answers[ques_num] } is the correct answer.")
        print("Explanation :")
        print(correct_ans[ques_num])
    print("__________________________________________________")
    ques_num +=1

#Printing the Score 
print(f"Your Final Score is {score} out of 5")

#Analyzing according to the score 
if score == 5:
    print("Excellent!! You have got all correct")
elif score == 4:
    print("Very Good!!")
elif score == 3:
    print("Average")
else:
    print("Can do better")

