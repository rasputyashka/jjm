from __future__ import annotations

import argparse


def register_default_options(
    initializer, runner, tester
) -> argparse.ArgumentParser:
    """Register the default options.

    These options include:


    """
    parser = argparse.ArgumentParser(add_help=False)

    subparsers = parser.add_subparsers()

    init_parser = subparsers.add_parser("init")
    run_parser = subparsers.add_parser("run")
    test_parser = subparsers.add_parser("test")

    init_parser.add_argument("dirname")
    init_parser.set_defaults(func=initializer)

    run_parser.add_argument("dirname")
    run_parser.add_argument("program_file")
    run_parser.set_defaults(func=runner)

    test_parser.add_argument("dirname")
    test_parser.set_defaults(func=tester)

    return parser
