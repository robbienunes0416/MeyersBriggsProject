import sys #Perhaps unneeded but unsure at current refracting stage
import time #Used for time.sleep

print("''The purpose of the Myers-Briggs Type Indicator® (MBTI®) personality inventory is to make the theory of psychological types described by C. G. Jung understandable and useful in people's \nlives. The essence of the theory is that much seemingly random variation in the behavior is actually quite orderly and consistent, \nbeing due to basic differences in the ways individuals prefer to use their perception and judgment.'' ~ meyersbriggs.org")
# Source for text: http://www.myersbriggs.org/my-mbti-personality-type/mbti-basics/home.htm?bhcp=1
print( )

instructions = False
start = False
quiz = False
end_quiz = False
restart_quiz = False
extrovert_value = 0
introvert_value = 0
sensing_value = 0
intuitive_value = 0
thinking_value = 0
feeling_value = 0
judging_value = 0
perceiving_value = 0
e_i_value = ()
s_i_value = ()
t_f_value = ()
j_p_value = ()
personality_type = ()

# questions adapted from: http://apps.nacada.ksu.edu/conferences/ProposalsPHP/uploads/handouts/2013/C079-H04.pdf
e_and_i_question_list = ["1. When you are with a group of people, would you usually rather... \na. Join in the talk of the group\nb. Talk individually with people you know well",
                         "2. When you have to meet strangers, do you find it... \na. Pleasant, or at least easy \nb. Something that takes a good deal of effort",
                         "3. Are you... \na. Easy to get to know \nb. Hard to get to know",
                         "4. Do you tend to have... \na. Broad friendships with many different people \nb. Deep friendships with very few people",
                         "5. At parties, do you... \na. Always have fun \nb. Sometimes get bored"]
s_and_n_question_list = ["6. Do you usually get along better with... \na. Realistic people \nb. Imaginative people",
                         "7. If you were a teacher, would you rather teach... \na. Fact courses\nb. Courses involving theory",
                         "8. Is it higher praise to you to say someone has... \na. Common sense \nb. Vision",
                         "9. Would you rather have a friend who... \na. Has ''both feet on the ground'' and is very practical \nb. Is always coming up with new ideas",
                         "10. Would you rather be considered... \na. A practical person \nb. An ingenious person"]
t_and_f_question_list = ["11. Which word appeals to you more? \na. Analyze \nb. Sympathize",
                         "12. Which word appeals to you more? \na Foresight \nb. Compassion",
                         "13. Which word in the pair appeals to you more? \na. Firm \nb. Gentle",
                         "14. Which word in the pair appeals to you more? \na. Thinking \nb. Feeling",
                         "15. Is it a higher compliment to you to be called... \na. A consistently reasonable person \nb. A person of real feeling"]
j_and_p_question_list = ["16. Does following a schedule \na. Appeal to you \nb. Make you feel restricted",
                         "17. Do you prefer to... \na. Arrange dates, parties, etc. well in advance \nb. Be free to do whatever seems appealing when the time comes",
                         "18. Does the idea of making a list of what you should get done over a weekend... \na. Appeal to you \nb. Seem confining",
                         "19. When it is settled well in advance that you will do a certain thing at a certain time, do you find it... \na. Nice to be able to plan accordingly \nb. Unpleasant to be tied down to the commitment",
                         "20. Is it harder for you to adapt to... \na. Constant change \nb. Routine"]

while start == False:
    quiz = False
    (initialize) = input ("Would you like to start the quiz? y/n")
    if str.lower(initialize) == "y":
        print ("Starting quiz....")
        time.sleep(.5)
        print("...")
        time.sleep(.5)
        print("..")
        time.sleep(.5)
        print(".")
        instructions = True
        start = True
    elif str.lower(initialize) == "n":
        quit("Quitting program. Have a nice day.")
    else:
        print("Response unrecognized, please try again.")
while instructions == True:
    print ("Instructions: This quiz has 20 questions with two options each that will determine your MBTI personality type. \n"
           "Read each question, and input the letter that matches what you feel most resonates with you. After these questions \n"
           "your result will be posted.")
    quiz = True
    instructions = False
counter1 = 0
counter2 = 0
counter3 = 0
counter4 = 0
while quiz == True:
    for i in e_and_i_question_list:
        x = input(e_and_i_question_list[counter1])
        if x == "a":
            extrovert_value += 1
            counter1 += 1
        elif x == "b":
            introvert_value += 1
            counter1 += 1
        else:
            print("Answer unrecognized. Please try again.")
        while counter1 == 4:
            break
    for i in s_and_n_question_list:
        x = input(s_and_n_question_list[counter2])
        if x == "a":
            sensing_value += 1
            counter2 += 1
        elif x == "b":
            intuitive_value += 1
            counter2 += 1
        else:
            print("Answer unrecognized. Please try again.")
        while counter2 == 4:
            break
    for i in t_and_f_question_list:
        x = input(t_and_f_question_list[counter3])
        if x == "a":
            thinking_value += 1
            counter3 += 1
        elif x == "b":
            feeling_value += 1
            counter3 += 1
        else:
            print("Answer unrecognized. Please try again.")
        while counter3 == 4:
            break
    for i in j_and_p_question_list:
        x = input(j_and_p_question_list[counter4])
        if x == "a":
            judging_value += 1
            counter4 += 1
        elif x == "b":
            perceiving_value += 1
            counter4 += 1
        else:
            print("Answer unrecognized. Please try again.")
        while counter4 == 4:
            quiz = False
            end_quiz = True
            break
while end_quiz == True:
    if extrovert_value > introvert_value:
        e_i_value = "E"
    else:
        e_i_value = "I"
    if sensing_value > intuitive_value:
        s_i_value = "S"
    else:
        s_i_value = "N"
    if thinking_value > feeling_value:
        t_f_value = "T"
    else:
        t_f_value = "F"
    if judging_value > perceiving_value:
        j_p_value = "J"
    else:
        j_p_value = "P"
    print("Calculating scores...")
    time.sleep(.5)
    print ("Your MBTI is " + e_i_value,s_i_value,t_f_value,j_p_value)
    quit("Thank you for taking the quiz! (Special thanks to Mohammad, Satiya, Ms. Bolin, and everyone else in AP Comp Sci Principles - thanks for explaining it all!) Have a nice day!")
    # The code below needs to be fixed - I want to restart the program.

    #restart_input = input("Would you like to take the quiz again? y/n")
    #if (restart_input) == "y":
        #restart_quiz = True
        #break
    #if (restart_input) == "n":
        #quit("Thank you for taking the quiz! (Special thanks to Mohammad, Satiya, Ms. Bolin, and everyone else in AP Comp Sci Principles - thanks for explaining it all!) Have a nice day.")
#while restart_quiz == True:
    #instructions = False
    #start = False
    #quiz = False
    #end_quiz = False
    #restart_quiz = False