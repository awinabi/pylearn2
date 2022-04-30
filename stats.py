import pdb


class Stats:
    def __init__(self, ary):
        self.ary = ary

    def median(self):
        sorted_ary = sorted(self.ary)
        med_index = int(len(sorted_ary) / 2)
        breakpoint()

        if len(self.ary) % 2 == 0:
            return sum(sorted_ary[med_index - 1 : med_index + 1]) / 2.0
        else:
            return sorted_ary[med_index]

    def mean(self):
        return sum(self.ary) / len(self.ary)


a = [10, 2, 3, 4, 5, 8, 1, 2]
s = Stats(a)

print("median: ", s.median())
print("mean: ", s.mean())
