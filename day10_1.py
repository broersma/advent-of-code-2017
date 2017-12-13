numbers = list(range(256))
position = 0
skip = 0
lengths = [int(x) for x in "165,1,255,31,87,52,24,113,0,91,148,254,158,2,73,153".split(",")]

for length in lengths:
    numbers = numbers[position:] + numbers[:position]
    numbers[:length] = numbers[:length][::-1]
    numbers = numbers[-position:] + numbers[:-position]
    position = (position + length + skip) % len(numbers)
    skip += 1
  
print(numbers[0] * numbers[1])