class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        courseGraph = {i: [] for i in range(numCourses)}
        for crs, preq in prerequisites:
            courseGraph[crs].append(preq)
        
        # ordering is providing output as well as visit set role at same time
        ordering = []
        visiting = set()

        def dfs(course):
            prequis = courseGraph[course]
            if course in ordering:
                return True
            if course in visiting:
                return False

            if prequis == []:
                ordering.append(course)                
            
            visiting.add(course)

            for p in prequis:
                if dfs(p) == False:
                    return False
            
            visiting.remove(course)
            ordering.append(course)
            return True

        for c in range(numCourses):
            if dfs(c) == False:
                return []
            
        return ordering