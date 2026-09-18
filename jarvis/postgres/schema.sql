CREATE TABLE IF NOT EXISTS jarvis_memory (
    id BIGSERIAL PRIMARY KEY,
    memory_key VARCHAR(255) NOT NULL,
    memory_type VARCHAR(50) NOT NULL,
    content TEXT NOT NULL,
    importance DOUBLE PRECISION DEFAULT 0.5,
    created_at TIMESTAMPTZ NOT NULL DEFAULT NOW()
);
CREATE INDEX IF NOT EXISTS idx_jarvis_memory_key ON jarvis_memory(memory_key);
CREATE INDEX IF NOT EXISTS idx_jarvis_memory_type ON jarvis_memory(memory_type);

CREATE TABLE IF NOT EXISTS jarvis_tasks (
    id BIGSERIAL PRIMARY KEY,
    task_id VARCHAR(255) UNIQUE NOT NULL,
    goal TEXT NOT NULL,
    status VARCHAR(32) NOT NULL,
    priority INTEGER NOT NULL DEFAULT 50,
    attempts INTEGER NOT NULL DEFAULT 0,
    created_at TIMESTAMPTZ NOT NULL DEFAULT NOW(),
    updated_at TIMESTAMPTZ NOT NULL DEFAULT NOW()
);
