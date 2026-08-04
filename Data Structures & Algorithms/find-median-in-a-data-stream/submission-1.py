class MedianFinder:

    def __init__(self):
        self.heap = deque()

    def addNum(self, num: int) -> None:
        self.heap.append(num)

    def findMedian(self) -> float:
        self.heap = sorted(self.heap)
        if len(self.heap) == 0:
            return
        if (len(self.heap)) == 1:
            return self.heap[0]

        if len(self.heap) == 2:
            return (float(self.heap[0]) + float(self.heap[1])) / 2.0

        mid = len(self.heap) // 2

        if len(self.heap) % 2 == 1:
            return self.heap[mid]

        return (float(self.heap[mid]) + float(self.heap[mid - 1])) / 2.0
        
        