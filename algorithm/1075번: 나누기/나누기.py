#  **************************************************************************  #
#                                                                              #
#                                                       :::    :::    :::      #
#    Problem Number: 1075                              :+:    :+:      :+:     #
#                                                     +:+    +:+        +:+    #
#    By: shaawwert6044 <boj.kr/u/shaawwert6044>      +#+    +#+          +#+   #
#                                                   +#+      +#+        +#+    #
#    https://boj.kr/1075                           #+#        #+#      #+#     #
#    Solved: 2023/12/14 23:13:23 by shaawwert6044 ###          ###   ##.kr     #
#                                                                              #
#  **************************************************************************  #
n = (int(input())//100)*100
f = int(input())

# 숫자의 뒷자리를 00으로 바꾸고,
# f로 나누어 떨어지는 수 만들기
# if 한자리 수이면 앞에 0을 붙이기

plus = 0
while n % f != 0:
  n += 1
  plus += 1

if plus < 10:
  print(f"0{plus}")
else:
  print(plus)