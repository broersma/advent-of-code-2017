def generator_generator(factor, divides_by):
    def generator(value):
        while True:
            value *= factor
            value %= 2147483647
            if value % divides_by == 0:
                yield value
    return generator

generator_a = generator_generator(16807, 4)
generator_b = generator_generator(48271, 8)

def match(value_a, value_b):
    return value_a & 0b1111111111111111 == value_b & 0b1111111111111111

from itertools import islice

count = 0
matches = (match(a,b) for a,b in islice(zip(generator_a(289), generator_b(629)), 5000000))
print(list(matches).count(True))