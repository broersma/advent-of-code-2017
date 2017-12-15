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

binary_rows = []
for row in range(128):
    input = "amgozmfv-" + str(row)
    binary_string = ''.join("{0:04b}".format(int(h,16)) for h in get_hash(input))
    binary_rows.append(binary_string)

import networkx as nx
G = nx.Graph()

import itertools
for x, y in itertools.product(range(128), range(128)):
    if binary_rows[x][y] == '1':
        G.add_node((x,y))
        if x > 0 and binary_rows[x-1][y] == '1':
            G.add_edge((x,y), (x-1,y))
        if y > 0 and binary_rows[x][y-1] == '1':
            G.add_edge((x,y), (x,y-1))

print(len(list(nx.connected_components(G))))