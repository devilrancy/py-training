#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Dec 25 11:48:20 2018

@author: Naresh Surisetty (a.k.a devilrancy)
"""

import pandas as pd
from fuzzywuzzy import fuzz
import logging
import os

logFormatter = logging.Formatter("%(asctime)s [%(threadName)-12.12s] [%(levelname)-5.5s]  %(message)s")
logger = logging.getLogger()
logPath = os.path.join(os.curdir, "logs")
fileName = "fuzzywuzzy"

fileHandler = logging.FileHandler("{0}/{1}.log".format(logPath, fileName))
fileHandler.setFormatter(logFormatter)
logger.addHandler(fileHandler)

consoleHandler = logging.StreamHandler()
consoleHandler.setFormatter(logFormatter)
logger.addHandler(consoleHandler)

def get_best_match(filename, name):
    df = pd.read_csv(filename)
    logger.info(df)
    print(df)
    df["Accuracy"] = df.apply(lambda row: fuzz.token_sort_ratio(row['Booking.com'], 'Deluxe Room, 1 King Bed'), axis=1)
    df = df.sort_values("Accuracy", ascending=False)
    logger.info(df)
    print(df)
    return df["Booking.com"].iloc[0] ,df["Accuracy"].iloc[0]

match, accuracy = get_best_match("room_type.csv", "Deluxe Room, 1 King Bed")
print(match, accuracy)
