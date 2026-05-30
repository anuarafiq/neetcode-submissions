class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        """
        pos = [10,8,0,5,3], speed = [2,4,1,1,3], target = 12
        -> pos = [12, ]
        pos.sort[-1] = [10,8,5,3,0]
        pos, speed = [(10,2), (8,4), (5,1), (3,3), (0,1)]
        time = [1, 1, 7, 3, 12]

        """
        
        fleets = []
        count = 0
        curr_fleet = -1
        pos_speed = sorted(zip(position, speed), key=lambda x: x[0], reverse=True)
        time = [-((-target+pos) // speed) for pos, speed in pos_speed]

        for t in time:
            if t >= curr_fleet:
                fleets.append(t)
                curr_fleet = max(curr_fleet, t)
                count += 1

        return count-1