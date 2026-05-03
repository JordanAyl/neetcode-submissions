class Deque:
    
    def __init__(self):
        self.quelist = []

    def isEmpty(self) -> bool:
        if not self.quelist:
            return True
        else:
            return False

    def append(self, value: int) -> None:
        self.quelist.append(value)

    def appendleft(self, value: int) -> None:
        self.quelist.insert(0, value)

    def pop(self) -> int:
        if not self.quelist:
            return -1

        return self.quelist.pop()

    def popleft(self) -> int:
        if not self.quelist:
            return -1
            
        return self.quelist.pop(0)
