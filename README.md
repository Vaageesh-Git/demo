# Dummy Vulnerable Repo - exi
Small intentionally vulnerable Python service for testing Vuln-Swarm end-to-end.
## Included Vulnerabilities

- `TRB-001`: unsafe `eval(...)`
- `TRB-002`: unsafe `yaml.load(...)`
- `CFG-003`: wildcard CORS origin
- `CFG-004`: debug mode enabled
- `DEP-003`: unpinned dependencies in `requirements.txt`
- `DEP-004`: missing dependency hashes in `requirements.txt`

## Files

- `app.py`: vulnerable FastAPI app
- `requirements.txt`: intentionally unpinned dependencies

## Run ##
```bash
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
uvicorn app:app --reload
```
