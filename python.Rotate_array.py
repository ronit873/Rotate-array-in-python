class solution:
    def rotate(self,arr):
        arr.insert(0,arr.pop())
        return arr 