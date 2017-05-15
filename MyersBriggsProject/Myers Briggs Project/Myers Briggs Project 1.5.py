import sys #Perhaps unneeded but unsure at current refracting stage
import time #Used for time.sleep

print("''The purpose of the Myers-Briggs Type Indicator® (MBTI®) personality inventory is to make the theory of psychological types described by C. G. Jung understandable and useful in people's \nlives. The essence of the theory is that much seemingly random variation in the behavior is actually quite orderly and consistent, \nbeing due to basic differences in the ways individuals prefer to use their perception and judgment.'' ~ meyersbriggs.org")
# Source for text: http://www.myersbriggs.org/my-mbti-personality-type/mbti-basics/home.htm?bhcp=1
print( )

instructions = 0
start = 0
quiz = 0
extrovert_value = 0
introvert_value = 0
sensing_value = 0
intuitive_value = 0
thinking_value = 0
feeling_value = 0
judging_value = 0
perceiving_value = 0

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

while start != 1:
    quiz == 0
    (initialize) = input ("Would you like to start the quiz? y/n")
    if str.lower(initialize) == "y":
        print ("Starting quiz....")
        time.sleep(1)
        print("...")
        time.sleep(1)
        print("..")
        time.sleep(1)
        print(".")
        instructions == 1
    elif str.lower(initialize) == "n":
        quit("Quitting program. Have a nice day.")
    else:
        print("Response unrecognized, please try again.")
while instructions == 1:
    print ("Instructions: This quiz has 20 questions with two options each that will determine your MBTI personality type. \n"
           "Read each question, and input the letter that matches what you feel most resonates with you. After these questions \n"
           "your result will be posted.")
    quiz == 1           # This is broken, fix!
    break

while quiz == 1:
    for i in e_and_i_question_list:
        input(i)
        if input(i) == "a":
            extrovert_value += 1
        else:
            introvert_value += 1

