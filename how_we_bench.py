#!/usr/bin/python
# -*- coding: UTF-8 -*-

SampleTextForBench = """
A Suggestion Box Entry from Bob Carter

Dear Anonymous,

I'm not quite sure I understand the concept of this 'Anonymous' Suggestion Box. If no one reads what we write, then how will anything ever
change?

But in the spirit of good will, I've decided to offer my two cents, and hopefully Kevin won't steal it! (ha, ha). I would really like to
see more varieties of coffee in the coffee machine in the break room. 'Milk and sugar', 'black with sugar', 'extra sugar' and 'cream and su
gar' don't offer much diversity. Also, the selection of drinks seems heavily weighted in favor of 'sugar'. What if we don't want any suga
r?

But all this is beside the point because I quite like sugar, to be honest. In fact, that's my second suggestion: more sugar in the office.
Cakes, candy, insulin, aspartame... I'm not picky. I'll take it by mouth or inject it intravenously, if I have to.

Also, if someone could please fix the lock on the men's room stall, that would be helpful. Yesterday I was doing my business when Icarus ne
arly climbed into my lap.

So, have a great day!

Anonymously,
 Bob Carter
"""

    
    
def mini_doit(NumberOfOccurencesOfWordInText, nb_runs=10):
    """Run NumberOfOccurencesOfWordInText on a few examples nb_runs times

    Expected result: 2000 for 1 run
    """
    i = 0
    for x in range(400*nb_runs):
        i+= NumberOfOccurencesOfWordInText("word" , SampleTextForBench)
        i+= NumberOfOccurencesOfWordInText("sugar" , SampleTextForBench)
        i+= NumberOfOccurencesOfWordInText("help" , SampleTextForBench)
        i+= NumberOfOccurencesOfWordInText("heavily" , SampleTextForBench)
        i+= NumberOfOccurencesOfWordInText("witfull" , SampleTextForBench)
        i+= NumberOfOccurencesOfWordInText("dog" , SampleTextForBench)
        i+= NumberOfOccurencesOfWordInText("almost" , SampleTextForBench)
        i+= NumberOfOccurencesOfWordInText("insulin" , SampleTextForBench)
        i+= NumberOfOccurencesOfWordInText("attaching" , SampleTextForBench)
        i+= NumberOfOccurencesOfWordInText("asma" , SampleTextForBench)
        i+= NumberOfOccurencesOfWordInText("neither" , SampleTextForBench)
        i+= NumberOfOccurencesOfWordInText("won't" , SampleTextForBench)
        i+= NumberOfOccurencesOfWordInText("green" , SampleTextForBench)
        i+= NumberOfOccurencesOfWordInText("parabole" , SampleTextForBench)
    return i # Should be 2000
 
