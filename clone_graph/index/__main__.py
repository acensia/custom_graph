import argparse
from .cli import index_cli

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--init",
        help="",
        action="store_true"
    )
    parser.add_argument(
        "--root",
        help="Root dir of your project",
        type=str,
    )


    args = parser.parse_args()

    index_cli(
        init=args.init or False,
        root=args.root or "./"
    )