#!/usr/bin/python3
def multiple_returns(sentence):
    longitud = len(sentence)
    return longitud, sentence[0] if longitud > 0 else None
