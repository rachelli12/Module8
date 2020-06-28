"""

"""
def get_test_scores():
    scores_dict = dict()
    # prompt user to input the number of test score
    try:
        num_score = int(input("How many test scores? "))
        if num_score < 0:
            print('Invalid input')
            raise ValueError
        else:
            for x in range(0, int(num_score)):
                score = int(input('Enter test score: '))
                if score < 0 and score > 100:
                    print("Invalid input")
                    raise ValueError
                else:
                    # if input valid, add to scores_dict
                    # dict.update()
                    scores_dict.update({x : score})
    except ValueError:
        raise ValueError
    return scores_dict

def average_scores(dict_avg):
    #use len() to determine num_scores for calculation
    total = 0
    for score,value in dict_avg.items():
        total += value
    #returns average scores
    return str('Average:' + str(total/len(dict_avg)))

if __name__ == '__main__':
    print(average_scores(get_test_scores()))


