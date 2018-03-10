class Solution(object):
    def helper(self, i, j, board, word, idx, visited):
        if i < 0 or i >= len(board) or j < 0 or j >= len(board[0]) or not (i, j) in visited or board[i][j] != word[idx]:
            return False
        if idx == len(word) - 1:
            return True
        visited.add((i, j))
        for d in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
            x, y = i + d[0], j + d[1]
            if self.helper(x, y, board, word, idx + 1, visited):
                return True
        visited.remove((i, j))
        return False
    def exist(self, board, word):
        """
        :type board: List[List[str]]
        :type word: str
        :rtype: bool
        """
        m, n = len(board), len(board[0])
        for i in range(m):
            for j in range(n):
                if board[i][j] == word[0]:
                    visited = set()
                    if self.helper(i, j, board, word, 0, visited):
                        return True
        return False
s = Solution()
#s.exist([["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]] "ABCCED")
print(s.exist([['A'], ['B']], 'AB'))
