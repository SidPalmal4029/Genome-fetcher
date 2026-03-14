#!/usr/bin/env python3

import argparse
from commands.transfer import run_transfer


def main():

    parser = argparse.ArgumentParser()

    sub = parser.add_subparsers(dest="command")

    transfer = sub.add_parser("transfer")

    transfer.add_argument("mode", choices=["send", "fetch"])
    transfer.add_argument("src")
    transfer.add_argument("dst")
    transfer.add_argument("--config", default="config.json")

    args = parser.parse_args()

    if args.command == "transfer":

        run_transfer(args)


if __name__ == "__main__":
    main()
