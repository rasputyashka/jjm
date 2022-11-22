from __future__ import annotations

import argparse
import logging
import os
import typing

from jjm.main import options
from jjm.defaults import (
    FIRST_IN_FILE,
    FIRST_OUT_FILE,
    IN_DIR_NAME,
    OUT_DIR_NAME,
)
from jjm.options.parse_args import parse_args

LOGGER = logging.getLogger(__name__)


class Application:
    def __init__(self):
        pass

    def initialize(self, argv: typing.Sequence[str]):
        self.initializer = Initializer()
        self.tester = Tester()
        self.parser = options.register_default_options(
            self.initializer.initialize, self.tester.run_tests
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
        args.func(args)


class Tester:
    def run_tests(self, args: argparse.Namespace):

        pass


class Initializer:
    """The class that contains everything that is needed for jjm init."""

    def __init__(self):
        self.pwd = os.path.abspath(".")

    def initialize(self, args: argparse.Namespace):
        """the main function of this class called by parser.

        Args:
            args (_type_): _description_
        """
        dirname = args.dirname
        lang = args.lang

        self._prepare_folders(dirname)
        self._prepare_files(dirname, lang)

    def _prepare_folders(self, dirname):
        """Creating tests directory.

        Created directory will contain `in` and `out` folders
        Args:
            dirname (str): directory name to be crated
        """
        in_dir_path = os.path.join(self.pwd, dirname, IN_DIR_NAME)
        out_dir_path = os.path.join(self.pwd, dirname, OUT_DIR_NAME)

        os.mkdir(dirname)
        os.mkdir(in_dir_path)
        os.mkdir(out_dir_path)

    def _prepare_files(self, dirname, lang):

        in_dir_path = os.path.join(self.pwd, dirname, IN_DIR_NAME)
        out_dir_path = os.path.join(self.pwd, dirname, OUT_DIR_NAME)

        # TODO remove harcoded constants -> add them to parser arguments
        with open(os.path.join(in_dir_path, FIRST_IN_FILE), "w") as in_file:
            in_file.write("[in]\n")

        with open(os.path.join(out_dir_path, FIRST_OUT_FILE), "w") as out_file:
            out_file.write(f"[out]\n[metadata]\n\tlanguage={lang}")
