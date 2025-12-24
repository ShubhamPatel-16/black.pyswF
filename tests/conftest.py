import pytest

pytest_plugins = ["tests.optional"]

PRINT_FULL_TREE: bool = False
PRINT_TREE_DIFF: bool = True


def pytest_addoption(parser: pytest.Parser) -> None:
    parser.addoption(
        "--print-full-tree",
        action="store_true",
        default=False,
        help="print full syntax trees on failed tests",
    )
    parser.addoption(
        "--print-tree-diff",
        action="store_true",
        help="print diff of syntax trees on failed tests",
    )


def pytest_configure(config: pytest.Config) -> None:
    global PRINT_FULL_TREE
    global PRINT_TREE_DIFF
    PRINT_FULL_TREE = config.getoption("--print-full-tree")
    # PRINT_TREE_DIFF defaults to True (see initial value on line 6).
    # Since action="store_true" makes getoption() return False when the flag
    # isn't provided, we preserve the True default by only setting it if the
    # flag was explicitly provided (which means it's True).
    if config.getoption("--print-tree-diff"):
        PRINT_TREE_DIFF = True
    # Otherwise, keep the default True value (don't change PRINT_TREE_DIFF)
