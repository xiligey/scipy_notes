from matplotlib import pyplot as plt
from scipy.interpolate import interp1d

if __name__ == '__main__':
    x = [0, 60, 120, 180, 240, 300]
    y = [0, 600, 1100, 1500, 1900, 2100]

    f = interp1d(x, y, kind='linear')
    x_new = range(0, 301, 1)
    y_new = f(x_new)
    print(y_new)

    plt.plot(x_new, y_new, '-', label='interpolated')
    plt.plot(x, y, 'o', label='original')
    plt.legend()
    plt.show()
