import time

class TimeReporter:
    MAX_RUNNING_SECONDS = 3
    def __init__(self) -> None:
        self.elapsed_time = 0
        self.start_time = time.time_ns()
        self.max_running_time = self.MAX_RUNNING_SECONDS * 1e9

    def stop(self):
        self.elapsed_time = time.time_ns() - self.start_time

    def restart(self):
        self.elapsed_time = 0
        self.start_time = time.time_ns()

    def report(self):
        milliseconds_total = self.elapsed_time // 1e6
        seconds = milliseconds_total // 1000
        milliseconds = milliseconds_total % 1000

        return f'{seconds}s {milliseconds}ms'

    def in_time(self):
        if self.max_running_time is None:
            return True

        return self.elapsed_time < self.max_running_time
