class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]):
        """
        pos = [4,1,0,7], speed = [2,2,1,1], target = 10
        pos.sort[-1] = [7,4,1,0]
        pos, speed = [(7,1), (4,2), (1,2), (0,1)]
        time = [3, 3, 5, 10]

        """
        
        pos_speed = sorted(zip(position, speed), key=lambda x: x[0], reverse=True)
        time = [-((-target+pos) // speed) for pos, speed in pos_speed]

        # return time
        return len(set(time))