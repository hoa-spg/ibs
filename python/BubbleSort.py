# a = [37, 12, 45, 2, 18, 25, 7, 30, 50, 1, 19, 5]  # Beispiel
a = [14, 10, 11, 7, 9, 3, 6, 4, 1, 2, 8, 5]     # Beispiel 2


def bubble_sort():
    n = len(a)
    for i in range(n):
        swapped = False
        for j in range(0, n - i - 1):
            if a[j] > a[j + 1]:
                swap(j, j + 1)
                swapped = True
        # Nach jedem Durchlauf Array ausgeben (ohne Markierungen)
        printLine()
        if not swapped:
            break


def swap(i, j):
    a[i], a[j] = a[j], a[i]


def printLine():
    line = ""
    for val in a:
        line += f"{val}".center(6)
    print(line)


if __name__ == "__main__":
    printLine()
    print()
    bubble_sort()
