# rdRMM UI (FastAPI)

Lightweight FastAPI-based UI prototype for rdRMM. Includes a user dashboard, admin page, and a small JSON API for demo data.

Quick start:

```bash
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
uvicorn ui.app.main:app --reload --port 8888
# open http://localhost:8888/
```

Notes:
- Templates use Tailwind CDN for fast, polished styling.
- Static assets are available under `/ui/static` mount.
