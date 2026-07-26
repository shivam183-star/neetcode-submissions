class Solution:
    def accountsMerge(self, accounts: List[List[str]]) -> List[List[str]]:
        parent = [i for i in range(len(accounts))]

        def find(x):
            if parent[x] != x:
                parent[x] = find(parent[x])
            return parent[x]
        
        def union(a, b):
            rootA = find(a)
            rootB = find(b)
            if rootA != rootB:
                parent[rootB] = rootA
        
        emails = {}

        for i, account in enumerate(accounts):
            for email in account[1:]:
                if email in emails:
                    union(i, emails[email])
                else:
                    emails[email] = i
        
        merged = defaultdict(list)

        for email, account in emails.items():
            root = find(account)
            merged[root].append(email)
        
        res = []

        for root, emails in merged.items():
            res.append([accounts[root][0]] + sorted(emails))
        return res