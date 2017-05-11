import sys

print("''The purpose of the Myers-Briggs Type Indicator® (MBTI®) personality inventory is to make the theory of psychological types described by C. G. Jung understandable and useful in people's \nlives. The essence of the theory is that much seemingly random variation in the behavior is actually quite orderly and consistent, \nbeing due to basic differences in the ways individuals prefer to use their perception and judgment.'' ~ meyersbriggs.org")
# Source for text: http://www.myersbriggs.org/my-mbti-personality-type/mbti-basics/home.htm?bhcp=1
print( )
start = 0
quiz = 0
quiz_score = 0
while start != 1:
    quiz == 0
    (initialize) = input ("Would you like to start the quiz? y/n")
    if str.lower(initialize) == "y":
        print ("Starting quiz...")
        quiz = 1
        start = 1
    elif str.lower(initialize) == "n":
        quit("Quitting program. Have a nice day.")
    else:
        print("Response unrecognized, please try again.")
while quiz == 1:
    quiz_score = 0
    print ("Instructions: This quiz will contain 60 statements that you are asked to respond with how you feel, ranging from -3 to 3, -3 being strongly agreeing, 3 being strongly disagreeing, and 0 being neutral/unknown or unsure.")
    Q1 = input ("You find it difficult to introduce yourself to other people.")
    quiz_score += int(Q1)
    # 5/11/17 Quiz_Score is broken if any input besides a number is put in, needs to be fixed and also limit to -3<0<3?
    if quiz_score != int(Q1):
        print("Unknown answer. Please try again.")
    else:
        print(quiz_score)



