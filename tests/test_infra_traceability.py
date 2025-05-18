# REQ-INF-001, REQ-INF-003, REQ-INF-004, REQ-INF-005, REQ-INF-006, REQ-INF-009, REQ-INF-010

import subprocess
import os
import pytest

# REQ-INF-002
def test_commit_message_enforcer_blocks_missing_req():
    from COMMIT_REQUIREMENT_ENFORCER import is_commit_message_valid
    assert not is_commit_message_valid("fix: forgot tag")

# REQ-INF-010
def test_commit_message_req_id():
    """Ensure authored commit messages include a valid REQ-ID, skip merges."""
    import subprocess

    # Get last 5 commits to be more tolerant in PR/Merge CI builds
    result = subprocess.run(
        ['git', 'log', '--pretty=%s', '-n', '5'],
        stdout=subprocess.PIPE,
        text=True,
    )
    commit_messages = result.stdout.strip().splitlines()

    for msg in commit_messages:
        if msg.startswith("Merge"):
            continue
        assert "REQ-" in msg or "REQ-INF-" in msg, \
            f"Commit message does not contain valid REQ-ID: {msg}"
        break  # test passed on first authored commit

# REQ-INF-010
def test_traceability_matrix_sync():
    """Validate that all REQ-IDs from requirements.md are mentioned in the validation report output."""
    with open('docs/requirements.md') as f:
        req_ids = [line.split("|")[1].strip() for line in f if "REQ-" in line]

    report = subprocess.run(["python", "REQ_VALIDATION_REPORT.py"], capture_output=True, text=True)
    output = report.stdout

    for req in req_ids:
        assert req in output, f"REQ {req} missing from REQ_VALIDATION_REPORT output."

# REQ-INF-001
def test_ci_yaml_includes_trigger_and_coverage_step():
    """Check if ci.yml includes push/pull_request triggers and coverage checks."""
    ci_file = ".github/workflows/ci.yml"
    assert os.path.exists(ci_file), "CI config file not found."

    with open(ci_file) as f:
        content = f.read()

    # Accept both short-form or long-form trigger syntax
    assert (
        "on: [push, pull_request]" in content
        or ("push:" in content and "pull_request:" in content)
    ), "Missing CI trigger events."

    assert "REQ_VALIDATION_REPORT.py" in content, "Missing REQ validation step."

# REQ-INF-004
def test_coverage_threshold_enforced():
    """Ensure CI enforces a minimum 100% coverage rule."""
    with open(".github/workflows/ci.yml") as f:
        content = f.read()
        assert "--fail-under=100" in content, "Coverage threshold enforcement missing."

# REQ-INF-005, REQ-INF-006
def test_branch_protection_is_documented():
    """Check if branch protection logic is declared or acknowledged."""
    readme_file = "README.md"
    with open(readme_file, errors="ignore") as f:
        text = f.read().lower()
        assert "branch protection" in text or "ci enforcement" in text, \
            "Branch protection rules not documented in README."
