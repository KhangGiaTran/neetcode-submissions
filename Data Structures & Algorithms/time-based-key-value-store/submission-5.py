class TimeMap:

    def __init__(self):
        self.hashmap = {}

    def set(self, key: str, value: str, timestamp: int) -> None:
        if self.hashmap.get(key):
            self.hashmap[key]["timestamps"].append(timestamp)
            self.hashmap[key]["values"].append(value)
        else:
            self.hashmap[key] = {
                "timestamps": [timestamp],
                "values": [value]
            }

    def get(self, key: str, timestamp: int) -> str:
        item = self.hashmap.get(key)
        if item == None:
            return ""
        timestamps = item["timestamps"]
        values = item["values"]

        l, r = 0, len(timestamps) - 1
        result = ""

        while l <= r:
            mid = (l + r) // 2
            if timestamps[mid] > timestamp:
                r = mid - 1
            else:
                l = mid + 1
                result = values[mid]
        return result



