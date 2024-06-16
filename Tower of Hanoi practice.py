step = 1


def hano(a, b, c, n):
    global step
    if n == 1:
        print("[STEP{:>4}] {}->{}".format(step, a, c))
        step = step + 1
    else:
        hano(a, c, b, n - 1)
        print("[STEP{:>4}] {}->{}".format(step, a, c))
        step = step + 1
        hano(b, a, c, n - 1)


n = eval(input())
hano("A", "B", "C", n)
