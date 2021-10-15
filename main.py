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
    # try: 
    #     name_of_csv = args[-1]
    #     assert name_of_csv.split(".")[1] == '.csv'
    # except: 
    #     print("no valid file given")
    #     #exit(1)

    parser.add_argument("--cloud",
                        help = "Generate a word cloud of most commonly types words (with some automatic filtering)",
                        action = "store_true"
                        )

    parser.add_argument("--chatnames",
                        help = "Display previous names that the chat has had",
                        action = "store_true",
                        )

    parser.add_argument("-p",
                        "--preview",
                        help = "Display less information",
                        action = "store_true",
                        )

    args = parser.parse_args(args)

    
    #gc = pd.read_csv(name_of_csv, delimiter=";",encoding="utf8",header=0,index_col="sender_name")

if __name__ == "__main__":
    main()