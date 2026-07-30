class MinStack:
    
    def __init__(self):
        self.thislist = []
        self.minimum = 0

    def push(self, val: int) -> None:
        self.thislist.append(val)
        self.minimum = min(self.minimum, val)
    
    def pop(self) -> None:
        self.thislist.pop()

    def top(self) -> int:
        return self.thislist[-1]
        
    def getMin(self) -> int:
        return min(self.thislist)
       
        

        
