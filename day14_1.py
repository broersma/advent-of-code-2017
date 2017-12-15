def get_hash(str):
    numbers = list(range(256))
    position = 0
    skip = 0
    lengths = [ord(x) for x in str] + [17, 31, 73, 47, 23]

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

    return ''.join(["%02x" % number for number in dense_hash])

count = 0
for row in range(128):
    input = "amgozmfv-" + str(row)
    binary_string = ''.join("{0:04b}".format(int(h,16)) for h in get_hash(input))
    count += binary_string.count('1')

print(count)
