#Data dictionary: Shows you what you're going to see
#series is a list of data
#df = data frame
import pandas as pd
import rich

df = pd.read_csv(filepath_or_buffer="hd2022.csv", encoding='latin1')
# print(df)
# print(df.columns)
# print(df.shape)
# # print(df['UNITID'])
# # print(type(df['UNITID']))
# # print(len(df['UNITID']))
# print(df['INSTNM'])
# print(df[df['INSTNM']=='Stetson University']) #will not display which rows that don't correlate to what you're looking for

stetson = df[df['INSTNM']=='Stetson University'].iloc[0]
# rich.print(stetson.to_dict()) #shows all relevant information pertaining to the school

df_finaid = pd.read_csv(filepath_or_buffer="sfa2122.csv",encoding='latin1')
print(df_finaid)
stetson_finaid = df_finaid[stetson['UNITID'].iloc[0] == df_finaid['UNITID']].iloc[0] #iloc = index location
print(stetson_finaid.to_dict())