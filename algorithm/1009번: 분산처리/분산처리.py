#  **************************************************************************  #
#                                                                              #
#                                                       :::    :::    :::      #
#    Problem Number: 1009                              :+:    :+:      :+:     #
#                                                     +:+    +:+        +:+    #
#    By: shaawwert6044 <boj.kr/u/shaawwert6044>      +#+    +#+          +#+   #
#                                                   +#+      +#+        +#+    #
#    https://boj.kr/1009                           #+#        #+#      #+#     #
#    Solved: 2023/12/11 04:33:26 by shaawwert6044 ###          ###   ##.kr     #
#                                                                              #
#  **************************************************************************  #
n = int(input())

for _ in range(n):
  a, b = map(int, input().split(" "))
  d = a**b # 데이터의 총 개수

  if d % 10 == 0:
    print(10)
  else:
    print(d % 10)