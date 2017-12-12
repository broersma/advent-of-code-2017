state = [int(blocks) for blocks in "0	5	10	0	11	14	13	4	11	8	8	7	1	4	12	11".split()]

states = []
cycle = 0

while state not in states:
    states.append(state)
    index = state.index(max(state))
    num_blocks = state[index]
    state = state[:]
    state[index] = 0
    for i in range(num_blocks):
        index = (index + 1) % len(state)
        state[index] += 1
    cycle +=1

print(cycle - states.index(state))