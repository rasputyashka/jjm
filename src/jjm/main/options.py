from __future__ import annotations

from typing import Sequence, Callable
import argparse

from jjm.utils import display_sample


def prepare_main_parser(
    initializer, runner, tester, generator
) -> argparse.ArgumentParser:
    """Registers the default options."""
    parser = argparse.ArgumentParser(add_help=True)

    subparsers = parser.add_subparsers()

    _configure_init_parser(subparsers, initializer)
    _configure_test_parser(subparsers, tester)
    _configure_gen_in_parser(subparsers, generator)
    # using 'hardchosen' display_sample function so far
    _configute_info_parser(subparsers, display_sample)
    _configute_run_parser(subparsers, runner)

    return parser


def _configure_test_parser(
    subparsers: argparse._SubParsersAction,
    default_function: Callable,
    *parents: Sequence[argparse.ArgumentParser],
):
    test_parser = subparsers.add_parser(
        "test",
        help="run code and compare answer from test case files with program's results.",
        parents=parents,
    )

    test_parser.add_argument(
        "-d",
        "--directory",
        help="path to the project directory. Default is '.'",
        required=False,
        default=".",
    )

    test_parser.add_argument(
        "source",
        help="Path to source file",
    )

    test_parser.set_defaults(func=default_function)


def _configure_init_parser(
    subparsers: argparse._SubParsersAction,
    default_function: Callable,
):
    init_parser = subparsers.add_parser(
        "init",
        help="create and initialize problem's working directory.",
    )
    init_parser.add_argument(
        "directory",
        help="name of problem's folder.",
    )

    init_parser.add_argument("filenames", nargs="*", help='generates sample files.')

    init_parser.set_defaults(func=default_function)


def _configute_run_parser(
    subparsers: argparse._SubParsersAction,
    default_function: Callable,
):
    run_parser = subparsers.add_parser(
        "run",
        help="run the code. Results are stored in 'out' folder."
    )

    run_parser.add_argument(
        "-d",
        "--directory",
        help="the project directory. Default is '.'",
        required=False,
        default=".",
    )

    run_parser.add_argument(
        "source",
        help="path to executable file",
    )

    run_parser.set_defaults(func=default_function)


def _configute_info_parser(
    subparsers: argparse._SubParsersAction,
    default_function: Callable,
):
    info_parser = subparsers.add_parser(
        "sample",
        help="show the sample of the test case file.",
    )

    info_parser.set_defaults(func=default_function)


def _configure_gen_in_parser(
    subparsers: argparse._SubParsersAction,
    default_function: Callable,
):
    gen_in_parser = subparsers.add_parser(
        "gen_in",
        help="generate test case file(s)."
    )

    gen_in_parser.add_argument(
        "-d",
        "--directory",
        help="the project directory. Default is '.'",
        required=False,
        default=".",
    )
    gen_in_parser.add_argument(
        "filenames",
        nargs="+",
    )
    gen_in_parser.set_defaults(func=default_function)
