numbers = list(range(256))
position = 0
skip = 0
lengths = [ord(x) for x in "165,1,255,31,87,52,24,113,0,91,148,254,158,2,73,153"] + [17, 31, 73, 47, 23]

for round in range(64):
    for length in lengths:
        numbers = numbers[position:] + numbers[:position]
        numbers[:length] = numbers[:length][::-1]
        numbers = numbers[-position:] + numbers[:-position]
        position = (position + length + skip) % len(numbers)
        skip += 1

dense_hash = []
from functools import reduce
for i in range(16):
    dense_hash.append(reduce(lambda x,y: x^y, numbers[16*i:16*i+16]))

print(''.join(["%02x" % number for number in dense_hash]))
