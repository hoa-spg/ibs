# a = [37, 12, 45, 2, 18, 25, 7, 30, 50, 1, 19, 5]  # Anhang Beispiel 1
a = [14, 10, 11, 7, 9, 3, 6, 4, 1, 2, 8, 5]         # Anhang Beispiel 2


def selection_sort():
    n = len(a)
    for i in range(n - 1):
        min_idx = i
        for j in range(i + 1, n):
            if a[j] < a[min_idx]:
                min_idx = j
        if min_idx != i:
            printLine(i, min_idx)
            swap(i, min_idx)


def swap(i, j):
    a[i], a[j] = a[j], a[i]


def printLine(i, min_idx):
    line = ""
    for idx, val in enumerate(a):
        if idx == i:
            line += f"({val})".center(6)  # verdrängtes Element (nach hinten)
        elif idx == min_idx:
            line += f"[{val}]".center(6)  # Minimum kommt nach vorne
        else:
            line += f"{val}".center(6)
    print(line)


if __name__ == "__main__":
    printLine(-1, -1)
    print()
    selection_sort()
