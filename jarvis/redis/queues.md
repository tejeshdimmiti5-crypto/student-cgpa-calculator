# Redis Queue Protocol

Queues:
- jarvis:tasks:high
- jarvis:tasks:normal
- jarvis:tasks:low
- jarvis:events

Message envelope:
- task_id
- correlation_id
- agent
- priority
- attempt
- payload

Sensitive tasks must carry explicit authorization/confirmation before execution.
