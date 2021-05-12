import os, time, random
i = 1
a = "-"
b = "_"
num = random.randrange(1,90)
list = range(random.randrange(22,60))
skip = {(iter):" " for iter in list}
y_n = [a, a, b]
y_y_n = [a, a, b, a, b, b]
maxl = (max(skip))
e = maxl
time.sleep(0.2)
def big_skip():
    r = random.randrange(1,30)
    a = "-"
    b = "_"
    c = 0
    y = 0
    d = ' '
    e = -1
    for i in range(1,60):
        os.system('cls' if os.name == 'nt' else 'clear')
        print(skip.get(1," ")+skip.get(2," ")+skip.get(3," ")+skip.get(4," ")+skip.get(5," ")+skip.get(6," ")+skip.get(7," ")+skip.get(8," ")+skip.get(9," ")+skip.get(10," ")+skip.get(11," ")+skip.get(12," ")+skip.get(13," ")+skip.get(14," ")+skip.get(15," ")+skip.get(16," ")+skip.get(17," ")+skip.get(18," ")+skip.get(19," ")+skip.get(20," ")+skip.get(21," ")+skip.get(22," ")+skip.get(23," ")+skip.get(24," ")+skip.get(25," ")+skip.get(26," ")+skip.get(27," ")+skip.get(28," ")+skip.get(29," ")+skip.get(30," ")+skip.get(31," ")+skip.get(32," ")+skip.get(33," ")+skip.get(34," ")+skip.get(35," ")+skip.get(36," ")+skip.get(37," ")+skip.get(38," ")+skip.get(39," ")+skip.get(40," ")+skip.get(41," ")+skip.get(42," ")+skip.get(43," ")+skip.get(44," ")+skip.get(45," ")+skip.get(46," ")+skip.get(47," ")+skip.get(48," ")+skip.get(49," ")+skip.get(50," ")+skip.get(51," ")+skip.get(52," ")+skip.get(53," ")+skip.get(54," ")+skip.get(55," ")+skip.get(56," ")+skip.get(57," ")+skip.get(58," ")+skip.get(59," ")+skip.get(60," "))
        c+=1
        e+=1
        y+=3
        n = 0.1
        q = (n / 10)
        time.sleep(n)
        n = n - q
        print(n, q)
        if n <= 0.03:
                n = 0.01
        skip[c] = random.choice(y_n)
        skip[e] = d
        if (c >= 15):
            skip[c] = random.choice(y_y_n)
        if (c % 2) == 0:
            skip[c] == b
            continue
big_skip()
