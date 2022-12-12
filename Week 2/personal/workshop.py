# import module directly 
import constants

# import variables from constant
from constants import CURRENT_STUDENT_COUNT

# Dont use '*' while importing 

print(f'There are currently {constants.CURRENT_MENTOR_COUNT} number of mentors')

print('There are currently',  constants.CURRENT_MENTOR_COUNT, 'number of mentors')
print('There are currently ' + str(CURRENT_STUDENT_COUNT) + ' number of students')