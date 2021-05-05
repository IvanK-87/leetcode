class Solution:
    def reachingPoints(self, sx: int, sy: int, tx: int, ty: int) -> bool:     

        if tx < sx or ty < sy or tx == ty:
            return False
        elif tx == sx and (ty-sy) % sx == 0:
            return True
        elif ty == sy and (tx-sx) % sy == 0:
            return True
        
        if tx > ty:
            tx = tx % ty
            if tx <= sx:
                if tx == sx:
                    return ((ty-sy) % sx == 0)
                else:
                    return False
                

        while True:
            ty = ty % tx
            if ty <= sy:
                if ty == sy:
                    return ((tx-sx) % sy == 0)
                else:
                    return False
            tx = tx % ty
            if tx <= sx:
                if tx == sx:
                    return ((ty-sy) % sx == 0)
                else:
                    return False