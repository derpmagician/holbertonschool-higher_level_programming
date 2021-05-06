#!/usr/bin/python3
def best_score(a_dictionary):
    if a_dictionary is None:
        return None

    new_score = max(a_dictionary.values(), default=None)
    for key, value in a_dictionary.items():
        if value == new_score:
            return key
