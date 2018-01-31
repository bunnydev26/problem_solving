"""
Usecase of permutations
Given a word apple
See if it can be arranged as elpap
"""
import itertools
def main():
    word = "apple"
    match_word = "elpap"

    combinations = itertools.combinations(word, len(match_word))
    permutations = itertools.permutations(word, len(match_word))

    for result in permutations:
        match_word_candidate = "".join(result)

        if match_word == match_word_candidate:
            print("Match found")
            break
    else:
        print("No match found")



if __name__ == '__main__':
    main()

