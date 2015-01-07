import numpy as np
import matplotlib.pyplot as plt
from pandas.stats.moments import rolling_mean, rolling_std


def plot(sample_file_name, window):
    data = open(sample_file_name, 'r').read()
    data = data.split('\n')
    x, y = np.loadtxt(data, delimiter=';', unpack=True)

    sma = rolling_mean(y, window)
    roll_std = rolling_std(y, window)
    ub = sma + (roll_std * 2)
    lb = sma - (roll_std * 2)

    plt.plot(x[window:], sma[window:], label='middle band', linewidth=0.3, alpha=0.95)
    plt.plot(x[window:], ub[window:], label='upper band', linewidth=0.3, alpha=0.95)
    plt.plot(x[window:], lb[window:], label='lower band', linewidth=0.3, alpha=0.95)
    plt.fill_between(x, lb, ub, facecolor='grey', alpha=0.7)

    plt.plot(x[window:], y[window:], label='plot', linewidth=1.3)
    plt.xlim(x[window + 1], x[-1])
    plt.legend()
    plt.show()


if __name__ == "__main__":
    plot('example/sample.csv', 20)