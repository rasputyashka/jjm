from __future__ import annotations

from typing import Sequence, Callable
import argparse

from jjm.utils import display_sample


def prepare_main_parser(
    initializer, runner, tester, generator
) -> argparse.ArgumentParser:
    """Register the default options.

    These options include:


    """
    parser = argparse.ArgumentParser(add_help=False)

    subparsers = parser.add_subparsers()

    _configure_test_parser(subparsers, tester)
    _configure_init_parser(subparsers, initializer)
    _configute_run_parser(subparsers, runner)
    _configure_gen_in_parser(subparsers, generator)
    # using 'hardchosen' display_sample function so far
    _configute_info_parser(subparsers, display_sample)

    return parser


def _configure_test_parser(
    subparsers: argparse._SubParsersAction,
    default_function: Callable,
    *parents: Sequence[argparse.ArgumentParser],
):
    test_parser = subparsers.add_parser(
        "test",
        help="Check whether test case's out equals to the program's out.",
        parents=parents,
    )

    test_parser.add_argument(
        "-d",
        "--directory",
        help="Path to the project directory. Default is '.'",
        required=False,
        default=".",
    )

    test_parser.add_argument(
        "source",
        help="Path to exexutable file",
    )

    test_parser.set_defaults(func=default_function)


def _configure_init_parser(
    subparsers: argparse._SubParsersAction,
    default_function: Callable,
):
    init_parser = subparsers.add_parser(
        "init",
        help="Make a case_directory for a problem.",
    )
    init_parser.add_argument(
        "dirname",
        help="Name of a problem",
    )

    init_parser.set_defaults(func=default_function)


def _configute_run_parser(
    subparsers: argparse._SubParsersAction,
    default_function: Callable,
):
    run_parser = subparsers.add_parser(
        "run",
        help="Run the code with given test cases and write the result "
        + "to out directory.",
    )

    run_parser.add_argument(
        "-d",
        "--directory",
        help="The project directory. Default is '.'",
        required=False,
        default=".",
    )

    run_parser.add_argument(
        "source",
        help="Path to exexutable file",
    )

    run_parser.set_defaults(func=default_function)


def _configute_info_parser(
    subparsers: argparse._SubParsersAction,
    default_function: Callable,
):
    info_parser = subparsers.add_parser(
        "sample",
        help="Shows the sample of the test case file.",
    )

    info_parser.set_defaults(func=default_function)


def _configure_gen_in_parser(
    subparsers: argparse._SubParsersAction,
    default_function: Callable,
):
    gen_in_parser = subparsers.add_parser(
        "gen_in",
        help="Produces files filled with result of "
        + "`jjm sample` in `cases` directory.",
    )

    gen_in_parser.add_argument("dirname", help="The directory of a problem.")
    gen_in_parser.add_argument(
        "filenames",
        nargs="+",
    )
    gen_in_parser.set_defaults(func=default_function)
