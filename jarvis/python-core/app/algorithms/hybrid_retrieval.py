from dataclasses import dataclass
from math import log
from typing import Iterable

@dataclass(frozen=True)
class Candidate:
    key: str
    dense_score: float
    lexical_score: float
    recency_score: float = 0.0

def reciprocal_rank_fusion(rankings: list[list[str]], k: int = 60) -> dict[str,float]:
    scores={}
    for ranking in rankings:
        for rank,key in enumerate(ranking,1):
            scores[key]=scores.get(key,0.0)+1.0/(k+rank)
    return scores

def hybrid_rank(candidates: Iterable[Candidate], dense_weight=.55, lexical_weight=.30, recency_weight=.15):
    rows=list(candidates)
    return sorted(rows,key=lambda x:dense_weight*x.dense_score+lexical_weight*x.lexical_score+recency_weight*x.recency_score,reverse=True)
