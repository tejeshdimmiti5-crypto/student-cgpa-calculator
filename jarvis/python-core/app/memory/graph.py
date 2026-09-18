from dataclasses import dataclass, field
from collections import defaultdict, deque
from typing import Any

@dataclass(frozen=True)
class MemoryRelation:
    source: str
    relation: str
    target: str
    metadata: dict[str,Any] = field(default_factory=dict)

class MemoryGraph:
    """Lightweight knowledge graph for entities and relationships in memory."""
    def __init__(self):
        self.adj=defaultdict(list)
        self.relations: list[MemoryRelation]=[]

    def link(self,source,relation,target,**metadata):
        edge=MemoryRelation(source,relation,target,metadata)
        self.relations.append(edge)
        self.adj[source].append(edge)
        return edge

    def neighbors(self,source,relation=None):
        return [e for e in self.adj.get(source,[]) if relation is None or e.relation==relation]

    def traverse(self,start,max_hops=2):
        seen={start}; q=deque([(start,0)]); out=[]
        while q:
            node,h=q.popleft()
            if h>=max_hops: continue
            for edge in self.adj.get(node,[]):
                if edge.target not in seen:
                    seen.add(edge.target); out.append(edge); q.append((edge.target,h+1))
        return out

    def to_context(self,start,max_hops=2):
        return [f"{e.source} --{e.relation}--> {e.target}" for e in self.traverse(start,max_hops)]
