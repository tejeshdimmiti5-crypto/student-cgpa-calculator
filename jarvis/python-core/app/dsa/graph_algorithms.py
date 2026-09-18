from collections import deque
import heapq

def bfs(graph: dict[str,list[str]], start: str) -> list[str]:
    seen={start}; q=deque([start]); order=[]
    while q:
        node=q.popleft(); order.append(node)
        for nxt in graph.get(node,[]):
            if nxt not in seen: seen.add(nxt); q.append(nxt)
    return order

def dfs(graph: dict[str,list[str]], start: str) -> list[str]:
    seen=set(); stack=[start]; order=[]
    while stack:
        node=stack.pop()
        if node in seen: continue
        seen.add(node); order.append(node)
        stack.extend(reversed(graph.get(node,[])))
    return order

def dijkstra(graph: dict[str,list[tuple[str,float]]], start: str) -> dict[str,float]:
    dist={start:0.0}; heap=[(0.0,start)]
    while heap:
        cost,node=heapq.heappop(heap)
        if cost!=dist.get(node): continue
        for nxt,weight in graph.get(node,[]):
            new=cost+weight
            if new<dist.get(nxt,float("inf")):
                dist[nxt]=new; heapq.heappush(heap,(new,nxt))
    return dist
