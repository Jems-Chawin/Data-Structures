class Stack:
    def __init__(self) -> None:
        self.stack = list()
    
    def size(self) -> int:
        return len(self.stack)
    
    def is_empty(self) -> bool:
        return not bool(len(self.stack))
    
    def push(self, data: any) -> None:
        self.stack.append(data)

    def pop(self) -> any:
        if not self.is_empty():
            return self.stack.pop() 
    
    def peek(self) -> any:
        if not self.is_empty():
            return self.stack[-1]
    
    def __str__(self) -> str:
        return str(self.stack)
