"""
The purpose of this program is to calculate half birthday
"""
import datetime
from datetime import timedelta

#latest birthday

def half_birthday(birthdate):
    '''
    :param birthdate: this represents birthdate
    :param half_birthdate: this represents calculated half birthday
    :return: returns calculated half birthday
    '''
    birthdate_strp = datetime.datetime.strptime(birthdate, '%Y-%m-%d')
    #use timedelta
    half_birthdate = birthdate_strp + timedelta(days = 183)
    #returns the half birthday
    return f'{half_birthdate:%Y-%m-%d}'

if __name__ == '__main__':
    print(half_birthday('2020-09-24'))
