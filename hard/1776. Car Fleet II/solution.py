class Solution:
    def getCollisionTimes(self, cars: List[List[int]]) -> List[float]:
        n = len(cars)
        answer = [-1]*n
        slow_cars = deque()
        v_min = cars[-1][1]
        slow_cars.append((cars[-1][0], v_min, inf))

        for i in reversed(range(n-1)):
            v1 = cars[i][1]
            if v_min < v1:
                while True:
                    p, v, t = slow_cars[0] 
                    if v < v1:
                        p1 = cars[i][0]
                        t_min = (p-p1)/(v1-v)
                        if t > t_min:
                            slow_cars.appendleft((p1, v1, t_min))
                            answer[i] = t_min
                            break
                    slow_cars.popleft()
            else:
                slow_cars = deque()
                slow_cars.append((cars[i][0], v1, inf))
                v_min = v1
                    
        return answer