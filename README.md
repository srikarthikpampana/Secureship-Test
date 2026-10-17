# Secureship-Test

Deliberately vulnerable **test fixture** for [SecureShip](https://github.com/srikarthikpampana) — a
DevSecOps remediation platform. Do not use this code.

`requirements.txt` pins `jinja2==3.1.4`, which has published CVEs fixed in later releases.
SecureShip scans this repository, raises issues, proposes a tested dependency upgrade as a pull
request, and marks the finding verified only after a post-merge scan of `main` no longer reports it.

## E2 scanner fixtures (deliberately insecure)

| File | Scanner | Category |
|---|---|---|
| `requirements.txt` (`jinja2==3.1.4`) | Trivy | dependency (3 CVEs, one package-level fix) |
| `web/package-lock.json` (`lodash 4.17.20`) | Trivy | dependency (npm) |
| `Dockerfile` (`python:3.11-slim`, root user) | Trivy image, Checkov | container, iac |
| `infra/main.tf` (open SSH, unencrypted bucket) | Checkov | iac |
| `tools/run_command.py` (`shell=True`) | Semgrep | code |
| `config/deploy_key.pem` | Trivy secret | secret — **fake key, random bytes, grants nothing** |
