import numpy, sys, time
import matplotlib.pyplot as plt

def mat(n):
    a = numpy.zeros((n, n)) # Matrix A
    b = numpy.zeros((n, n)) # Matrix B
    c = numpy.zeros((n, n)) # Matrix C

    # Initialize the matrices to some values.
    for i in range(n):
        for j in range(n):
            a[i, j] = i * n + j
            b[i, j] = j * n + i
            c[i, j] = 0

    begin = time.time()

    c = a.dot(b)

    end = time.time()
    print("time: %.6f sec" % (end - begin))
    return end - begin

if __name__ == '__main__':
    x = []
    y = []
    for i in range(1,1000):
        res = mat(i)
        x.append(i)
        y.append(res)
    
    plt.plot(x, y, label = "A", color = "red")
    plt.xlabel("value of N")
    plt.ylabel("time[sec]")
    plt.show()

