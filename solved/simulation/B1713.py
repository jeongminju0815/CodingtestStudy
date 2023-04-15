from collections import deque, defaultdict
import heapq
import sys
input = sys.stdin.readline

n = int(input())
r = int(input())
student = list(map(int, input().split()))
recomm = defaultdict(int) #학생번호: 투표수

q = []
photo = []

for i in range(len(student)):
    if student[i] in photo:
        recomm[student[i]] += 1
        continue
    if len(q) < n:
        recomm[student[i]] += 1
        heapq.heappush(q, (recomm[student[i]],i+1, student[i])) #투표수, idx+1(날짜), 학생번호
        photo.append(student[i]) #포토에 들어간 학생
    else:
        #우선순위 큐에서 꺼낸다, 투표수가 dict 투표수랑 같으면 그대로, 다르다면 계속 빼서 같을 때 까지 넣기
        vote, day, s = heapq.heappop(q)
        if vote != recomm[s]:
            while True:
                heapq.heappush(q, (recomm[s], day, s))
                vote, day, s = heapq.heappop(q)
                if vote == recomm[s]:
                    break
        recomm[s] = 0
        photo.remove(s)
        recomm[student[i]] += 1
        heapq.heappush(q, (recomm[student[i]],i+1, student[i])) #투표수, idx+1(날짜), 학생번호
        photo.append(student[i]) #포토에 들어간 학생

    # print(recomm, photo, q)
for key, value in sorted(recomm.items()):
    if value != 0:
        print(key, end=" ")
                



        

