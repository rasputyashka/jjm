from __future__ import annotations

import argparse
import enum

SAMPLE_TEXT = """#  this is the example of case file
#  .toml format
[main]
in = ""
out = "?"  # ? - output is not specified
time = 1   # TLE timeout. Optional (1 is default)
"""


class COLORS(enum.Enum):
    OKGREEN = "\033[92m"
    WARNING = "\033[93m"
    FAIL = "\033[91m"
    ENDC = "\033[0m"


def display_sample(_: argparse.Namespace) -> None:
    print(SAMPLE_TEXT)


def get_warn_color(text) -> str:
    return f"{COLORS.WARNING.value}{text}{COLORS.ENDC.value}"


def get_success_color(text) -> str:
    return f"{COLORS.OKGREEN.value}{text}{COLORS.ENDC.value}"


def get_fail_color(text) -> str:
    return f"{COLORS.FAIL.value}{text}{COLORS.ENDC.value}"
