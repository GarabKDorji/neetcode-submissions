class MinStack:

    def __init__(self):
        self.store = [] 
        self.min_store = []

    def push(self, val: int) -> None:
    
        self.store.append(val)

        if not self.min_store:
            self.min_store.append(val)
        else:
            self.min_store.append(min(val, self.min_store[-1]))

    def pop(self) -> None:
        if not self.store:
            return 
        self.store.pop()
        self.min_store.pop()
      
     


    def top(self) -> int:
        if not self.store:
            return None 
        return self.store[-1]

    def getMin(self) -> int:
        return self.min_store[-1]
        
