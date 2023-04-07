import sys
input = sys.stdin.readline

n,mod = map(int,input().split())
array = list(map(int,input().split()))
modular = [0] * mod #mod로 나누기 때문에 나머지가 mod 이상일 수 없음
prefix = 0

for i in range(n):
    prefix += array[i]
    modular[prefix%mod] +=1 #누적합이 mod로 나눈 나머지를 인덱스로 카운트, 나머지가 같은 경우 빼주면 mod로 나누어짐
    #ex) array = [1,2,3,1,2] mod: 3 modular = [3,2,0]
answer = modular[0] #나머지가 0인 경우는 원소 하나만으로도 mod로 나눠짐
for content in modular:
    answer += int(content*(content-1)/2) #nC2 -> 누적합 구할 때 Si- Sj라서 n개중에 두개 골라줌
print(answer)
