![Pipenv-Python](https://img.shields.io/github/pipenv/locked/python-version/kwzrd/advent-of-code?label=Python&style=flat-square)
![Github-Workflow-Status](https://img.shields.io/github/workflow/status/kwzrd/advent-of-code/Flake8%20&%20friends/master?label=Flake8%20%26%20friends&style=flat-square)

# Advent of Code

My solutions to the **2020 [Advent of Code](https://adventofcode.com/)** event, using **Python 3.8** with **[Pipenv](https://github.com/pypa/pipenv)** for dependency management.

Use Pipenv to reproduce the Python environment:
```
pipenv sync
```

Then run solutions for a specific day:
```
pipenv run day 1
```

This will load input data from [inputs.json](aoc/inputs.json) and pass it to the solution.
