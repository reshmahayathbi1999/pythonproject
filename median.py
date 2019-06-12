import statistics
number=int(input())
a = [int(x) for x in input().split()]
sortedlists=a.sort()
median=statistics.median(a)
print(median)
