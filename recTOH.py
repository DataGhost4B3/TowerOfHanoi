def recTH(stacks: dict, a, b, c, t, l, sim, simList):
    if t==1:
        peek_a = stacks[a].pop(0)
        stacks[c].insert(0, peek_a)
        l.append(f'{peek_a}{a}{c}')
        if sim:
            simList.append(f'{len(simList)+1}: ({peek_a}) {a} -> {c} : {stacks}')
        return
    recTH(stacks, a, c, b, t-1, l, sim, simList)
    recTH(stacks, a, b, c, 1, l, sim, simList)
    recTH(stacks, b, a, c, t-1, l, sim, simList)


def rt(n, sim=False):
    towers = {'A': [i for i in range(n)],'B': [],'C': []}
    steps, simL = [], []
    recTH(towers, 'A', 'B', 'C', n, steps, sim, simL)
    if sim:
        return steps, simL
    return steps


print('function: rt(n:= number of disks, simulate? := True (False by default))')
print('X (, Y if simulate is True) = rt(n(,sim))')
print('function: printSim(Y) if simulate is True for printing the simulation')

def printSim(n):
    t,s=rt(n, True)
    for step in s:
        print(step)
