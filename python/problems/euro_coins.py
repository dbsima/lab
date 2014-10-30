"""
There are 8 type of coins - 1c, 2c, 5c, 10c, 20c, 50c, 1 euro (100c), 2 euros
(200c) each in a infinite number.

In how many ways can you combine the coins to add up to 2 euros?
    1*2 euro
    1*1 euro + 1*50c + 2*20c + 1*5c + 1*2c + 3*1c
"""


count = 0
total = 200
for a in range(total, -1, -200):
    for b in range(a, -1, -100):
        for c in range(b, -1, -50):
            for d in range(c, -1, -20):
                for e in range(d, -1, -10):
                    for f in range(e, -1, -5):
                        for g in range(f, -1, -2):
                               count += 1
