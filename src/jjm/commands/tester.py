from __future__ import annotations

import argparse
import os
import subprocess

import toml

from jjm.defaults import OUT_DIR, TEST_CASES_DIR
from jjm.utils import get_fail_color, get_success_color, get_warn_color


class Tester:
    def __init__(self, pwd):
        self.pwd = pwd

    def process_file(self, in_file, out_file, executable):
        case_data = toml.load(in_file)
        in_data = case_data["main"]["in"]
        max_time = case_data["main"].get("time") or 5
        try:
            with open(out_file, "w") as to_file:
                subprocess.run(
                    ["python3", executable],
                    stdout=to_file,
                    timeout=max_time,
                    input=in_data,
                    text=True,
                )
        except subprocess.TimeoutExpired:
            with open(out_file, "w") as to_file:
                #  This rewrites the log
                to_file.write("TLE")

    def generate_results(self, args: argparse.Namespace):
        """Run all the test cases and save their results to out directory."""
        dirname = args.directory
        project_folder = os.path.join(os.path.abspath("."), dirname)
        test_cases_dir_path = os.path.join(project_folder, TEST_CASES_DIR)
        out_dir_path = os.path.join(project_folder, OUT_DIR)
        for case_file in os.listdir(test_cases_dir_path):
            self.process_file(
                os.path.join(test_cases_dir_path, case_file),
                os.path.join(out_dir_path, case_file.split(".")[0]),
                args.source,
            )

    def run_tests(self, args: argparse.Namespace):
        # `jjm test` has source and directory paramters
        self.generate_results(args)
        dirname = args.directory
        out_path = os.path.join(self.pwd, dirname, OUT_DIR)
        cases_dir = os.path.join(self.pwd, dirname, TEST_CASES_DIR)
        for case_file in os.listdir(cases_dir):
            case_data = toml.load(os.path.join(cases_dir, case_file))
            case_out = str(case_data["main"]["out"].rstrip())  # trailing '\n'
            if case_out == "?":
                # if ouput is not specified there is no sense in checking it
                print(f"{case_file} - {get_warn_color('Out Not Specified')}")
                continue
            with open(
                os.path.join(out_path, case_file.split(".")[0])
            ) as out_file:
                out_read = str(out_file.read().rstrip())  # trailing '\n'
                if case_out == out_read:
                    print(f"{cse_fiale} - {get_success_color('AC')}")
                elif out_read == "TLE":
                    print(f"{case_file} - {get_fail_color('TLE')}")
                else:
                    print(f"{case_file} - {get_fail_color('WA')}")
                    if "\n" in case_out or "\n" in out_read:
                        print(f"Expected:\n{case_out}")
                        print(f"Got:\n{out_read}")
                    else:
                        print(f"{'Expected: ':<10}{case_out!s}")
                        print(f"{'Got: ':<10}{out_read!s}")
