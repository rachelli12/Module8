"""
Program name: assign_average.py
Author: Rachel Li
Last date modified: 06/28/2020

The purpose of this program is to
assign a grade to average scores
and print GPA based on average score.
"""

def grade(average_score):
    '''
    use reST style

    :param average_score: this represents the average
    :return: this returns the average
    '''
    returned_score = 0.0

def one():
    return 'A'

def two():
    return 'B'

def three():
    return 'C'

def four():
    return 'D'

def default():
    return 'F'

def switch_average(score1, score2, score3):
    '''
    use reST style

    :param score1: this represents user input score1
    :param score2: this represents user input score2
    :param score3: this represents user input score3
    :param average_score: this represents the average of the test scores
    :return: returns the average_score
    :keyError: raise ValueError
    '''
    total = 0.0
    average_score = int(score1 + score2 + score3) / 3
    if 90 <= average_score <= 100:
        return one()
    elif 80 <= average_score < 90:
        return two()
    elif 70 <= average_score < 80:
        return three()
    elif 50 < average_score < 70:
        return four()
    elif average_score <= 50:
        return default()
    else:
        raise ValueError
    #return score = ??
    #make similar function wise to a switch statement
    #useing a dictionary and if, elif, else

def switch_gpa(grades):
    '''
    use reST style

    :param grades: this represents the average grade
    :return: returns the GPA based on the grade
    '''
    score_dict = {
    one(): 4.0,
    two(): 3.0,
    three(): 2.0,
    four(): 1.0,
    default(): 0.0
    }
    grade_func = score_dict.get(grades, 'default')
    return grade_func


if __name__ == '__main__':
    score1 = int(input("Enter score1: "))
    score2 = int(input("Enter score2: "))
    score3 = int(input("Enter score3: "))
    average_score = switch_average(score1, score2, score3)
    print(switch_gpa(average_score))
    print(average_score)
    grade(average_score)
