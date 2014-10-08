class KMP(object):
    def __init__(self, needle):
        self.needle = needle
        self.table = [1] * (len(needle) + 1)
        shift = 1
        for index, obj in enumerate(needle):
            while shift <= index and obj != needle[index - shift]:
                shift += self.table[index - shift]
            self.table[index + 1] = shift
 
    def __repr__(self):
        return 'KMP(%r)' % needle
 
    def search_in(self, haystack):
        index = 0
        match = 0
	count = 0
        while index + match < len(haystack):
            if self.needle[match] == haystack[index + match]:
                match += 1
                if match == len(self.needle): return True
            else:
                if match == 0: index += 1
                else:
                    index += match - self.table[match]
	return False
 
 
## run tests
if __name__ == '__main__':
	needle = 'seven years ago'.split()
	haystack = 'four score and seven years ago our fathers'.split()
	print KMP(needle).search_in(haystack)
