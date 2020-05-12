class Solution:
    def trap(self, height: list) -> int:
        if len(height) < 3:
            return 0
        water = 0
        index = 0
        while index < len(height) and height[index] < 1:
            index += 1
        first_index = index
        index += 1
        while index < len(height):
            current_water = 0
            highest = index + 1
            if highest >= len(height):
                break
            while index < len(height) and height[index] < height[first_index]:
                current_water += (height[first_index] - height[index])
                if height[index] > height[highest]:
                    highest = index
                index += 1
            if index == len(height):
                height[first_index] = height[highest]
                return water + self.trap(height[first_index : highest + 1]) + self.trap(height[highest:])
            water += current_water
            first_index = index
            index += 1
        return water

s = Solution()
print(s.trap([0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]) == 6)
print(s.trap([4, 2, 3]) == 1)