#!/usr/bin/env python3

import re

class MyString:
    
    def __init__(self, value = ''):
        self.value = value

    def get_value(self):
        return self._value
    
    def set_value(self, value):
        if(type(value) is str):
            self._value = value
        else:
            print("The value must be a string.")

    value = property(get_value, set_value)

    def is_sentence(self):
        return (len(self.value) > 0 and self.value[-1] == '.')
    
    def is_question(self):
        return (len(self.value) > 0 and self.value[-1] == '?')
    
    def is_exclamation(self):
        return (len(self.value) > 0 and self.value[-1] == '!')
    
    def count_sentences(self):
        sentences = re.split('[!?.]+', self.value)
        
        for sentence in sentences:
            if(sentence == ""):
                sentences.remove(sentence)

        return len(sentences)