"""
This is an example of a combination usecase
Where in a given list of number [1,2,3,4,5,6]
In how many ways three numbers can be arranged
that the sum be 10
"""
import itertools

def main():
    my_list = [1,2,3,4,5,6]

    combinations = itertools.combinations(my_list, 3)

    result_list = [result for result in combinations if sum(result) == 10]

    for result in result_list:
        print(result)

    return

if __name__ == '__main__':
    main()
