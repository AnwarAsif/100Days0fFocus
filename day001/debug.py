# ############DEBUGGING#####################
#
# # Describe Problem
# def my_function():
#   for i in range(1, 21):
#     if i == 20:
#       print("You got it")
# my_function()
#
# '''objective of the above code is to print "You got it". The print command is expected to happen when the vlaue
# of i is 20. from the range command the probable values of i are 1 to 19, hence its never reaching to 20'''
#
# # Reproduce the Bug
# from random import randint
# dice_imgs = ["❶", "❷", "❸", "❹", "❺", "❻"]
# # dice_num = randint(6, 6)
# dice_num = randint(0, 5)
# print(dice_imgs[dice_num])
#
# '''To reproduce the error, first lets have a look at problem. prblem here is picking up a random dice from list.
# now lets look at the error. Error says list index out of range. that mean it taking the value 6 which in not a list value.
# To reproduce the error we can change th range for random from 6 to 6'''
#
# # Play Computer
# year = int(input("What's your year of birth?"))
# if year > 1980 and year <= 1994:
#   print("You are a millenial.")
# elif year > 1994:
#   print("You are a Gen Z.")
#
# # Fix the Errors
# age = int(input("How old are you?"))
# if age > 18:
#   print(f"You can drive at age {age}.")
#
# #Print is Your Friend
# pages = 0
# word_per_page = 0
# pages = int(input("Number of pages: "))
# print(pages)
# word_per_page = int(input("Number of words per page: "))
# print(word_per_page)
# total_words = pages * word_per_page
# print(total_words)

#Use a Debugger
def mutate(a_list):
  b_list = []
  for item in a_list:
    new_item = item * 2
    b_list.append(new_item)
  print(b_list)

mutate([1,2,3,5,8,13])