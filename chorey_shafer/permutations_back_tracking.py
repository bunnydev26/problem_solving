"""
Permutation where the order the way the elements are arranged matters
Using a back tracking we print all the permutations
E.g.
abc
There are total 3! permutations
abc
acb
acb
bac
bca
cab
cba
"""

def calculate_permutations(element_list, pos, r=None):
    n = len(element_list)
    if pos == n:
        if r:
            print(element_list[:r])
        else:
            print(element_list)
        return

    index = pos
    while pos < n:
        element_list[pos], element_list[index] = element_list[index], element_list[pos]
        calculate_permutations(element_list, index+1, r)
        # back tracking the element in the list
        element_list[pos], element_list[index] = element_list[index], element_list[pos]
        pos += 1


def permutations(element_list, r=None):
    calculate_permutations(list(element_list), 0)

def main():
    permutations("abc", 2)

if __name__ == '__main__':
    main()