import argparse
import os

from jjm.defaults import OUT_DIR, TEST_CASES_DIR


class Initializer:
    """The class that contains everything that is needed for jjm init."""

    def __init__(self):
        self.pwd = os.path.abspath(".")

    def initialize(self, args: argparse.Namespace):
        """The main function of this class called by parser."""
        dirname = args.dirname
        self._prepare_folders(dirname)

    def _prepare_folders(self, dirname):
        """Create tests directory.

        Created directory will contain `in` and `out` folders

        Parameters
        ----------
        dirname : str
            directory name to be created
        """
        in_dir_path = os.path.join(self.pwd, dirname, TEST_CASES_DIR)
        out_dir_path = os.path.join(self.pwd, dirname, OUT_DIR)

        os.mkdir(dirname)
        os.mkdir(in_dir_path)
        os.mkdir(out_dir_path)
