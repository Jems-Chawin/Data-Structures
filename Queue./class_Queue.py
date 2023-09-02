class Queue():
    def __init__(self) -> None:
        self.queue = list()
    
    def size(self) -> int:
        return len(self.queue)
    
    def is_empty(self) -> bool:
        return not bool(len(self.queue))
    
    def enqueue(self, data: any) -> None:
        self.queue.append(data)
    
    def dequeue(self) -> any:
        if not self.is_empty():
            return self.queue.pop(0)
    
    def front(self) -> any:
        return self.queue[0]
    
    def rear(self) -> any:
        return self.queue[-1]
    
    def __str__(self) -> str:
        return str(self.queue)
