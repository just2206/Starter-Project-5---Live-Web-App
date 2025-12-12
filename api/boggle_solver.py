import re
import sys
import json
from .randomGen import *
from .readJSONFile import *

class Boggle:
    def __init__(self, grid, dictionary):
        self.grid = grid
        # Normalize dictionary to lowercase for consistent matching
        self.dictionary = set(word.lower() for word in dictionary)
        # Build a prefix set for pruning during DFS
        self.prefixes = set()
        for word in self.dictionary:
            for i in range(1, len(word) + 1):
                self.prefixes.add(word[:i])
        self.rows = len(grid)
        self.cols = len(grid[0]) if self.rows > 0 else 0
        self.solutions = set() # Use a set to store unique solutions


    def is_valid(self, word):
        """Checks if a word is in the dictionary."""
        return word in self.dictionary


    def find_words(self):
        """Main method to find all valid words in the Boggle grid."""
        # Iterate through each cell of the grid
        for r in range(self.rows):
            for c in range(self.cols):
                # Start a depth-first search (DFS) from each cell
                visited = [[False for _ in range(self.cols)] for _ in range(self.rows)]
                self._dfs(r, c, "", visited)
        return sorted(list(self.solutions))


    # Public API expected by tests
    def getSolution(self):
        return self.find_words()


    def _dfs(self, r, c, current_word, visited):
        """
        Recursive helper function for the depth-first search.
        r: current row
        c: current column
        current_word: the word formed so far
        visited: a 2D list to keep track of visited cells
        """
        # Base case for invalid moves
        if not (0 <= r < self.rows and 0 <= c < self.cols and not visited[r][c]):
            return


        # Handle "Qu" special case and extend current word
        cell_char = self.grid[r][c]
        if cell_char == "Qu":
            current_word += "qu"
        else:
            current_word += cell_char.lower()


        # Prune paths that cannot lead to any dictionary word
        if current_word not in self.prefixes:
            return


        # Mark the current cell as visited
        visited[r][c] = True


        # Check if the current word is a valid solution (at least 3 characters)
        if len(current_word) >= 3 and self.is_valid(current_word):
            self.solutions.add(current_word)


        # Explore all 8 adjacent neighbors
        for dr in [-1, 0, 1]:
            for dc in [-1, 0, 1]:
                if dr == 0 and dc == 0:
                    continue
                self._dfs(r + dr, c + dc, current_word, visited)


        # Backtrack: mark the current cell as unvisited
        visited[r][c] = False




def main():
    grid = [["T", "W", "Y", "R"], ["E", "N", "P", "H"],["G", "Z", "Qu", "R"],["O", "N", "T", "A"]]
    dictionary = ["art", "ego", "gent", "get", "net", "new", "newt", "prat", "pry", "qua", "quart", "quartz", "rat", "tar", "tarp", "ten", "went", "wet", "arty", "rhr", "not", "quar"]


    mygame = Boggle(grid, dictionary)
    solutions = mygame.find_words()
    print("Found solutions:")
    for word in solutions:
        print(word)


if __name__ == "__main__":
    main()


