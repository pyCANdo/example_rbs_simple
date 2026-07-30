from datetime import datetime
from pathlib import Path

from pyrbs import BusLogger, PyRbs


rbs = PyRbs()

log_file = Path("default") / f"first-steps-{datetime.now():%Y-%m-%d_%H-%M-%S}.mf4"
bus_logger: BusLogger = rbs.buslog.add(
    "first_steps_log",
    log_file,
)


@rbs.on_start()
def start_logging():
    print(f"Logging CAN traffic to {log_file}")
    bus_logger.start()


@rbs.on_stop()
def stop_logging():
    bus_logger.stop()
