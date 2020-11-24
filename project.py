import pandas as pd
import csv

df = pd.read_csv("total_stars.csv")

del df["Luminosity"]

df.to_csv('newfile.csv')
