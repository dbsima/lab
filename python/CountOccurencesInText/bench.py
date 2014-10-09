import sys

sys.path.append('.');

import timeit
me = timeit.timeit("mini_doit(NumberOfOccurencesOfWordInText=CountOccurencesInText)",setup="from how_we_bench import mini_doit; from ggnumber_v5 import CountOccurencesInText",number=1)
print me
