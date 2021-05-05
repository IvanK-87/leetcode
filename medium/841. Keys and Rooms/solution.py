class Solution:
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
        l = len(rooms)
        collected_keys = set()        
        keys = deque()
        k = 0
        collected_keys.add(k)
        for i in range(l):
            for key in rooms[k]:
                if key not in collected_keys:
                    collected_keys.add(key)
                    keys.append(key)
            if len(keys) == 0:
                break
            k = keys.popleft()
            
        for i in range(l):
            if i not in collected_keys:
                return False
        return True