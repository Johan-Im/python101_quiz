'''
There is a popular fried chicken place in a town.
To try to reduce some waiting time, we would like to make a 
program that automates order system. 
Check the System code and enter the appropriate 'except' function. 

Rule 1: if 1 > or not a number, enter ValueError saying
"Wrong Input"

Rule 2: Waiting Customer can order up to 10 fried chicken
        when no more chickens, use error defined by user [SoldOutError], and
        terminate the program saying "No more orders due to no more chickens"
'''

class SoldOutError(Exception):
    pass
  
chicken = 10
waiting = 1 
