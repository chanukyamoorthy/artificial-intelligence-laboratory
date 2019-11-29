# -*- coding: utf-8 -*-
"""
Created on Wed Aug 28 10:36:27 2019

@author: student
"""

inf = 1000

graph = [[inf, 1, 6, 8, 4],
         [7, inf, 8, 5, 6],
         [6, 8, inf, 9, 7],
         [8, 5, 9, inf, 8],
         [4, 6, 7, 8, inf]]

n = 5
vis = [0]
val = inf

def dfs(graph, vis, num, cost):
    global val, inf
    if len(vis) == n:
        val = min(val, cost+graph[num][0])
        return
    for i in range(n):
        if i != num and graph[num][i] != inf and i not in vis:
            vis.append(num)
            dfs(graph, vis, i, cost+graph[num][i])
            vis.pop()

dfs(graph, vis, 0, 0)

print(val)