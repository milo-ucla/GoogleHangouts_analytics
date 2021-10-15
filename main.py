#!/usr/bin/env python3
import general_functions as util
import pandas as pd
import matplotlib.pyplot as plt
import csv
from os import path

import sys
import argparse

name_of_csv: str

def main(args = sys.argv[1:]):

    parser = argparse.ArgumentParser()
    # try: 
    name_of_csv = 'groupchat_modified.csv'
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

    ##############################

    gc = pd.read_csv(name_of_csv,encoding="utf8",header=0,dtype = {'message':'object'})
    plt.plot([1,2,3,4], [1,2,3,4])
    plt.show()
    #print(gc.message_type.unique())

    if (args.cloud):
        util.generateWordCloud(gc)
    if(args.chatnames):
        print(util.getPreviousChatNames(gc))
    if(args.preview):
        print(util.getUserChatFrequencies(gc))
    # else:
    #     print("User Chat Freq. Preview", util.getUserChatFrequencies(gc))
    #     print("Word Count by Individual", util.getUserWordCount(gc))
    #     print("User Words Per Message Average", util.getUserWordsPerMessage(gc))

if __name__ == "__main__":
    main()