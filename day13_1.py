input = """0: 3
1: 2
2: 6
4: 4
6: 4
8: 10
10: 6
12: 8
14: 5
16: 6
18: 8
20: 8
22: 12
24: 6
26: 9
28: 8
30: 8
32: 10
34: 12
36: 12
38: 8
40: 12
42: 12
44: 14
46: 12
48: 12
50: 12
52: 12
54: 14
56: 14
58: 14
60: 12
62: 14
64: 14
66: 17
68: 14
72: 18
74: 14
76: 20
78: 14
82: 18
86: 14
90: 18
92: 14""".split("\n")

depth_ranges = {}

for line in input:
    depth, range = line.split(": ")
    depth_ranges[int(depth)] = int(range)

severity = 0
for depth, range in depth_ranges.items():
    if depth % ((range-1) * 2) == 0:
        severity += depth * range
        
print(severity)