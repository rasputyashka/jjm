from __future__ import annotations
import typing

import argparse


def register_default_options(initializer, tester) -> argparse.ArgumentParser:
    """Register the default options.

    These options include:


    """
    parser = argparse.ArgumentParser(add_help=False)

    subparsers = parser.add_subparsers()

    init_parser = subparsers.add_parser("init")
    test_parser = subparsers.add_parser("run")

    init_parser.add_argument("dirname")
    init_parser.add_argument("lang")
    init_parser.set_defaults(func=initializer)

    test_parser.set_defaults(func=tester)

    return parser
