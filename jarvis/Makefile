install:
	python -m pip install -r python-core/requirements.txt

run:
	PYTHONPATH=python-core uvicorn app.api.server:app --reload --app-dir python-core

cli:
	PYTHONPATH=python-core python python-core/app/main.py

infra:
	docker compose up -d

infra-down:
	docker compose down
