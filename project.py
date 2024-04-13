""""
小蓝正在和朋友们玩一种新的连连看游戏。在一个 n × m 的矩形网格中，
每个格子中都有一个整数，第 i 行第 j 列上的整数为 Ai, j 。玩家需要在这个网
格中寻找一对格子 (a, b) − (c, d) 使得这两个格子中的整数 Aa,b 和 Ac,d 相等，且
它们的位置满足 |a − c| = |b − d| > 0 。请问在这个 n × m 的矩形网格中有多少对
这样的格子满足条件:
1.输入的第一行包含两个正整数 n, m ，用一个空格分隔。
接下来 n 行，第 i 行包含 m 个正整数 Ai,1, Ai,2, · · · , Ai,m ，相邻整数之间使
用一个空格分隔
2.输出一行包含一个整数表示答案。

"""
""""
n, m = map(int, input().split())
a = [list(map(int, input().split())) for i in range(n)]
d = {}
for i in range(n):
    for j in range(m):
        if a[i][j] not in d:
            d[a[i][j]] = []
        d[a[i][j]].append((i, j))
ans = 0
for k in d:
    v = d[k]
    for i in range(len(v)):
        for j in range(i + 1, len(v)):
            if abs(v[i][0] - v[j][0]) == abs(v[i][1] - v[j][1]):
                ans += 1
print(ans)

"""
""""
【问题描述】
小蓝发现了一个神奇的闹钟，从纪元时间（1970 年 1 月 1 日 00:00:00 ）开
始，每经过 x 分钟，这个闹钟便会触发一次闹铃（纪元时间也会响铃）。这引起
了小蓝的兴趣，他想要好好研究下这个闹钟。
对于给出的任意一个格式为 yyyy-MM-dd HH:mm:ss 的时间，小蓝想要
知道在这个时间点之前（包含这个时间点）的最近的一次闹铃时间是哪个时间？
注意，你不必考虑时区问题。
【输入格式】
输入的第一行包含一个整数 T，表示每次输入包含 T 组数据。
接下来依次描述 T 组数据。
每组数据一行，包含一个时间（格式为 yyyy-MM-dd HH:mm:ss ）和一
个整数 x ，其中 x 表示闹铃时间间隔（单位为分钟）。
【输出格式】
输出 T 行，每行包含一个时间（格式为 yyyy-MM-dd HH:mm:ss ），依
次表示每组数据的答案。
【样例输入】
2
2016-09-07 18:24:33 10
2037-01-05 01:40:43 30
【样例输出】
2016-09-07 18:20:00
""""
""""
import datetime
nums = int(input())
for i in range(nums):
    str = input().split()
    time = datetime.datetime.strptime(str[0], "%Y-%m-%d %H:%M:%S")
    x = int(str[1])
    time = time - datetime.timedelta(minutes = time.minute % x)
    print(time.strftime("%Y-%m-%d %H:%M:%S"))
"""
import time
n = int(input())
for i in range(n):
    time_str, x = input().split()
    x = int(x)
    time_1 = time.strptime(time_str, "%Y-%m-%d %H:%M:%S")
    time_2 = int(time.mktime(time_1))
    minute = time_2 // 60
    minute = minute - minute % x
    time_2 = minute * 60
    time_1 = time.localtime(time_2)
   Time = time.strftime("%Y-%m-%d %H:%M:%S", time_1)
    print(Time）
          
          
          
"""import time
T = int(input())
for i in range(T):
    time_str, x = input().split()
    x = int(x)
    timeArray = time.strptime(time_str, "%Y-%m-%d %H:%M:%S")
    timeStamp = int(time.mktime(timeArray))
    minute = timeStamp // 60
    minute = minute - minute % x
    timeStamp = minute * 60
    Array = time.localtime(timeStamp)
    otherStyleTime = time.strftime("%Y-%m-%d %H:%M:%S", timeArray)
    print(otherStyleTime)
