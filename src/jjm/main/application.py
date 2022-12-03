from __future__ import annotations

import logging
import os
import typing

from jjm.main import options
from jjm.commands.initializer import Initializer
from jjm.commands.tester import Tester

LOGGER = logging.getLogger(__name__)


class Application:
    def __init__(self):
        self.pwd = os.path.abspath(".")

    def initialize(self, argv: typing.Sequence[str]):
        self.initializer = Initializer()
        self.tester = Tester()
        self.parser = options.prepare_main_parser(
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
