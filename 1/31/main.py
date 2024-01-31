#Data dictionary: Shows you what you're going to see
#series is a list of data
#df = data frame
import pandas as pd

df = pd.read_csv(filepath_or_buffer="hd2022.csv", encoding='latin1')
print(df)
print(df.columns)
print(df.shape)
# print(df['UNITID'])
# print(type(df['UNITID']))
# print(len(df['UNITID']))
print(df['INSTNM'])
print(df[df['INSTNM']=='Stetson University']) #will not display which rows that don't correlate to what you're looking for