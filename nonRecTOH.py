def tohSteps(n):
    _steps = [-1 for i in range(2**n-1)]
    for disk in range(n):
        iPos = 2**disk - 1
        _steps[iPos] = str(disk)+initStep(n, disk)
        diff = posdiff(disk)
        for step in range(iPos+diff, len(_steps), diff):
            _steps[step] = str(disk)+nextStep(_steps[iPos][1::], _steps[step-diff][1::])
    return tuple(_steps)

def initStep(n, k):
    return 'AC' if (n+k)&1 else 'AB'

def posdiff(k):
    return 2**(k+1)

def nextStep(initStep, preStep):
    stacks = ('A', 'B', 'C') if initStep[1] == 'B' else ('A', 'C', 'B')
    last = preStep[-1]
    return initStep if last==initStep[0] else f"{last}{stacks[(stacks.index(last)+1)%3]}"


def simulToh(numOfDisks: int) -> tuple:
    towers = dict()
    towers['A'] = list(disk for disk in range(numOfDisks))
    towers['B'], towers['C'] = [], []
    print(towers)
    StepList = tohSteps(numOfDisks)
    for step in range(len(StepList)):
        towers[StepList[step][2]].insert(0, towers[StepList[step][1]].pop(0))
        print(f'{step+1}: ({StepList[step][0]}) {StepList[step][1]} -> {StepList[step][2]} {towers}')


print('function: tohSteps(number of disks) to print out the steps; simulToh(number of disks) to print out the simulation')
