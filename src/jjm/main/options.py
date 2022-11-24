from __future__ import annotations

import argparse

from jjm.utils import display_sample


def register_default_options(
    initializer, runner, tester
) -> argparse.ArgumentParser:
    """Register the default options.

    These options include:


    """
    parser = argparse.ArgumentParser()

    subparsers = parser.add_subparsers()

    init_parser = subparsers.add_parser(
        "init",
        help="Make a case_folder for a problem.",
    )
    run_parser = subparsers.add_parser(
        "run",
        help="Run the code with given test cases and write the result "
        + "to out folder.",
    )
    test_parser = subparsers.add_parser(
        "test",
        help="Check whether test case's out equals to the program's out.",
    )
    info_parser = subparsers.add_parser(
        "sample",
        help="Shows the sample of the test case file.",
    )

    init_parser.add_argument(
        "dirname",
        help="Name of a problem",
    )
    init_parser.set_defaults(func=initializer)

    run_parser.add_argument(
        "dirname",
        help="Directory of a problem, may be '.'",
    )
    run_parser.add_argument(
        "program_file",
        help="Executable source code. Currently support only python files",
    )
    run_parser.set_defaults(func=runner)

    test_parser.add_argument(
        "dirname",
        help="Directory of a problem, may be '.'",
    )
    test_parser.set_defaults(func=tester)

    info_parser.set_defaults(func=display_sample)

    return parser
