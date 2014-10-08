import string
separators = string.whitespace + ",.?!\"_():" 

def knuth_morris_pratt_shift(p):
    m = len(p)
    shift = [1 for k in xrange(m)]
    i=1
    j=0
    while(i+j<m):
        if(p[i+j]==p[j]):
            shift[i+j] = i
            j=j+1
        elif(j==0):
            shift[i] = i+1
        i = i+shift[j-1]
        j = max(j-shift[j-1], 0)
    return shift
            
def knuth_morris_pratt_search(p, t):
    m = len(p)
    n = len(t)
    shift = knuth_morris_pratt_shift(p)
    i=0
    j=0
    while(i+m<=n):
        while(t[i+j]==p[j]):
            j=j+1
            if(j>=m): 
                return i

        i = i+shift[j-1]
        j = max(j-shift[j-1],0)
    return -1



def KnuthMorrisPratt(text, pattern):
 
    '''Yields all starting positions of copies of the pattern in the text.
Calling conventions are similar to string.find, but its arguments can be
lists or iterators, not just strings, it returns all matches, not just
the first one, and it does not need the whole text in memory at once.
Whenever it yields, it will have read the text exactly up to and including
the match that caused the yield.'''
 
    # allow indexing into pattern and protect against change during yield
    text = text.lower()
    pattern = pattern.lower()
    
    pattern = list(pattern)
    print pattern
 
    m = len(pattern)
    n = len(text)
    
    # build table of shift amounts
    shifts = [1] * (m + 1)
    shift = 1
    for pos in range(m):
        while shift <= pos and pattern[pos] != pattern[pos-shift]:
            shift += shifts[pos-shift]
        shifts[pos+1] = shift
 
    # do the actual search
    startPos = 0
    matchLen = 0
    count = 0
    for c in text:
        while matchLen == m or \
              matchLen >= 0 and pattern[matchLen] != c:
            startPos += shifts[matchLen]
            matchLen -= shifts[matchLen]
        matchLen += 1
        if matchLen == m:
            if startPos > 0:
                begin = text[startPos - 1]
            else:
                begin = "!"
            if startPos + m + 1 < n:
                end = text[startPos + m]
            else:
                end = "!"
            #print begin + " - " + end
            if (end in separators and begin in separators):
                #print begin + " - " + end
                count += 1
    return count
            
text="""I am a senior citizen and I live in the Fun-Plex 'Reflexion Mirror' in Sopchoppy, Florida"""
pattern = "'reflexion mirror'"


print knuth_morris_pratt_search(pattern, text)
