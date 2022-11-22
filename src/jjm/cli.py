"""cli implementation of jjm"""
from __future__ import annotations

import typing
import sys

from jjm.main.application import Application


def main(argv: typing.Sequence[str] | None = None) -> int:
    if argv is None:
        argv = sys.argv[1:]

    app = Application()
    app.run(argv)
