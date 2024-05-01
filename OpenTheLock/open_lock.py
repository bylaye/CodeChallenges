from typing import *
from collections import defaultdict

class OpenLock:
    """
    Class to solve the Open Lock Problem in a numeric wheel game.
    """

    def __init__(self, deadends:List[str], target: str, first="0000"):
        """
        Initializes an instance of the OpenLock class.

        Args:
            deadends (List[str]): A list of strings representing the states of blocked locks.
            target (str): A string representing the target state of the lock.
        """
        self.deadends = set(deadends)
        self.target = target
        self.first = first
        self.count = -1
        self.paths = []

    
    def neighbors(self, state: str) -> List[str]:
        """
        Returns a list of possible neighboring states for the lock by turning the wheels.

        Args:
            state (str): A string representing the current state of the lock.

        Returns:
            List[str]: A list of strings representing possible neighboring states.
        """
        lock = [char for char in state]
        n = len(lock)
        out = []
        
        for i in range(n):
            digit = int(lock[i])

            wheel_up = str((digit + 1) % 10)
            lock[i] = wheel_up
            state_up = ''.join(lock)

            wheel_down = str((digit - 1 ) % 10)
            lock[i] = wheel_down
            state_down = ''.join(lock)

            lock[i] = str(digit)
            
            if state_up not in self.deadends:
                out.append(state_up)
            if state_down not in self.deadends:
                out.append(state_down)

        return out
    

    def bfs(self):
        """
        Breadth-First Search (BFS) algorithm to find the minimum number of moves required
        to reach the target state of the lock from the initial state.
        """
        queue = [(self.first, 0)]
        visited = {self.first: self.first}

        while queue:
            lock, level = queue.pop(0)
            if lock == self.target:
                self.count = level
                self.paths = self.wheels(visited=visited)
                break
            neighbors_locks = self.neighbors(lock)

            for code  in neighbors_locks:
                if code not in visited:
                    visited[code] = lock
                    queue.append((code, level+1))


    def wheels(self, visited:{str: str}) -> List[str]: # type: ignore
        out = []
        if self.count != -1:
            code = self.target
            out.append(code)
            
            while code != self.first:
                out.insert(0, visited[code])
                code = visited[code]

        return out


    def result(self):
        self.bfs()
        print(self.paths)
        return self.count