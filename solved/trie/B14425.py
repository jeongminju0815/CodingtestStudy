class Trie:
    def __init__(self):
        self.root = {}
    def insert(self, s):
        cur_node = self.root #처음 루트로 잡아준다.
        for c in s: # 받은 문자열 하나하나에 대해서
            if c not in cur_node: #현재 노드에 그 문자가 있으면 들어가고, 그렇지 않으면 새로 만든다.
                cur_node[c] = {}
            cur_node = cur_node[c]
        cur_node["*"] = s #"*" 노드를 만들어 '단어의 끝' 표시를 해 준다.
    def search(self, s):
        cur_node = self.root
        for c in s:
            if c in cur_node:
                cur_node = cur_node[c]
            else:
                return False
        return "*" in cur_node #"*"가 해당 노드에 있으면 그 글자로 끝나는 단어가 있다는 것이다. "*"일 경우 print(cur_node)히면 최종 결과 나옴

trie = Trie()
n, m = map(int, input().split())
result = 0

for i in range(n):
    trie.insert(input())
for j in range(m):
    if trie.search(input()):
        result+=1

print(result)
