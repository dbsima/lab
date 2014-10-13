#!/usr/bin/python
# -*- coding: UTF-8 -*-

import string

def has_unique_characters(string):
    """Determine if a string with only lower case letters has all unique 
    characters"""

    try:
        n = string.__len__()
    except AttributeError:
        print "You should insert a valid string!"
    else:
        if n == 0: return False
        
        checker = 0
        ord_a = ord('a')
        for character in string:
            val = ord(character) - ord_a
            if (checker & (1 << val) > 0):
                return False
            checker |= (1 << val)
        return True


def test():
    assert( True == has_unique_characters("abcde") )
    assert( True == has_unique_characters("a") )
    assert( False == has_unique_characters("aa") )
    assert( False == has_unique_characters("aba") )
    assert( False == has_unique_characters("") )
    assert( None == has_unique_characters(1) )
    
    
if __name__ == '__main__':
    try:
        test()
    except:
        print "Error !"
        raise
    print "Tests passed"