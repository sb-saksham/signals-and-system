from io import StringIO

import numpy as np
import matplotlib.pyplot as plt
import matplotlib as mpl

mpl.style.use('seaborn')


def periodic_signal(freq, amp, func):
    ts = np.arange(0, 0.3, 1 / (50 * freq))
    phases = 2 * np.pi * freq * ts
    ys = amp * func(phases)
    return ts, ys


def sin_signal(freq, amp):
    return periodic_signal(freq, amp, np.sin)


def cos_signal(freq, amp):
    return periodic_signal(freq, amp, np.cos)


def step(x):
    return 1 * (x > 0)


def impulse(x):
    return 1 * (x == 0)


def plot(t, y, label="Signal"):
    fig = plt.figure()
    ax = fig.gca()
    ax.set_ylim((-2, 2))
    ax.grid(True)
    plt.plot(t, y, 'C1', label=label)

    imgdata = StringIO()
    fig.savefig(imgdata, format='svg')
    imgdata.seek(0)

    data = imgdata.getvalue()
    return data


def plot2(t, y1, y2, label1="C1", label2="C2"):
    fig = plt.figure()
    ax = fig.gca()
    ax.set_ylim((-5, 5))
    ax.grid(True)

    plt.plot(t, y1, 'C1', label=label1)
    plt.plot(t, y2, 'C2', label=label2)
    plt.legend()

    imgdata = StringIO()
    fig.savefig(imgdata, format='svg')
    imgdata.seek(0)

    data = imgdata.getvalue()
    return data


def stem(t, y1, label="y2"):
    fig = plt.figure()
    markerline, stemlines, baseline = plt.stem(t, y1, markerfmt='o', label=label)
    plt.setp(stemlines, 'color', plt.getp(markerline, 'color'))
    plt.setp(stemlines, 'linestyle', 'dotted')

    plt.legend()

    imgdata = StringIO()
    fig.savefig(imgdata, format='svg')
    imgdata.seek(0)

    data = imgdata.getvalue()
    return data


def stem2(t, y1, y2, label1="y1", label2="y2"):
    fig = plt.figure()
    markerline, stemlines, baseline = plt.stem(t, y1, linefmt="r", markerfmt='o', label=label1)
    plt.setp(stemlines, 'color', 'red')
    plt.setp(stemlines, 'linestyle', 'dotted')

    markerline, stemlines, baseline = plt.stem(t, y2, markerfmt='o', label=label2)
    plt.setp(stemlines, 'color', 'blue')
    plt.setp(stemlines, 'linestyle', 'dotted')

    plt.legend()

    imgdata = StringIO()
    fig.savefig(imgdata, format='svg')
    imgdata.seek(0)

    data = imgdata.getvalue()
    return data