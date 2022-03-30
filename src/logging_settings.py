import os
import logging
from logging import Handler, LogRecord

logging.basicConfig(
    format="%(asctime)s | %(filename)s | %(levelname)s | %(message)s",
    datefmt="%Y-%m-%d %H:%M:%S",
    filename="logs.txt",
    level=logging.INFO
)

formatter = logging.Formatter("%(asctime)s | %(filename)s | %(levelname)s | %(message)s")

console = logging.StreamHandler()
console.setLevel(logging.INFO)
console.setFormatter(formatter)

file = logging.FileHandler(filename="secondary_logs.txt")
file.setLevel(logging.ERROR)
file.setFormatter(formatter)


class DrawFilter(logging.Filter):
    def filter(self, record):
        return not (record.msg.startswith("Battle") and record.msg.endswith("0"))


root_logger = logging.getLogger("")
root_logger.addHandler(console)
root_logger.addHandler(file)
root_logger.addFilter(DrawFilter())