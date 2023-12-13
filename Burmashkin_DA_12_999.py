from matplotlib import pyplot as plt
from matplotlib.gridspec import GridSpec
import numpy as np

gs = GridSpec(3, 5)

def graphic(A, B, color, name, gs):
    window = plt.subplot(gs)
    x = np.linspace(-50, 50, 10001)
    x[x == 0] = None
    y = (x ** B + A ** B) / x ** B
    window = plt.plot(x, y, label=name, color=color)
    plt.xlim(-40, 40)
    plt.ylim(-1, 5)
    plt.xlabel('Ось х')
    plt.ylabel('Ось y')
    plt.legend(loc='lower left')
    plt.grid()


graphic(1, 2, 'r', 'a=1 B=2', gs[0, 0])
graphic(1, 1, 'b', 'a=1 B=1', gs[1, 0])
graphic(2, 1, 'lime', 'a=2 B=1', gs[2, 0])

graphic(1, 2, 'r', 'a=1 B=2', gs[:, 2:5])
graphic(1, 1, 'b', 'a=1 B=1', gs[:, 2:5])
graphic(2, 1, 'lime', 'a=2 B=1', gs[:, 2:5])
plt.title('1)Исследование Графика',fontsize=15,bbox={'boxstyle':'round','facecolor':'white'})

plt.show()
plt.savefig('C:\Проект инфа\my_first_dependence.svg')


def graphic(A, B, color, name, i, o):
    window = plt.subplot(i)
    x = np.linspace(0, 50, o)
    x[x == 0] = None
    y = (x ** B + A ** B) / x ** B
    window = plt.plot(x, y, label=name, color=color)
    plt.xlim(-3, 20)
    plt.ylim(0, 6)
    plt.legend(loc='lower left')
    plt.grid()


gs = GridSpec(4, 4)
graphic(1, 2, 'r', 'a=1 B=2', gs[:, :], 10001)
graphic(1, 1, 'b', 'a=1 B=1', gs[:, :], 10001)
graphic(2, 1, 'lime', 'a=2 B=1', gs[:, :], 10001)
plt.xlabel('Ось х')
plt.ylabel('Ось y')
plt.text(7, 1.9, '2)График для X>0', fontsize=17, bbox={'boxstyle': 'round', 'facecolor': 'white'})
plt.text(1.9, 3.8, 'Стремиться\nпо оси y к ∞', bbox={'boxstyle': 'larrow', 'facecolor': 'white'})
plt.text(1.9, 4.8, 'Пересечение\nкрасного и\nзеленого\nграфика в (0.5,5.0)', fontsize=7,
         bbox={'boxstyle': 'larrow', 'facecolor': 'white'})
plt.text(-3.9, 1.8, 'Пересечение\nкрасного и\nсинего\nграфика в\n(1.0,2.0)', fontsize=7,
         bbox={'boxstyle': 'rarrow', 'facecolor': 'white'})

graphic(1, 2, 'r', 'a=1 B=2', gs[0:2, 3:4], 10001)
graphic(1, 1, 'b', 'a=1 B=2', gs[0:2, 3:4], 10001)
graphic(2, 1, 'lime', 'a=1 B=2', gs[0:2, 3:4], 10001)
plt.title('Для б. X', fontsize=14, bbox={'boxstyle': 'round', 'facecolor': 'white'})
plt.legend()
graphic(1, 2, 'r', 'a=1 B=2', gs[0:2, 2:3], 101)
graphic(1, 1, 'b', 'a=1 B=2', gs[0:2, 2:3], 101)
graphic(2, 1, 'lime', 'a=1 B=2', gs[0:2, 2:3], 101)
plt.title('Для м. X', fontsize=14, bbox={'boxstyle': 'round', 'facecolor': 'white'})
plt.legend()
plt.show()

gs = GridSpec(5, 5)


def graphic(A, B, color, name, i, o1, o2):
    window = plt.subplot(i)
    x = np.linspace(o1, o2, 10001)
    x[x == 0] = None
    y = (x ** B + A ** B) / x ** B
    window = plt.plot(x, y, label=name, color=color)
    plt.xlim(-20, 3)
    plt.ylim(-9, 3)
    plt.legend(loc='lower right')
    plt.grid()


