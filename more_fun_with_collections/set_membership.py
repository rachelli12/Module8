"""
Program name: set_membership.py
Author: Rachel Li
Last date modified: 06/26/2020

The purpose of this program is to accept a set
and return boolean value if element is in set.
"""
def in_set(element, my_set):
    '''
    :param element: this represents item in set
    :param my_set: this represents set
    :return: return boolean value if element is in set
    '''
    #accept set
    my_set = {34, 25, 67, 98, 3, 5}
    #return boolean value stating if element is in the set
    return element in my_set

if __name__ == '__main__':
    check_set = (34, (34, 25, 67, 98, 3, 5))
    print(check_set)
