import math
import random
import matplotlib
import matplotlib.pyplot as plt

totalSimulations = 1000
t = 0
n = 0

# maximum number of molecules
limit = 50

# r0 is decay
r0 = 0.01

# r1 is production
r1 = 0.02

X = 1

simulation = list()


while n < totalSimulations:
    rT = random.uniform(0, 1)
    rR = bool(random.getrandbits(1))
    t = t +rT

    if rR == 0 and X > 0:
        X = X - r0 * X

    elif X < limit:
        X = X + r1 * X


    n = n + 1
    simulation.append((t, int(X)))


fig = plt.figure()
plt.axis([0,1000, 0, 100])
plt.xlabel("time")
plt.ylabel("X")


for i in range(len(simulation)):
    print(str(i), str(simulation[i][0]), str(simulation[i][1]))
    plt.scatter(i, simulation[i][1], s=1)
    #plt.pause(0.001)



plt.savefig("gillespie.png")

