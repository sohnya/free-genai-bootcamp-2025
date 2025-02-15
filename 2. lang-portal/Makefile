.PHONY: install run dev test lint format seed

install:
	cd backend_python && uv sync

run:
	cd backend_python && PYTHONPATH=src uvicorn language_learning_api.main:app --reload --host 0.0.0.0 --port 8000

test:
	cd backend_python && pytest

lint:
	cd backend_python && ruff check .

format:
	cd backend_python && ruff format .

seed:
	cd backend_python && PYTHONPATH=src python -m language_learning_api.db.seeds.seed
