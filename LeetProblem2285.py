# Solution to Problem 2285 on LeetCode

class Solution(object):
    def maximumImportance(self, n, roads):
        """
        :type n: int
        :type roads: List[List[int]]
        :rtype: int
        """
        RoadMap = {} # a dictionary of how many roads is connected to each city
        for index in range(n): # for each city
            RoadMap.update({index:0}) # initialise each city having 0 road usage
        for road in roads:
            RoadMap[road[0]] += 1 # add road usage from start of road
            RoadMap[road[1]] += 1 # add road usage from end of road
        CityOrder = sorted(RoadMap, key=RoadMap.get, reverse=True) # order city based on roads
        Total = sum((n-i)*RoadMap[CityOrder[i]] for i in range(n)) # add up weighted roads
        return Total
        
        