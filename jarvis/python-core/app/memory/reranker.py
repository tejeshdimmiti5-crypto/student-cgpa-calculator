import math
from datetime import datetime, timezone

def recency_score(created_at: str, half_life_hours: float = 24.0) -> float:
    try: dt=datetime.fromisoformat(created_at.replace("Z","+00:00"))
    except ValueError: return 0.0
    age=max(0.0,(datetime.now(timezone.utc)-dt).total_seconds()/3600)
    return math.exp(-math.log(2)*age/max(half_life_hours,0.001))

def rerank(results, query_terms=None):
    query_terms=set((query_terms or "").lower().split())
    scored=[]
    for item in results:
        text=str(item.get("text",item.get("value",""))).lower()
        lexical=sum(term in text for term in query_terms)/max(1,len(query_terms))
        dense=float(item.get("score",0))
        recency=recency_score(str(item.get("created_at","")))
        score=.55*dense+.30*lexical+.15*recency
        scored.append((score,item))
    return [item for _,item in sorted(scored,key=lambda x:x[0],reverse=True)]
