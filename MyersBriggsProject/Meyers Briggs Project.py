import sys

print("''The purpose of the Myers-Briggs Type Indicator® (MBTI®) personality inventory is to make the theory of psychological types described by C. G. Jung understandable and useful in people's \nlives. The essence of the theory is that much seemingly random variation in the behavior is actually quite orderly and consistent, \nbeing due to basic differences in the ways individuals prefer to use their perception and judgment.'' ~ meyersbriggs.org")
# Source for text: http://www.myersbriggs.org/my-mbti-personality-type/mbti-basics/home.htm?bhcp=1
print( )
start = 0
while start == 0:
   (initialize) = input ("Would you like to start the quiz? y/n")
   if str.lower(initialize) == "y":
       print ("Starting quiz...")
       break
   elif str.lower(initialize) == "n":
       quit("Quitting program. Have a nice day.")
       break
   else:
       print("Response unrecognized, please try again.")
