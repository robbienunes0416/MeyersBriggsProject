import sys

print("''The purpose of the Myers-Briggs Type Indicator® (MBTI®) personality inventory is to make the theory of psychological types described by C. G. Jung understandable and useful in people's \nlives. The essence of the theory is that much seemingly random variation in the behavior is actually quite orderly and consistent, \nbeing due to basic differences in the ways individuals prefer to use their perception and judgment.'' ~ meyersbriggs.org")
# Source for text: http://www.myersbriggs.org/my-mbti-personality-type/mbti-basics/home.htm?bhcp=1
print( )
start = 0
quiz = 0
introvert_extrovert_value = 0
sensing_intuitive_value = 0
judging_percieving_value = 0
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
    print ("Instructions: This quiz will contain 60 statements that you are asked to respond with how you feel,\nranging from -3 to 3, -3 being strongly agreeing, 3 being strongly disagreeing, and 0 being neutral/unknown or unsure.")
    Q1 = input("You find it difficult to introduce yourself to other people.")
    introvert_extrovert_value += int(Q1)
    # 5/11/17 Quiz_Score is broken if any input besides a number is put in, needs to be fixed and also limit to -3<0<3?
    if introvert_extrovert_value != int(Q1):
        print("Unknown answer. Please try again.")
    else:
        print(introvert_extrovert_value) # 5/12/17 Changed quiz_score variable to introvert_extrovert_value - each question has to be INTERPRETED to be assigned to a value.
        quiz += 1
        break
while quiz == 2:
    Q2 = input("You often get so lost in your thoughts that you ignore people and their surroundings")
    sensing_intuitive_value += int(Q2)
    if sensing_intuitive_value != int(Q2):
        print("Unkown answer. Please try again.")
    else:
        print(sensing_intuitive_value)
        quiz += 1
        break
while quiz == 3:
    Q3 = input("You try to respond to your e-mails as soon as possible and cannot stand a messy inbox.")
    judging_percieving_value += int(Q3)
    if judging_percieving_value != int(Q3):
        print("Unknown answer. Please try again.")
    else:
        print(judging_percieving_value)
        quiz += 1
        break       # 5/12/17 @ 10:30 - program works as intended, keep repeating the while loop function but must find a limit for the numbers.
while quiz == 4:
    Q4 = input("You find it easy to stay relaxed and focused even when there is some pressure.")
    