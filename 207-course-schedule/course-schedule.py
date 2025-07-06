from collections import deque
class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        # # check if there is a cycle if so can tcomplete 
        # # prep
        # parameter: numCourse = int
        # prereqs = list of lists

        # make a graph of prerequisites
        # make a list that we can deduct as we take the prerequisites
        # Find all courses with in-degree 0 and put them in the queue.

            # While the queue isn't empty:

            # Take a course from the queue (it has no prereqs).

            # Mark it completed.

            # For each of its neighbors:

            # Decrease their in-degree by 1.

            # If their in-degree hits 0 → they're now ready → put them in the queue.
    
        graph = defaultdict(list)
        in_degree = [0] * numCourses

        for course, prereq in prerequisites:
            # print(f'course: {course}, prereq: {prereq}')
            graph[prereq].append(course)    
            in_degree[course] +=1
            # print(f'in-degree for {course}: {in_degree[course]}')
        #  {   
        #       0: [1, 2],
        #       1: [3], 
        #       2: [3]
        # }
        # [0, 1, 1, 2]
        #     i
        q = deque([])
        completed = []
        for i in range(numCourses):
            if in_degree[i] == 0:
                q.appendleft(i)
            
        while q:
            # pop it off and mark it as completed
            curr = q.pop()
            completed.append(curr)

            for neighbor in graph[curr]:
                in_degree[neighbor] -=1
                if in_degree[neighbor] == 0:
                    q.appendleft(neighbor)
                    
        return len(completed) == numCourses



                


