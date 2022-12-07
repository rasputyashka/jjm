from __future__ import annotations

import argparse
import os

from jjm.defaults import TEST_CASES_DIR
from jjm.utils import SAMPLE_TEXT


class InputCaseGenerator:
    def __init__(self, pwd):
        self.pwd = pwd

    def make_files(self, args: argparse.Namespace):
        dirname = args.dirname
        filenames = args.filenames
        for filename in filenames:
            with open(
                os.path.join(dirname, TEST_CASES_DIR, filename + ".toml"), "w"
            ) as case_file:
                case_file.write(SAMPLE_TEXT)
