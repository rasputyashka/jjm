from __future__ import annotations

import argparse
import logging
import os
import subprocess
import typing

import toml

from jjm.defaults import OUT_DIR, TEST_CASES_DIR
from jjm.main import options
from jjm.utils import get_fail_color, get_success_color

LOGGER = logging.getLogger(__name__)


class Application:
    def __init__(self):
        self.pwd = os.path.abspath(".")

    def initialize(self, argv: typing.Sequence[str]):
        self.initializer = Initializer()
        self.tester = Tester()
        self.parser = options.register_default_options(
            self.initializer.initialize,
            self.tester.generate_results,
            self.tester.run_tests,
        )
        self.parser.parse_args(argv)

    def run(self, argv: typing.Sequence[str]):
        try:
            self._run(argv)
        except KeyboardInterrupt as exc:
            LOGGER.critical("Caught keyboard interrupt")
            LOGGER.exception(exc)

    def _run(self, argv: typing.Sequence[str]):
        self.initialize(argv)
        args = self.parser.parse_args(argv)
        # func is a default function that executes on
        # jjm some_command. jjm sample does need a function for instance.
        if "func" in args:
            args.func(args)


class Tester:
    def generate_results(self, args: argparse.Namespace):
        # TODO refactor this stuff
        """Run all the test cases and save their results to out directory."""
        dirname = args.dirname
        path = os.path.join(os.path.abspath("."), dirname, TEST_CASES_DIR)
        for case_file in os.listdir(path):
            case_data = toml.load(os.path.join(path, case_file))
            with open(
                os.path.join(
                    os.path.abspath("."),
                    dirname,
                    OUT_DIR,
                    case_file.removesuffix(".toml"),
                ),
                "w",
            ) as out_file:
                subprocess.run(
                    ["python3", args.program_file],
                    stdout=out_file,
                    timeout=10,
                    input=case_data["main"]["in"],
                    text=True,
                )

    def run_tests(self, args: argparse.Namespace):
        dirname = args.dirname
        pwd = os.path.abspath(".")
        out_path = os.path.join(pwd, dirname, OUT_DIR)
        cases_dir = os.path.join(pwd, dirname, TEST_CASES_DIR)
        for case_file in os.listdir(cases_dir):
            case_data = toml.load(os.path.join(cases_dir, case_file))
            case_out = case_data["main"]["out"]
            with open(
                os.path.join(out_path, case_file.removesuffix(".toml"))
            ) as out_file:
                out_read = out_file.read().rstrip()  # trailing '\n'
                if case_out == out_read:
                    print(f"{case_file} - {get_success_color('OK')}")
                else:
                    print(f"{case_file} - {get_fail_color('FAILED')}")
                    print(f"Expected: {case_out!r}\nGot {out_read!r}")

        LOGGER.info("Everything is OK")


class Initializer:
    """The class that contains everything that is needed for jjm init."""

    def __init__(self):
        self.pwd = os.path.abspath(".")

    def initialize(self, args: argparse.Namespace):
        """The main function of this class called by parser."""
        dirname = args.dirname
        self._prepare_folders(dirname)

    def _prepare_folders(self, dirname):
        """Creating tests directory.

        Created directory will contain `in` and `out` folders
        Args:
            dirname (str): directory name to be crated
        """
        in_dir_path = os.path.join(self.pwd, dirname, TEST_CASES_DIR)
        out_dir_path = os.path.join(self.pwd, dirname, OUT_DIR)

        os.mkdir(dirname)
        os.mkdir(in_dir_path)
        os.mkdir(out_dir_path)
