from __future__ import annotations

import argparse

from jjm.main import options


def parse_args(argv, **kwargs) -> argparse.Namespace:
    parser = options.get_parser(**kwargs)
    return parser.parse_args(argv)
