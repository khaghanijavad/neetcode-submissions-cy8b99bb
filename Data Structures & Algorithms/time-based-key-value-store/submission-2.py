class TimeMap:

    def __init__(self):
        self.memory = {}
        

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key not in self.memory:
            self.memory[key] = [(value, timestamp)]  
        else:
            self.memory[key].append((value, timestamp))    

    def get(self, key: str, timestamp: int) -> str:
        output = ""
        values = self.memory.get(key, [])
        l, r = -1, len(values)

        while l + 1 < r:
            mid = (l + r) // 2
            if values[mid][1] <= timestamp:
                output = values[mid][0]
                l = mid
            else: 
                r = mid
        return output


        
