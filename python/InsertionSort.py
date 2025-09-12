# a = [37, 12, 45, 2, 18, 25, 7, 30, 50, 1, 19, 5]  # Anhang Beispiel 1
a = [14, 10, 11, 7, 9, 3, 6, 4, 1, 2, 8, 5]     # Anhang Beispiel 2


def insertion_sort():
    n = len(a)
    for i in range(1, n):
        key = a[i]
        j = i - 1
        while j >= 0 and a[j] > key:
            a[j + 1] = a[j]
            j -= 1
        a[j + 1] = key
        # Ausgabe: das eingefügte Element in [ ] und das verdrängte in ( )
        printLine(insertedIndex=j + 1, originalIndex=i)


def printLine(insertedIndex, originalIndex):
    line = ""
    for idx, val in enumerate(a):
        if idx == originalIndex and idx == insertedIndex:
            line += f"[{val}]|".center(6)  # ursprüngliche Position
        elif idx == insertedIndex:
            line += f"[{val}]".center(6)  # eingefügtes Element
        elif idx == originalIndex:
            line += f" {val}|".center(6)  # ursprüngliche Position

        else:
            line += f"{val}".center(6)
    print(line)


if __name__ == "__main__":
    printLine(-1, -1)
    print()
    insertion_sort()
