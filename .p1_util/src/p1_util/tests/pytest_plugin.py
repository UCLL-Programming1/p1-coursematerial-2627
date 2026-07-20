import pytest


@pytest.hookimpl(hookwrapper=True, tryfirst=True)
def pytest_terminal_summary(terminalreporter):
    """Show details for the first failed test only; count the others."""
    failed = terminalreporter.stats.get("failed", [])
    hidden = len(failed) - 1
    if hidden > 0:
        terminalreporter.stats["failed"] = failed[:1]
    yield
    if hidden > 0:
        terminalreporter.stats["failed"] = failed  # restore, so the final count is right
        tests = "test" if hidden == 1 else "tests"
        terminalreporter.write_line(f"Failure details only shown for first failed test. {hidden} more {tests} failed.")
