from pyspark import SparkContext
from pyspark.ml.recommendation import ALS
from pyspark.sql import SQLContext
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


df1 = pd.read_csv('netflix-prize-data/combined_data_1.txt', header=None, names=['user_id', 'rating', 'timestamp'])

df = df1

df_nan = pd.DataFrame(pd.isnull(df.Rating))
df_nan = df_nan[df_nan['Rating'] is True]
df_nan = df_nan.reset_index()

movie_np = []
movie_id = 1

als = ALS(rank=10,)
