class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        graph = defaultdict(list)

        for u, v in tickets:
            graph[u].append(v)

        res = []
        for u in graph:
            graph[u].sort(reverse=True)

        def dfs(curr):
            while graph[curr]:
                next = graph[curr].pop()
                dfs(next)
            res.append(curr)

        dfs("JFK")

        return res[::-1]