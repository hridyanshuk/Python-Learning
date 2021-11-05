courses=['CS201', 'CS221', 'CS203', 'CS204', 'CS242']

"""Importing a module in the same directory"""

#import testModule
#index=testModule.findIndex('CS204', courses)
#print(index)
#index=testModule.findIndex('MA222', courses)
#print(index)


"""Importing a module and giving it an alias instead of using the entire name"""

#import testModule as test
#index=test.findIndex("CS242", courses)
#print(index)
#index=test.findIndex("MA225", courses)
#print(index)

"""Importing just some functions from a module"""

#from testModule import findIndex as FIND, printNo as NO
#index=FIND('MA222', courses)
#if index == 'Not Found':
#    NO
#else:
#    print(index)

"""Where does python check for modules"""

#import sys
#sys.path.append(path)
#print(sys.path)
#Python checks for the modules in the paths in the list sys.path

#If the module exists in a path which does not exist in sys.path list, you can add its
#path to the list - sys.path.

"""Some modules from Standard library"""

import random
var=random.choice(courses)
print('A random element from \'courses\' is {}'.format(var))

import math
rad=math.radians(90)
print('90 degree in radians is {}'.format(rad))
sine=math.sin(rad)
print('sine of 90 degrees is {}'.format(sine))

import datetime
import calendar
todayDate=datetime.date.today()
print('Today\'s date is {}'.format(todayDate))
print('Is 2020 a leap year?')
print(calendar.isleap(2020))

import os
print(os.getcwd()) #Prints current directory
print(os.__file__) #Prints where the os.py file exists