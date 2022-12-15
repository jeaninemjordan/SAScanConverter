import pandas as pd
import numpy

# Import data
filepath= (r"C:\Users\hcfor\OneDrive\Desktop\Analysis_Projects\SAScanConverter\test\SAscan.csv")

# Read in data
dataframe = pd.read_csv("SAscan.csv", names=["freq"])

# Split data using ; as delimiter
dataframe=dataframe["freq"].str.split(";", expand=True)

# Name headers
dataframe.rename(columns={0:"freq", 1: "level"}, inplace=True)

# Convert freq column to double/float variable type
dataframe["freq"] = pd.to_numeric(dataframe["freq"])

dataframe["level"] = pd.to_numeric(dataframe["level"])

dataframe=dataframe.astype(float)

#Divide Freq column
dataframe["freq"]=dataframe["freq"]/1000000

# Round Freq and Level columns to respective decimal places
roundfreq= dataframe["freq"] = dataframe["freq"].round(3)

roundlevel= dataframe["level"] = dataframe["level"].round(2)

# concatenate dataframes
Updated_SAscan = pd.concat([roundfreq, roundlevel], axis= 1)

# Export new file
Updated_SAscan.to_csv(".\\newfile\\Updated_SAscan.csv", index=False)