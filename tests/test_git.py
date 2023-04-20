import mock
import pytest
import subprocess

from src.flask_meter.git import git_stats


def raises_exception(*args, **kwargs):
    raise subprocess.CalledProcessError(1, "git log", "git: command not found")


@mock.patch("src.flask_meter.git.subprocess.check_output", raises_exception)
def test_status_exception():
    res = git_stats()
    assert res == {
        "commit": "Unknown",
        "author": "Unknown",
        "date": "Unknown",
    }
