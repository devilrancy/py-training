# -*- coding: utf-8 -*-
"""
Edited by Naresh Surisetty.
"""

from jira import JIRA
import logging
import os

logFormatter = logging.Formatter("%(asctime)s [%(threadName)-12.12s] [%(levelname)-5.5s]  %(message)s")
logger = logging.getLogger()
logPath = os.path.join(os.curdir, "logs")
fileName = "jiraextract"

fileHandler = logging.FileHandler("{0}/{1}.log".format(logPath, fileName))
fileHandler.setFormatter(logFormatter)
logger.addHandler(fileHandler)

consoleHandler = logging.StreamHandler()
consoleHandler.setFormatter(logFormatter)
logger.addHandler(consoleHandler)

jira = JIRA('https://jira.spring.io')

block_size = 1000
block_num = 0
allissues = []
while True:
     start_idx = block_num*block_size
     issues = jira.search_issues('project=XD', start_idx, block_size)
     if len(issues) == 0:
         break
     block_num += 1
     for issue in issues:
         print('%s: %s' % (issue.key, issue.fields.summary))
         allissues.append(issue)

print("")