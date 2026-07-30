class MinStack:
    
    def __init__(self):
        self.thislist = []
        self.minimum = []

    def push(self, val: int) -> None:
        self.thislist.append(val)
        val = min(val, self.minimum[-1] if self.minimum else val)
        self.minimum.append(val)
    def pop(self) -> None:
        self.thislist.pop()
        self.minimum.pop()

    def top(self) -> int:
        return self.thislist[-1]
        
    def getMin(self) -> int:
        return self.minimum[-1]
       
        

        
