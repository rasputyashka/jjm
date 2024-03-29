from __future__ import annotations

import logging
import os
import typing

from jjm.commands.file_generator import make_files
from jjm.commands.initializer import Initializer
from jjm.commands.tester import Tester
from jjm.main import options


LOGGER = logging.getLogger(__name__)


class Application:
    def __init__(self):
        self.pwd = os.path.abspath(".")

    def initialize(self, argv: typing.Sequence[str]):
        self.initializer = Initializer(self.pwd)
        self.tester = Tester(self.pwd)
        self.parser = options.prepare_main_parser(
            self.initializer.initialize,
            self.tester.generate_results,
            self.tester.run_tests,
            make_files,
        )
        self.parser.parse_args(argv)

    def run(self, argv: typing.Sequence[str]):
        try:
            self._run(argv)
        except KeyboardInterrupt:
            print("stopping...")
            LOGGER.error("Keyboard interrupt")

    def _run(self, argv: typing.Sequence[str]):
        self.initialize(argv)
        args = self.parser.parse_args(argv)
        # func is a default function that executes on
        # jjm some_command. jjm sample does need a function for instance.
        if "func" in args:
            args.func(args)
