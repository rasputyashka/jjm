# Local Jujment

### About
`jjm` is a cli that allows you make your own test samples and run the given tests.

### Some details for current version (0.1.1)
The commands are:
```
$ jjm --help
usage: jjm [-h] {init,run,test,sample} ...

positional arguments:
  {init,run,test,sample}
    init                Make a case_folder for a problem.
    run                 Run the code with given test cases and write the result to out folder.
    test                executes run command and compares outputs
    sample              Shows the sample of the test case file.

options:
  -h, --help            show this help message and exit

```
`init` generates the directory with `cases` and `out` directories. `out` directory is used only for the jjm itself.

`run` runs your code with data given in test_case `.toml` files in `cases` folder

`test` compares cpecified output with real output (real output is from `run` command)

`sample` prints basic sample for a test_case file
```
$ jjm sample
#  this is the example of case_file
#  .toml format
[main]
in = ""
out = "?"  # output is not specified
```

## Installing
I haven't added jjm to PyPI yet, so you can install it via `pip` or `pipx` which i prefer for other CLIs:
```sh
git clone https://github.com/rasputyashka/jjm.git jjm
cd jjm
pipx install .  # see how to install pipx
```
