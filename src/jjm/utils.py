from __future__ import annotations

import argparse

SAMPLE_TEXT = """#  this is the MRE of case_file
#  the extension of file must be .toml
[main]
in = ""
out = ""
"""


def display_sample(_: argparse.Namespace):

    print(SAMPLE_TEXT)
