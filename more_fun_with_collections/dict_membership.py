def in_dict(element, my_dict):
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
