#!/usr/bin/python3
import general_functions as general
import pandas as pd
import csv
from os import path

import sys
import argparse

name_of_csv: str

def main(args = sys.argv[1:]):
    print("start")
    parser = argparse.ArgumentParser()
    name_of_csv = args[-1]

    parser.add_argument("--cloud",
                        help = "Generate a word cloud of most commonly types words (with some automatic filtering)",
                        action = "store_true"
                        )

    parser.add_argument("--chatnames",
                        help = "Display previous names that the chat has had",
                        type = bool,
                        default = False)

    parser.add_argument("-p",
                        "--preview",
                        help = "Display less information",
                        type = bool,
                        default = False)

    args = parser.parse_args(args)

    if args.cloud:
        print("cloud works")
    print(args)
    gc = pd.read_csv(name_of_csv, delimiter=";",encoding="utf8",header=0,index_col="sender_name")

    if __name__ == "__main__":
        print("yes")
        main()