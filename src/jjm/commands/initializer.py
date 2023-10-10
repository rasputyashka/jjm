import argparse
import os

from jjm.defaults import OUT_DIR, TEST_CASES_DIR
from jjm.commands.file_generator import make_files


class Initializer:
    """The class that contains everything that is needed for jjm init."""

    def __init__(self, pwd):
        self.pwd = pwd

    def initialize(self, args: argparse.Namespace):
        """The main function of this class called by parser."""
        dirname = args.directory
        self._prepare_folders(dirname)
        make_files(args)

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
