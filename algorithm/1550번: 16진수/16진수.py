#  **************************************************************************  #
#                                                                              #
#                                                       :::    :::    :::      #
#    Problem Number: 1550                              :+:    :+:      :+:     #
#                                                     +:+    +:+        +:+    #
#    By: shaawwert6044 <boj.kr/u/shaawwert6044>      +#+    +#+          +#+   #
#                                                   +#+      +#+        +#+    #
#    https://boj.kr/1550                           #+#        #+#      #+#     #
#    Solved: 2023/12/14 17:07:56 by shaawwert6044 ###          ###   ##.kr     #
#                                                                              #
#  **************************************************************************  #
# d 자료구조 코드 작성
d = {}

for i in range(0, 10):
  d[str(i)] = i

for i in range(ord("A"), ord("G")):
  d[chr(i)] = i-55

# d 자료구조 활용 계산
n = input()
# n의 1번째, 2번째, 3번째 ...
# 예시) AB5F1C3
# ==> 3*16**0 + C*16**1 + ... A*16**7
cnt = 0
result = 0
for i in range(len(n)-1, -1, -1):
  result += d[n[i]]*16**cnt
  cnt += 1

print(result)