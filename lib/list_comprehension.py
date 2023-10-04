#!/usr/bin/env python3

def return_evens(num_list):
    even_numbers = [num for num in num_list if num % 2 == 0]
    return even_numbers


def make_exclamation(sentence_list):
    exclamated_sentences = [sentence + '!' for sentence in sentence_list]
    return exclamated_sentences