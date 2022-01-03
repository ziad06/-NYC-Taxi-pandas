#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""

@author: ziad
"""

# open terminal and pass  python file.py and argumnts


# import libraries
import pandas as pd
import sys

# inter the paths of the datasets 
path_df = sys.argv[1]
path_zone = 'taxi+_zone_lookup.csv'
# read datasets
df = pd.read_csv(path_df)
df_zone = pd.read_csv(path_zone)

# merge dataset
df_merge = pd.merge(df,df_zone, left_on='DOLocationID',  right_on='LocationID')
# calculate percentile 0.95

value = df_merge.trip_distance.quantile(0.95) 
#filter the dataframe depend on the trip distance that exceed the percentile 0.95

df_merge = df_merge[df_merge.trip_distance >= value]

# groupBy the dataframe and calculate the number of trips
# sort the results from the greatest number of trips to the smallest number of trips
# return the greatest 10 number of trips
s=df_merge.groupby(['Zone','Borough']).size().reset_index().sort_values(by=0,ascending=False).head(10)
s=s.rename(columns={0: "trips","Borough":"end_borough","Zone":"end_zone"})
print(s.to_string(index=False))

