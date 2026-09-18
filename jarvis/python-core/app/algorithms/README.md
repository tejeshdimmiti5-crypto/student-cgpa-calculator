# JARVIS Algorithm Layer

The algorithm layer contains deterministic building blocks used by the agent runtime.

## Retrieval
- Hybrid dense + lexical + recency ranking
- Reciprocal Rank Fusion (RRF)

## Planning
- Priority-queue best-first search
- Bounded beam search
- DAG topological execution

## Memory
- LRU cache
- Trie prefix index
- Vector similarity

## Graph
- BFS
- DFS
- Dijkstra

## Multi-agent
- Confidence-weighted consensus

These are algorithmic primitives; the LLM remains responsible for semantic interpretation where appropriate.
