class MyCircularQueue:

    def __init__(self, k: int):
        self.max_size = k
        self.vector = [0]*k
        self.size = 0
        self.front_idx = 0 # pointer to the deletion end (next element to pop)
        self.rear_idx = 0 # pointer to insertion end (next element to push)

    def enQueue(self, value: int) -> bool:
        if self.isFull():
            return False
        self.vector[self.rear_idx] = value
        self.rear_idx = (self.rear_idx + 1) % self.max_size
        self.size += 1
        return True


    def deQueue(self) -> bool:
        if self.isEmpty():
            return False
        self.front_idx = (self.front_idx + 1) % self.max_size
        self.size -= 1
        return True

    def Front(self) -> int:
        if self.isEmpty():
            return -1
        return self.vector[self.front_idx]
        

    def Rear(self) -> int:
        if self.isEmpty():
            return -1
        return self.vector[self.rear_idx-1]

    def isEmpty(self) -> bool:
        return self.size == 0

    def isFull(self) -> bool:
        return self.size == self.max_size
        