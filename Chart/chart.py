import matplotlib
import matplotlib.pyplot as plt
import numpy as np


y = [2, 4, 6, 8, 10, 12, 14, 16, 18, 20]
x = np.arange(10)
fig = plt.figure()
ax = plt.subplot(111)
ax.plot(x, y, label='$y = numbers')
plt.title('Legend inside')
ax.legend()
# plt.show()

fig.savefig('c://Python_Lessons//plot22.png')
'''

y = ('Python', 'C++', 'Java', 'Perl', 'Scala', 'Lisp')
x = np.arange(len(10))
#x = [10, 8, 6, 4, 2, 1]
fig = plt.figure()
ax = plt.subplot(111)
ax.plot(x, y, label='$y = Usage')

#plt.ylabel('Usage')
plt.title('Programming language usage')
ax.legend()
fig.savefig('c://Python_Lessons//plot22.png')

#plt.bar(y, x, align='center', alpha=0.5)
#plt.xticks(y_pos, values)

'''