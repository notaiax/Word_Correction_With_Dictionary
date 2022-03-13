#!/usr/bin/env python3
import sys


def is_correct(word, dictionary):

    for dict_word in dictionary:
        if word == dict_word:
            return True

    return False


def correct(word, dictionary):
    for dict_word in dictionary:
        if len(word) == len(dict_word) and check_equal_len(word, dict_word):
            return dict_word
        elif len(word) == (len(dict_word) - 1) and check_diff_len(word, dict_word):
            return dict_word
        elif len(word) == (len(dict_word) + 1) and check_diff_len(dict_word, word):
            return dict_word


def check_equal_len(word, dict_word):
    diff_counter = 0
    i = 0

    for letter in word:
        if letter != dict_word[i]:
            diff_counter += 1
        i += 1

    if diff_counter > 1:
        return False

    return True


def check_diff_len(short_word, long_word):
    diff_counter = 0
    i = 0

    for letter in long_word:
        if i == len(short_word):
            return True
        if letter == short_word[i]:
            i += 1
        else:
            diff_counter += 1

    if diff_counter > 1:
        return False

    return True


def main():
    dictionary = open(sys.argv[1]).readline().split()
    noisy = open(sys.argv[2]).readline().split()
    corrected_file = open(sys.argv[3], 'w')
    editions_file = open(sys.argv[4], 'w')
    corrected = ''
    editions = 0

    for word in noisy:
        if is_correct(word, dictionary):
            corrected += word + " "
        else:
            correct_word = correct(word, dictionary)
            corrected += str(correct_word) + " "
            editions += 1

    print(editions, file=editions_file)
    print(corrected, file=corrected_file)


if __name__ == "__main__":
    main()
