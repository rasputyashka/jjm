from __future__ import annotations

import argparse
import os

from jjm.defaults import TEST_CASES_DIR
from jjm.utils import SAMPLE_TEXT


def make_files(args: argparse.Namespace):
    dirname = args.directory
    filenames = args.filenames
    for filename in filenames:
        with open(
            os.path.join(dirname, TEST_CASES_DIR, f"{filename}.toml"), "w"
        ) as case_file:
            case_file.write(SAMPLE_TEXT)
