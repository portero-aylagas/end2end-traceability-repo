# REQ-INF-002, REQ-INF-008, REQ-INF-009
def test_commit_message_enforcer_accepts_good_msg():
    from COMMIT_REQUIREMENT_ENFORCER import is_commit_message_valid
    assert is_commit_message_valid("fix(REQ-INF-002): test")

# REQ-INF-002, REQ-INF-009
def test_commit_message_enforcer_rejects_bad_msg():
    from COMMIT_REQUIREMENT_ENFORCER import is_commit_message_valid
    assert not is_commit_message_valid("fix: no tag here")

# REQ-INF-007, REQ-INF-010
def test_requirement_coverage_checks_against_known_reqs():
    from REQUIREMENT_COVERAGE_CHECK import check_coverage
    assert check_coverage(["REQ-001", "REQ-INF-002"], ["REQ-001", "REQ-INF-002"])