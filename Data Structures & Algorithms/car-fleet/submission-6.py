class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        position_speed_map = {}
        stack = []

        for i, pos in enumerate(position):
            position_speed_map[pos] = i

        position.sort(reverse = True)

        for i, pos in enumerate(position):
            time = (target - pos) / speed[position_speed_map[pos]]

            if not stack or time > stack[-1]:
                stack.append(time)

        return len(stack)