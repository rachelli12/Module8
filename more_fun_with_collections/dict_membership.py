"""
Program name: dict_membership.py
Author name: Rachel Li
Last date modified: 06/25/2020

The purpose of this program is to accept a set
and return boolean value if element in set.
"""
def in_dict(element, my_dict):
    '''
    use reST style
    :param element: this represents the item searched
    :param my_dict: this repesents the dictionary set
    :return:  this returns boolean value if item is in set
    '''
    #accept a set
    my_dict = {'A': 'apple', 'B': 'banana', 'C': 'cantaloupe', 'D': 'dragonfruit'}
    #return boolean value if the element is in the set
    if 'A' in my_dict:
        print('True')
    else:
        print('False')
    return element in my_dict

if __name__ == '__main__':
    in_dict('A', {'A': 'apple', 'B': 'banana', 'C': 'cantaloupe', 'D': 'dragonfruit'})
