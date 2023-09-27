import pytest
import time
from app.jobs.time_reporter import TimeReporter

@pytest.fixture
def timer():
    return TimeReporter()

def test_init(timer):
    assert timer.elapsed_time == 0
    assert timer.start_time is not None
    assert timer.max_running_time == TimeReporter.MAX_RUNNING_SECONDS * 1e9

def test_stop(timer):
    time.sleep(1)
    timer.stop()
    assert timer.elapsed_time > 0

def test_restart(timer):
    timer.restart()
    assert timer.elapsed_time == 0
    assert timer.start_time is not None

def test_report(timer):
    timer.stop()
    assert 's' in timer.report()
    assert 'ms' in timer.report()

def test_in_time(timer):
    assert timer.in_time() is True
    timer.max_running_time = 1
    time.sleep(1)
    timer.stop()
    assert timer.in_time() is False