"""Regression tests: a malformed settings.json must not crash the app.

`load_settings()` runs before anything else in `main()`, so any valid JSON
value that is not an object (list, string, number, ...) used to raise an
unhandled TypeError/AttributeError and abort startup with a traceback.
"""
import json
import subprocess
import sys
from pathlib import Path

REPO_DIR = Path(__file__).resolve().parent

PROBE = (
    'import sys; sys.path.insert(0, r"%s"); import main; main.load_settings();'
    ' print("TIME-LIMIT=" + str(main.settings.get("default_time_limit")))'
) % REPO_DIR


def _run_with_settings(tmp_path, payload):
    (tmp_path / 'settings.json').write_text(payload, encoding='utf-8')
    return subprocess.run(
        [sys.executable, '-c', PROBE],
        cwd=tmp_path,
        capture_output=True,
        text=True,
    )


def test_non_dict_settings_json_does_not_crash(tmp_path):
    proc = _run_with_settings(tmp_path, json.dumps([1, 2, 3]))
    assert proc.returncode == 0, proc.stderr
    assert 'Traceback' not in proc.stderr
    assert 'TIME-LIMIT=60' in proc.stdout  # built-in default kept


def test_valid_settings_json_still_loads(tmp_path):
    proc = _run_with_settings(
        tmp_path, json.dumps({'default_time_limit': 30})
    )
    assert proc.returncode == 0, proc.stderr
    assert 'TIME-LIMIT=30' in proc.stdout
