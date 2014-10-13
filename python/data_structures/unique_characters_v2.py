#!/usr/bin/python
# -*- coding: UTF-8 -*-

import string

def has_unique_characters(string):
    """Determine if a string has all unique characters"""

    try:
        n = string.__len__()
    except AttributeError:
        print "You should insert a valid string!"
    else:
        if n > 256 or n == 0: return False
        
        unique_characters = {}
        for character in string:
            if ord(character) in unique_characters:
                return False
            unique_characters[ord(character)] = True
        return True


def test():
    assert( True == has_unique_characters("Abcde") )
    assert( True == has_unique_characters("a") )
    assert( False == has_unique_characters("aa") )
    assert( False == has_unique_characters("aba") )
    assert( False == has_unique_characters("") )
    assert( False == has_unique_characters("«Reflexion Mirror»") )
    assert( None == has_unique_characters(1) )
    
     
if __name__ == '__main__':
    try:
        test()
    except:
        print "Error !"
        raise
    print "Tests passed"