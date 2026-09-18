from dataclasses import dataclass

@dataclass(frozen=True)
class AgentVote:
    agent: str
    answer: str
    confidence: float

def weighted_consensus(votes: list[AgentVote]) -> tuple[str,float]:
    if not votes:
        return "",0.0
    scores={}
    for vote in votes:
        scores[vote.answer]=scores.get(vote.answer,0.0)+max(0.0,min(1.0,vote.confidence))
    answer=max(scores,key=scores.get)
    total=sum(scores.values())
    return answer,(scores[answer]/total if total else 0.0)
