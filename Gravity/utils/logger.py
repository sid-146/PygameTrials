import logging
from datetime import datetime

console = logging.getLogger("console")
console.setLevel(logging.INFO)

c_handler = logging.StreamHandler()
c_handler.setLevel(logging.INFO)

f_handler = logging.FileHandler(
    f"utils/logs/log_{datetime.now().strftime('%Y%m%d_%H%M%S')}.log", mode="w"
)
f_handler.setLevel(logging.INFO)

c_format = logging.Formatter(
    "%(asctime)s-%(name)s-%(levelname)s-%(module)s-%(funcName)s-%(lineno)d- :%(message)s"
)
f_format = logging.Formatter(
    "%(asctime)s-%(name)s-%(levelname)s-%(module)s-%(funcName)s-%(lineno)d- :%(message)s"
)

c_handler.setFormatter(c_format)
f_handler.setFormatter(f_format)


console.addHandler(c_handler)
console.addHandler(f_handler)
