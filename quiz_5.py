'''
You are a taxi driver for Kakao Taxi Service.
If there is a matching chance with 20 passengers,
Make a program that calculates passengers with a status.

Rule # 1 : For operation time, a random number will be selected between 5 mins ~ 50 mins
Rule # 2 : You have to be matched with passengers that would need 5 mins - 15 mins of operation time

Example:
[O] 1st passenger (Operation Time : 15 mins)
[ ] 2nd passenger (Operation Time : 50 mins)
[O] 3rd passenger (Operation Time : 5 mins)
...
[ ] 20th passenger (Operation Time : 16 mins)

A total number of passenger : 2 
'''
from random import *
