#  **************************************************************************  #
#                                                                              #
#                                                       :::    :::    :::      #
#    Problem Number: 15552                             :+:    :+:      :+:     #
#                                                     +:+    +:+        +:+    #
#    By: shaawwert6044 <boj.kr/u/shaawwert6044>      +#+    +#+          +#+   #
#                                                   +#+      +#+        +#+    #
#    https://boj.kr/15552                          #+#        #+#      #+#     #
#    Solved: 2023/08/11 09:13:02 by shaawwert6044 ###          ###   ##.kr     #
#                                                                              #
#  **************************************************************************  #
import sys
# t = int(intput().split())
t = int(sys.stdin.readline())
for _ in range(t):
    # a,b = map(int, sys.stdin.readline().split())
    a,b = map(int, sys.stdin.readline().split())
    print(a+b)