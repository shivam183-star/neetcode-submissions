class Solution:
    def lemonadeChange(self, bills: List[int]) -> bool:
        hashmap = { 5 : 0,
                   10 : 0}
        
        for bill in bills:
            if bill == 5:
                hashmap[5] += 1
            if bill == 10:
                hashmap[10] += 1
                if hashmap[5] == 0:
                    return False
                else:
                    hashmap[5] -= 1
            if bill == 20:
                if hashmap[10] > 0 and hashmap[5] > 0:
                    hashmap[10] -= 1
                    hashmap[5] -= 1
                elif hashmap[5] > 2:
                    hashmap[5] -= 3
                else:
                    return False
        
        return True