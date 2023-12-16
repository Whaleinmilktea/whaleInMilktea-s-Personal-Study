#  **************************************************************************  #
#                                                                              #
#                                                       :::    :::    :::      #
#    Problem Number: 1292                              :+:    :+:      :+:     #
#                                                     +:+    +:+        +:+    #
#    By: shaawwert6044 <boj.kr/u/shaawwert6044>      +#+    +#+          +#+   #
#                                                   +#+      +#+        +#+    #
#    https://boj.kr/1292                           #+#        #+#      #+#     #
#    Solved: 2023/12/17 02:46:49 by shaawwert6044 ###          ###   ##.kr     #
#                                                                              #
#  **************************************************************************  #
a, b = map(int, input().split(" "))

seq = []

for i in range(1, 46):
  for _ in range(i):
    seq.append(i)

print(sum(seq[a-1:b]))