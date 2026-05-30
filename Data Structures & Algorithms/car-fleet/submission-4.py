class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        fleets = []
        count = 0
        curr_fleet = -1
        pos_speed = sorted(zip(position, speed), key=lambda x: x[0], reverse=True)
        time = [(target-pos) / speed for pos, speed in pos_speed]

        for t in time:
            if t > curr_fleet:
                fleets.append(t)
                curr_fleet = max(curr_fleet, t)
                count += 1

        return count