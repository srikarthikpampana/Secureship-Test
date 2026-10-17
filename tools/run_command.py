"""Deliberately unsafe helper so Semgrep has a code finding (test fixture)."""

import subprocess


def run(command: str) -> int:
    return subprocess.run(command, shell=True, check=False).returncode
