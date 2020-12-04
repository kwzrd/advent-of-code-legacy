import importlib
import json
import logging
import sys
import typing as t
from datetime import datetime
from pathlib import Path
from types import ModuleType

INPUTS = Path("aoc", "inputs.json")

log = logging.getLogger(__name__)


def get_data(name: str) -> t.Optional[str]:
    """
    Read input data from `INPUTS` based on `name`.

    None if `name` isn't present in the `INPUTS` file.
    """
    with INPUTS.open(mode="r", encoding="UTF-8") as inputs:
        all_data: t.Dict[str, str] = json.load(inputs)

    return all_data.get(name)


def get_module(name: str) -> t.Optional[ModuleType]:
    """
    Import module from `SOLUTIONS` based on `name`.

    The module is additionally verified to ensure that it provides a 'main' function. If this does
    not hold, we log an error & return None.
    """
    dotted_path = f"aoc.solutions.{name}"

    try:
        module = importlib.import_module(dotted_path)
    except ModuleNotFoundError:
        log.error(f"Module {name!r} does not exist")
        return

    if not (hasattr(module, "main") and callable(module.main)):
        log.error(f"Module {name!r} does not have a 'main' function")
        return

    log.info(f"Module loaded & verified: {name!r}")
    return module


def main() -> None:
    """
    Run solution for chosen day.

    The program first initializes via the following steps:
        * Acquire day number from command line arguments
        * Read input data for the chosen day
        * Import module for the chosen day

    Since the module is imported dynamically & there is no guarantee that it exists and provides
    the required 'main' function, the primary purpose of this function is error handling.

    Once the solution is initialized, it receives the input data as a sole argument and is expected
    to return a 2-tuple with solutions to the two problems.
    """
    try:
        day_number = int(sys.argv[1])
    except IndexError:
        log.error("Day number must be provided as command line argument")
        return
    except ValueError:
        log.error("Day number must be a valid integer")
        return

    qualified_name = f"day_{day_number:0>2}"

    if (data := get_data(qualified_name)) is None:
        log.error(f"Failed to get input data for: {qualified_name!r}")
        return

    if (module := get_module(qualified_name)) is None:
        log.error(f"Failed to get solution module for: {qualified_name!r}")
        return

    start_time = datetime.utcnow()

    try:
        result_1, result_2 = module.main(data)  # noqa: We verified that it does exist :)
    except Exception as exc:
        log.exception("Solution failed with unhandled exception", exc_info=exc)
    else:
        log.info(f"Result 1: {result_1}")
        log.info(f"Result 2: {result_2}")

    runtime = datetime.utcnow() - start_time
    log.info(f"Time taken: {runtime}")


if __name__ == "__main__":
    main()
