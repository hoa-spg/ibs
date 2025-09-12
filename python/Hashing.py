class ProbingHashTable:
    """
    Implements the two open-addressing probe sequences from the script:
    - linear probing:   h_i(k) = (h'(k) + i) mod m
    - quadratic probing: h_i(k) = (h'(k) + i + i^2) mod m  (c1=c2=1)

    Methods return a list of table snapshots (list of lists) after each insertion.
    """

    def __init__(self, m=8):
        self.m = m

    def _h0(self, k):
        return k % self.m

    def linear_probe_sequence(self, keys):
        """
        Insert `keys` in given order using linear probing.
        Return list of table snapshots after each insertion.
        """
        T = [None] * self.m
        snapshots = []
        for k in keys:
            base = self._h0(k)
            i = 0
            placed = False
            while i < self.m:
                pos = (base + i) % self.m
                if T[pos] is None:
                    T[pos] = k
                    snapshots.append(T.copy())
                    placed = True
                    break
                i += 1
            if not placed:
                raise RuntimeError("Hash table full, could not insert {}".format(k))
        return snapshots

    def quadratic_probe_sequence(self, keys):
        """
        Insert `keys` in given order using quadratic probing with f(i)=i+i^2.
        Return list of table snapshots after each insertion.
        """
        T = [None] * self.m
        snapshots = []
        for k in keys:
            base = self._h0(k)
            i = 0
            placed = False
            while i < self.m:
                pos = (base + i + i * i) % self.m
                if T[pos] is None:
                    T[pos] = k
                    snapshots.append(T.copy())
                    placed = True
                    break
                i += 1
            if not placed:
                raise RuntimeError("Hash table full, could not insert {}".format(k))
        return snapshots

    @staticmethod
    def format_table(T):
        """Return a tuple (indices_row, values_row) for easy printing/testing."""
        indices = list(range(len(T)))
        values = [("" if v is None else str(v)) for v in T]
        return indices, values


if __name__ == "__main__":
    # Use exactly the examples from the script
    # keys = [10, 19, 31, 22, 14, 16]
    keys = [11, 14, 5, 19, 1, 27]

    h = ProbingHashTable(m=8)

    print("Linear probing snapshots:")
    linear_snapshots = h.linear_probe_sequence(keys)
    for step, tbl in enumerate(linear_snapshots, start=1):
        idxs, vals = ProbingHashTable.format_table(tbl)
        print(f"After inserting {keys[step-1]}:") 
        print("Index:", " ".join(f"{i:>2}" for i in idxs))
        print("Table:", " ".join(f"{v:>2}" if v else "  " for v in vals))
        print()

    print("Quadratic probing snapshots:")
    quad_snapshots = h.quadratic_probe_sequence(keys)
    for step, tbl in enumerate(quad_snapshots, start=1):
        idxs, vals = ProbingHashTable.format_table(tbl)
        print(f"After inserting {keys[step-1]}:")
        print("Index:", " ".join(f"{i:>2}" for i in idxs))
        print("Table:", " ".join(f"{v:>2}" if v else "  " for v in vals))
        print()