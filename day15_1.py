def generator_generator(factor):
    def generator(value):
        while True:
            value *= factor
            value %= 2147483647
            yield value
    return generator

generator_a = generator_generator(16807)
generator_b = generator_generator(48271)

def match(value_a, value_b):
    return value_a & 0b1111111111111111 == value_b & 0b1111111111111111

from itertools import islice

count = 0
matches = (match(a,b) for a,b in islice(zip(generator_a(289), generator_b(629)), 40000000))
print(list(matches).count(True))