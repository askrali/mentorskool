import pandas as pd
from pandas import json_normalize
import json
import os
import cProfile, pstats
import time
 
def fetch_dataframe(filename):
    with open(filename) as f:
        data= json.load(f)
    df= json_normalize(data)
 
    time.sleep(1)
    return df
 
def main():
    path= r"C:\Users\askar.ali\Downloads\python_wrangling\bank_json_data"
    category_dataframes= {}
    for file in os.listdir(path):
        category_dataframes[file.split('.')[0]]= fetch_dataframe(os.path.join(path,file))
 
 
 
if __name__=='__main__':
    with cProfile.Profile() as profile:
        main()
   
    results= pstats.Stats(profile)
    results.sort_stats(pstats.SortKey.TIME)
    results.print_stats()