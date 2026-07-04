class TimeMap:

    def __init__(self):
        self.hashmap = {}

    def set(self, key: str, value: str, timestamp: int) -> None:
        if self.hashmap.get(key):
            self.hashmap[key].get("values").append(value)
            self.hashmap[key].get("timestamps").append(timestamp)
        else:
            self.hashmap[key] = {"values": [value], "timestamps": [timestamp]}

    def get(self, key: str, timestamp: int) -> str:
        print(self.hashmap)
        if self.hashmap.get(key):
            # find timestamp index
            timestamps = self.hashmap[key].get("timestamps")
            mid = 0
            l = 0
            r = len(timestamps) - 1
            result = ""
            while l <= r:
                mid = (l + r) // 2
                if timestamps[mid] < timestamp:
                    result = self.hashmap[key].get("values")[mid]
                    l = mid + 1
                elif timestamps[mid] > timestamp:
                    r = mid - 1
                else:
                    return self.hashmap[key].get("values")[mid]
            return result
        else:
            return ""
        
