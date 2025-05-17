# REQ-INF-009
# REQ-INF-010

import subprocess
import pytest

# REQ-INF-010
def test_commit_message_req_id():
    """Allow merge commits without REQ-ID; enforce on authored commits only."""
    result = subprocess.run(['git', 'log', '--oneline', '-n', '1'], stdout=subprocess.PIPE)
    commit_message = result.stdout.decode('utf-8').strip()

    if commit_message.startswith("Merge"):
        return  # merge commits are exempt

    assert "REQ-" in commit_message or "REQ-INF-" in commit_message, \
        f"Commit message does not contain valid REQ-ID: {commit_message}"



# REQ-INF-010
def test_traceability_matrix_sync():
    """Test that REQ-ID from the traceability matrix matches the implemented and tested requirements."""
    with open('docs/requirements.md') as f:
        req_ids = [line.split("|")[1].strip() for line in f if "REQ-" in line]

    implemented = subprocess.run(["python", "REQ_VALIDATION_REPORT.py"], capture_output=True, text=True)
    implemented_reqs = implemented.stdout

    for req in req_ids:
        assert req in implemented_reqs, f"REQ {req} not implemented or not covered by tests."
