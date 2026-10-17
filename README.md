# Secureship-Test

Deliberately vulnerable **test fixture** for [SecureShip](https://github.com/srikarthikpampana) — a
DevSecOps remediation platform. Do not use this code.

`requirements.txt` pins `jinja2==3.1.4`, which has published CVEs fixed in later releases.
SecureShip scans this repository, raises issues, proposes a tested dependency upgrade as a pull
request, and marks the finding verified only after a post-merge scan of `main` no longer reports it.
