# -*- coding: utf-8 -*-
"""
Created on Sat Oct 15 12:23:18 2022

@author: Negative
"""

import glassdoor_scraper as gs
import pandas as pd
path = "E:/DataScience_Projects/ds_salary_proj/chromedriver"

df = gs.get_jobs('data scientist',1000, False, path, 15)

df.to_csv('glassdoor_jobs.csv', index = False)

