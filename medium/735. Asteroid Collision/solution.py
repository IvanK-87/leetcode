class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        l = len(asteroids)
        if l <= 1:
            return asteroids
        last_state = deque()
        last_astrd = 0
        
        for i in asteroids:
            if i < 0: 
                if last_astrd > 0:
                    while last_astrd > 0:
                        if last_state[-1] > -i:
                            break
                        elif last_state[-1] == -i:
                            last_astrd -= 1
                            last_state.pop()
                            break
                        else:
                            last_astrd -= 1
                            last_state.pop()
                    else:
                        last_state.append(i)
                            
                else:
                    last_state.append(i)
            else:
                last_state.append(i)
                last_astrd += 1

        return list(last_state)