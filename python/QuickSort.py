a = [37, 12, 45, 2, 18, 25, 7, 30, 50, 1, 19, 5] # Anhang 1. Beispiel

# a = [14, 10, 11, 7, 9, 3, 6, 4, 1, 2, 8, 5] # Anhang 2. Beispiel

def quicksort(left, right):
    if left < right:
        pidx = partition(left, right)
        quicksort(left, pidx - 1)
        quicksort(pidx + 1, right)

# Variant of Hoare's partition scheme (used here)
def partition(left, right):
    pivot = a[right]
    printLine(pivotPos=right, pivotSelected=True, pivotFinallyPlaced=False, partitionLeftPos=left, partitionRightPos=right)

    i = left
    j = right - 1
    while i < j:
        while a[i] < pivot:
            i += 1
        while j > left and a[j] >= pivot:
            j -= 1

        if i < j:
            swap(i, j)
            i += 1
            j -= 1
            printLine(pivotPos=-1, pivotSelected=False, pivotFinallyPlaced=False, partitionLeftPos=left, partitionRightPos=right)

    if i == j and a[i] < pivot:
        i += 1

    if a[i] != pivot:
        swap(i, right)

    printLine(pivotPos=i, pivotSelected=False, pivotFinallyPlaced=True, partitionLeftPos=left, partitionRightPos=right)
    print()
    return i

# Lomuto's partition scheme (not used here)
def partition2(left, right):
    pivot = a[right]
    i = left
    for j in range(left, right + 1):
        if a[j] < pivot:
            swap(i, j)
            printLine(pivotPos=-1, pivotSelected=False, pivotFinallyPlaced=False, partitionLeftPos=left, partitionRightPos=right)
            i += 1
    swap(i, right)

    printLine(pivotPos=i, pivotSelected=False, pivotFinallyPlaced=False, partitionLeftPos=left, partitionRightPos=right)
    print()
    return i


def swap(i, j):
    a[i], a[j] = a[j], a[i]
    printLine(pivotPos=-1, pivotSelected=False, pivotFinallyPlaced=False, swappedLeft=min(i,j), swappedRight=max(i,j))


def printLine(*, pivotPos, pivotSelected, pivotFinallyPlaced, partitionLeftPos=None, partitionRightPos=None, swappedLeft=None, swappedRight=None):
    line = ""
    for idx, val in enumerate(a):
        line += ">" if idx == partitionLeftPos else " "

        if idx == pivotPos and pivotSelected:
            line += f"({val})".center(6)
        elif idx == pivotPos and pivotFinallyPlaced:
            line += f"[{val}]".center(6)
        elif idx == swappedLeft:
            line += f"l*{val}".center(6)
        elif idx == swappedRight:
            line += f"r*{val}".center(6)            
        else:
            line += f"{val}".center(6)
        line += "<" if idx == partitionRightPos else " "
    print(line)


if __name__ == "__main__":
    printLine(pivotPos=-1, pivotSelected=False, pivotFinallyPlaced=False, partitionLeftPos=0, partitionRightPos=(len(a) - 1))
    print()
    quicksort(0, len(a) - 1)
