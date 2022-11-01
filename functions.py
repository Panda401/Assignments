import math


def func4(x):
    # |sin x/3,12+cosx2|-8,3sin3x
    return math.fabs(math.sin(x / 3.12) + math.cos(x * x)) - 8.3 * math.sin(3 * x)


def func5(x):
    # cos|2x| /1,12-cos(3x-2)+6,15
    return math.cos(math.fabs(2 * x)) / 1.12 - math.cos(3 * x - 2) + 6.15


def func6(x):
    # sin x cosx2 sin(x+1,4)+5,14
    return math.sin(x) * math.cos(x * x) * math.sin(x + 1.4) + 5.14


def func7(x):
    # |sin(2x-1,5)+3sinx2|+2,38
    return math.fabs(math.sin(2 * x - 1.5) + 3 * math.sin(x * x)) + 2.38


def func8(x):
    # cos x2sin(2x-1)+4,29
    return math.cos(x) * x * x * math.sin(2 * x - 1) + 4.29


def func9(x):
    # cos(x2+1)-|sin2x-5,76|
    return math.cos(x * x + 1) - math.fabs(math.sin(2 * x) - 5.76)


def func10(x):
    # sinx-cosx3sin(x2-4,2)+4,27
    return math.sin(x) - math.cos(x) * 3 * math.sin(x * x - 4.2) + 4.27
