"""
http://en.wikipedia.org/wiki/Impossible_Puzzle
"""
limit = 100
#before they talk any x*y where 1<x<y<x+y<limit is allowed as P
PAllowed1 = {}
for x in range(2, limit):
   for y in range(x+1, limit-x):
       if x*y not in PAllowed1:
           PAllowed1[x*y] = 1
       else:
           PAllowed1[x*y] += 1
# when P says I don't know, only P's with PAllowed1[P]>1 are allowed
SNotAllowed1 = {}
for x in range(2, limit):
   for y in range(x+1, limit-x):
       if  PAllowed1[x*y] == 1 :
           SNotAllowed1[x+y] = 1
# when S says I don't know, only S's that are not in the domain of SNotAllowed1 are allowed
PAllowed2 = {}
for n in range(2, limit):
 if n not in SNotAllowed1:
   for x in range(2, n//2+1):
       p = x * (n-x)
       if p in PAllowed1 and PAllowed1[p] > 1:
           if p in PAllowed2:
               PAllowed2[p] += 1
           else:
               PAllowed2[p] = 1
# only the P's that can by split to two x,y where x+y is allowed in only 1 way are allowed, i.e., PAllowed2[P]==1
SAllowed2 = {}
for n in range(2, limit):
 if n not in SNotAllowed1:
   for x in range(2, n//2+1):
       if x*(n-x) in PAllowed2 and PAllowed2[x*(n-x)] == 1:
           if n in SAllowed2:
               SAllowed2[n] += 1
           else:
               SAllowed2[n] = 1
# since S knows the answer now the split can only be done in one way, so only S where SAllowed2[S]==1
for n in SAllowed2:
   if SAllowed2[n] == 1:
       for x in range(2, n//2+1):
           if x*(n-x) in PAllowed2 and PAllowed2[x*(n-x)] == 1:
              print '(S,P) = ( %d , %d ), (x,y)= ( %d , %d )' % (n, x*(n-x), x, n-x)
