import numpy as np
import matplotlib.pyplot as plt


def func(argA, argB):
    return cp * argA + tp * argB


ca, cb, cp = list(map(int, input(' Chairs : Enter space seperated time for machine A and B and profit : ').split()))
ta, tb, tp = list(map(int, input(' Tables : Enter space seperated time for machine A and B and profit : ').split()))

restA, restB = list(map(int, input('Enter the space seperated time for which the machine is resting : ').split()))

x = range(-10, 11)
a1 = ca
b1 = ta
c1 = -1 * restA
x = np.linspace(-10, 10, 100)

y = (-a1 * x - c1) / b1
fig, ax = plt.subplots()

ax.plot(x, y, color='blue')

a2 = cb
b2 = tb
c2 = -1 * restB

if b2 != 0:
    y = (-a2 * x - c2) / b2
    ax.plot(x, y, color='blue')
else:
    ax.axvline(x=-c2 / a2, color='blue')

A = np.array([[a1, b1], [a2, b2]])
b = np.array([-c1, -c2])
x, y = np.linalg.solve(A, b)
ax.plot(x, y, 'ro')

ax.axhline(y=0, color='black')
ax.axvline(x=0, color='black')

ax.set_xlim(-10, 10)
ax.set_ylim(-10, 10)

plt.show()
ans = 0
s1= func(0, 0)

try:
    s2 = func(-1 * (c2 / a2), 0)
except:
    s2 = func(0,-1 * (c2 / b2))
    # ans+=func
try:
    s3= func(0, -1 * (c1 / b1))
except:
    s3 = func(-1 * (c1 / a1), 0)

s4= func(x, y)
# ans=func(,-1*(c1/b1))

print("Maximum profit is : ", max(s1,s2,s3,s4))