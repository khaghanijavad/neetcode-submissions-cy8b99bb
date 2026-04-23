class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        courseGraph = {i: [] for i in range(numCourses)}
        for crs, preq in prerequisites:
            courseGraph[crs].append(preq)
        
        ordering = []
        visiting = set()

        def dfs(course):
            prequis = courseGraph[course]
            if course in ordering:
                return
            if course in visiting:
                return []

            if prequis == []:
                ordering.append(course)                
            
            visiting.add(course)

            for p in prequis:
                if dfs(p) == []:
                    return []
            
            visiting.remove(course)
            ordering.append(course)
            return ordering

        for c in range(numCourses):
            if dfs(c) == []:
                return []
            
        return ordering