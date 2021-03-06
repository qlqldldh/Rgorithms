import sys

UPDATE = 1


class InputFactory:
    def __init__(self):
        self.input = sys.stdin.readline

    def get_values_from_input(self):
        return map(int, self.input().split())

    def get_value_from_input(self):
        return int(self.input())


class SegmentTree:
    def __init__(self, nums):
        self._nums = nums
        self.tree_array = [0 for _ in range(len(nums) * 4)]

    def setup(self, node, start, end):
        if start == end:
            self.tree_array[node] = self._nums[start]
            return self.tree_array[node]

        mid = (start + end) // 2

        self.tree_array[node] = self.setup(node * 2, start, mid) + self.setup(
            node * 2 + 1, mid + 1, end
        )
        return self.tree_array[node]

    def sum_interval(self, node, start, end, left, right):
        if left > end or right < start:
            return 0

        if left <= start and right >= end:
            return self.tree_array[node]

        mid = (start + end) // 2

        return self.sum_interval(node * 2, start, mid, left, right) + self.sum_interval(
            node * 2 + 1, mid + 1, end, left, right
        )

    def update(self, node, start, end, idx, diff):
        if idx < start or idx > end:
            return

        self.tree_array[node] += diff

        if start != end:
            mid = (start + end) // 2
            self.update(node * 2, start, mid, idx, diff)
            self.update(node * 2 + 1, mid + 1, end, idx, diff)


def solution():
    input_factory = InputFactory()

    n, update_count, sum_count = input_factory.get_values_from_input()

    init_node = 1
    start = 0
    end = n - 1
    nums = [input_factory.get_value_from_input() for _ in range(n)]

    segment_tree = SegmentTree(nums)
    segment_tree.setup(init_node, start, end)

    for _ in range(update_count + sum_count):
        command, b, c = input_factory.get_values_from_input()
        if command == UPDATE:
            segment_tree.update(init_node, start, end, b - 1, c - nums[b - 1])
            nums[b - 1] = c
        else:
            print(segment_tree.sum_interval(init_node, start, end, b - 1, c - 1))


solution()