graphic(1, 2, 'r', 'a=1 B=2', gs[:, :], -50, 0)
graphic(1, 1, 'b', 'a=1 B=1', gs[:, :], -50, 0)
graphic(2, 1, 'lime', 'a=2 B=1', gs[:, :], -50, 0)
plt.subplot(gs[:, :])
x = np.linspace(-40, 3, 1000)
y = x
plt.plot(x, y, label='f(x)', color='black')
plt.legend(loc='lower right')
plt.title('3)График для X<0', fontsize=17, bbox={'boxstyle': 'round', 'facecolor': 'white'})
plt.text(-16, -2, 'Графики функции не\n имеют пересечений', fontsize=15,
         bbox={'boxstyle': 'round', 'facecolor': 'white'})

graphic(1, 2, 'r', 'a=1 B=2', gs[3:5, 0:2], -1000, 0)
graphic(1, 1, 'b', 'a=1 B=1', gs[3:5, 0:2], -1000, 0)
graphic(2, 1, 'lime', 'a=2 B=1', gs[3:5, 0:2], -1000, 0)
plt.title('Удаление x\nот 0 до -∞', fontsize=11, bbox={'boxstyle': 'round', 'facecolor': 'white'})

plt.show()

gs = GridSpec(3, 5)


def graphic(A, B, color, name, i):
    window = plt.subplot(i)
    x = np.linspace(0, 1000, 100001)
    x[x == 0] = None
    y = (x ** B + A ** B) / x ** B
    window = plt.plot(x, y, label=name, color=color)
    plt.xlim(-40, 110)
    plt.ylim(-2, 8)
    plt.xlabel('Ось х')
    plt.ylabel('Ось y')
    plt.legend(loc='lower left')
    plt.grid()



graphic(1, 0.5, 'orange', 'a=1 B=0.5', gs[:, :])
graphic(1, -0.5, 'cyan', 'a=1 B=-0.5', gs[:, :])
graphic(1, -1.5, 'teal', 'a=1 B=-1.5', gs[:, :])
plt.title('4)Графики',fontsize=18,bbox={'boxstyle':'round','facecolor':'white'})
plt.show()

gs = GridSpec(18, 15)

def graphic(A, B, x, linestyle, color, name, i):
    okno = plt.subplot(i)
    x = np.linspace(x, 1000, 100001)
    x[x == 0] = None
    y = (x ** B + A ** B) / x ** B
    okno = plt.plot(x, y, linestyle=linestyle, label=name, color=color)
    plt.xlim(-20, 100)
    plt.ylim(-2, 10)
    plt.xlabel('Ось х')
    plt.ylabel('Ось y')
    plt.legend(loc='lower right')


graphic(1, 0, -1000, '--', 'b', 'a=1 B=0', gs[0:8, 0:7])
graphic(1, -1, -1000, '--', 'r', 'a=1 B=-1', gs[0:8, 0:7])
graphic(1, 0.5, 0, '-', 'green', 'a=1 B=0.5', gs[0:8, 0:7])
graphic(1, 0.8, 0, '-', 'darkred', 'a=1 B=0.8', gs[0:8, 0:7])
plt.grid()

graphic(1, 0, -1000, '--', 'b', 'a=1 B=0', gs[0:8, 8:15])
graphic(1, -1, -1000, '--', 'r', 'a=1 B=-1', gs[0:8, 8:15])
graphic(1, -0.5, 0, '-', 'green', 'a=1 B=-0.5', gs[0:8, 8:15])
graphic(1, -0.8, 0, '-', 'darkred', 'a=1 B=-0.8', gs[0:8, 8:15])
plt.grid()

graphic(1, 0, -1000, '--', 'b', 'a=1 B=0', gs[10:18, 4:11])
graphic(1, -1, -1000, '--', 'r', 'a=1 B=-1', gs[10:18, 4:11])
graphic(1, -1.5, 0, '-', 'green', 'a=1 B=-1.5', gs[10:18, 4:11])
graphic(1, -2.5, 0, '-', 'darkred', 'a=1 B=-2.5', gs[10:18, 4:11])
plt.grid()

plt.suptitle('5)Последний Подпункт',fontsize=16,bbox={'boxstyle':'round','facecolor':'white'})
plt.show()
