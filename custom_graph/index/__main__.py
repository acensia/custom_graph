import argparse
from .cli import index_cli

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--init",
        help="",
        action="store_true"
    )


    args = parser.parse_args()

    index_cli(
        init=args.init or False
    )