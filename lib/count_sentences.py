#!/usr/bin/env python3

import ipdb

class MyString:
    
    def __init__(self, value = ""):
        self.value = value

    @property
    def value(self):
        return self._value
    
    @value.setter
    def value(self, value):
        if isinstance(value, str):
            self._value = value
        else:
            print("The value must be a string.")

    def is_sentence(self):
        return self._value[-1] == "."
    
    def is_question(self):
        return self._value[-1] == "?"
    
    def is_exclamation(self):
        return self._value[-1] == "!"
    
    def count_sentences(self):
        number_of_sentences = []
        pwd = self._value
        pwd = pwd.replace(" ", "")
        pwd = pwd.replace("!!", "!")
        pwd = pwd.replace("...", ".")
        
        for char in pwd:
            if char in (".", "!", "?", "...", "!!"):
                a = pwd[0 : pwd.index(char) + 1]
                pwd = pwd.replace(a,"")
                number_of_sentences.append(a)
        return len(number_of_sentences)