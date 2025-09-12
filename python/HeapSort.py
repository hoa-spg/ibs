
"""Heapsort with in place sorting, using a max heap and placing the largest
element at the end of the considered array in each iteration.

This implementation prints a step-by-step trace similar to `Quicksort.py` in
this repository. Behaviour:
- Before sorting starts it prints the initial array line.
- During heap construction and during the repeated extraction phase each
  swap performed during sift-down (heapify/versickern) is printed.
- When the max is selected (the root) it is shown as chosen (printed as
  (v) ) and when it is moved to its final place at the end of the current
  heap range it is printed as placed ( [v] ).

"""



# a = [9, 7, 8, 2, 4, 6, 2, 1]
a = [37, 12, 45, 2, 18, 25, 7, 30, 50, 1, 19, 5] # Anhang 1. Beispiel

# a = [14, 10, 11, 7, 9, 3, 6, 4, 1, 2, 8, 5] # Anhang

def heapify(n, i, heap_left, heap_right):
	"""Sift-down (versickern) at index i for heap size n.
	Performs sift-down without intermediate prints. The caller will print
	a line after the heapify completes.
	"""
	while True:
		left = 2 * i + 1
		right = 2 * i + 2
		largest = i
		if left < n and a[left] > a[largest]:
			largest = left
		if right < n and a[right] > a[largest]:
			largest = right
		if largest != i:
			swap(i, largest)
			i = largest
			continue
		break


def build_max_heap(n):
	# heapify from last non-leaf down to root
	for i in range((n // 2) - 1, -1, -1):
		heapify(n, i, 0, n - 1)


def heapsort():
	n = len(a)
	# initial state
	print("Initial array:")
	printLine(pivotPos=-1, pivotSelected=False, pivotFinallyPlaced=False,
			  partitionLeftPos=0, partitionRightPos=n - 1)
	print()

	# build heap
	build_max_heap(n)

	print("After initial heap construction:")
	printLine(pivotPos=-1, pivotSelected=False, pivotFinallyPlaced=False,
			  partitionLeftPos=0, partitionRightPos=n - 1)
	print()

	# extraction phase: remove max and place at end
	for end in range(n - 1, 0, -1):
		# show root (maximum) and current heap end marked with '|'
		printLine(pivotPos=0, pivotSelected=True, pivotFinallyPlaced=False,
				  partitionLeftPos=0, partitionRightPos=end)

		# swap root with a[end]
		swap(0, end)
		# print array immediately after swap; show the reduced heap (end-1)
		printLine(pivotPos=-1, pivotSelected=False, pivotFinallyPlaced=False,
				  partitionLeftPos=0, partitionRightPos=end - 1)

		# heapify reduced heap, then print the array after heapify
		heapify(end, 0, 0, end - 1)
		printLine(pivotPos=-1, pivotSelected=False, pivotFinallyPlaced=False,
				  partitionLeftPos=0, partitionRightPos=end - 1)
		print()


def swap(i, j):
	a[i], a[j] = a[j], a[i]


def printLine(*, pivotPos, pivotSelected, pivotFinallyPlaced,
			  partitionLeftPos=None, partitionRightPos=None,
			  swappedLeft=None, swappedRight=None):
	# simplified printing: fixed-width columns and '|' markers for heap bounds
	numw = max(len(str(x)) for x in a)
	cellw = numw + 2
	parts = []
	for idx, val in enumerate(a):
		sval = str(val).rjust(numw)
		if idx == pivotPos and pivotSelected:
			s = f"({sval})".rjust(cellw)
		elif idx == pivotPos and pivotFinallyPlaced:
			s = f"[{sval}]".rjust(cellw)
		else:
			s = f" {sval} ".rjust(cellw)
		parts.append((idx, s))

	line = ""
	for idx, s in parts:
		if partitionLeftPos is not None and idx == partitionLeftPos:
			line += "| "
		line += s
		if partitionRightPos is not None and idx == partitionRightPos:
			line += " |"
		line += "  "
	print(line.rstrip())


if __name__ == '__main__':
	heapsort()


