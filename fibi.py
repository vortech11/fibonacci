import sys
sys.set_int_max_str_digits(0)

def fibi(end):
    n1:int = 0
    n2:int = 1
    n3:int = 0
    for _ in range(end):
        n3 = n1 + n2
        n1 = n2
        n2 = n3

    return n2

def fibisequence(end, ratio=False, formatdeapth=0):
    sequence = [0, 1]
    ratios = []
    for i in range(end):
        sequence.append(sequence[-1] + sequence[-2])
        if ratio:
            if formatdeapth > 0:
                frac = sequence[-2] / sequence[-1]
            else:
                frac = f"{sequence[-2]}/{sequence[-1]}"
            ratios.append(frac)
    if ratio:
        return ratios
    else:
        sequence.pop(0)
        return sequence

n:int = 100000

print(fibi(n))

print(fibisequence(n)[-1])

print(fibisequence(n, True, 10)[-1])