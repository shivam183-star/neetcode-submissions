class Solution:
    def foreignDictionary(self, words: List[str]) -> str:
         
        graph = {c : set() for w in words for c in w}

        for i in range(len(words) - 1):
            w1 = words[i]
            w2 = words[i+1]
            minlen = min(len(w1), len(w2))
            if len(w1) > len(w2) and w1[:minlen] == w2[:minlen]:
                return ""

            for j in range(minlen):
                if w1[j] != w2[j]:
                    graph[w1[j]].add(w2[j])
                    break

        visited = {}
        res = []

        def dfs(c):
            if c in visited:
                return visited[c]

            visited[c] = True

            for nei in graph[c]:
                if dfs(nei):
                    return True

            visited[c] = False
            res.append(c)

        for c in graph:
            if dfs(c):
                return ""

        return "".join(res[::-1])
