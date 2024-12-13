### About
`jjm` is a cli tool that simplifies testing your code against input samples from leetcode-like services. This works kind of like online judgment systems: provide input samples, answers and test your code. 

### NOTE: works only for python now.

### Some details for current version (0.1.2)
The commands are:
```
$ jjm --help                                                                                     
usage: jjm [-h] {init,test,gen_in,sample,run} ...

positional arguments:
  {init,test,gen_in,sample,run}
    init                create and initialize problem's working directory.
    test                run code and compare answer from test case files with program's results.
    gen_in              generate test case file(s).
    sample              show the sample of the test case file.
    run                 run the code. Results are stored in 'out' folder.

options:
  -h, --help            show this help message and exit

```
`init <name>` generates the problem's directory with `cases` and `out` directories. `out` directory is used only for the jjm itself (previous results of running your solution are stored in here).

`run <file>` runs your code with data given in test_case `.toml` files in `cases` folder

`test <file>` runs the program against cases in `cases` folder and compares results.

`gen_in <list of filenames> `generates specified test files in `cases` folder. Extensions are ignored (i.e `jjm gen_in 1.toml ` Would produce 1.toml.toml file with default config. See `jjm sample`).

`sample` prints basic sample for a test_case file

```
$ jjm sample
#  this is the example of case file
#  .toml format
[main]
in = ""
out = "?"  # ? - output is not specified
time = 1   # TLE timeout. Optional (1 is default) 
```

## Installing
I haven't uploaded jjm to PyPI, you can install it via `pip` or `pipx` (which i prefer for CLIs):
```sh
git clone https://github.com/rasputyashka/jjm.git jjm
cd jjm
pipx install .  # see how to install pipx
```

## Usage example

```sh
$ jjm init day7 example myinput wa_example  # for demo, i won't edit myinput (it will contain default values)
$ cd day7
$ echo "print(int(input()) * 2)" > sol.py   
$ nvim cases/example.toml # edit in="12", out="24"
$ nvim cases/wa_example.toml # edit in="12", out="24"
$ jjm test sol.py
example.toml - AC
myinput.toml - Output Not Specified
wa_example.toml - WA
Expected: 23
Got:      24
# cat out/myinput if you want to see the answer in case you haven't specified it.
```
