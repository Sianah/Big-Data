import pandas as pd
import rich

df = pd.read_csv("hd2022.csv", encoding='latin1')
print(df)

# Picking Columns
print(df.columns)
print(df.shape)
print(df['INSTNM'])
stetson = df[df['INSTNM'] == 'Stetson University'].iloc[0]
# rich.print(stetson.to_dict())
rich.print(df[['UNITID', 'INSTNM']])
rich.print(df.filter(regex='.URL'))

# Picking Rows

# all institutions in florida
rich.print(df[df['STABBR'] == 'FL'])

# institutions in florida that have 'university' in their name
fl_univ = df.query('STABBR == "FL" & INSTNM.str.contains("University")',
                   engine='python')  # 64 institutions in florida
rich.print(fl_univ)

# First 10 rows
rich.print(fl_univ.iloc[0:10])

# first 10 rows, third column
rich.print(fl_univ.iloc[0:10, 2])
# blue cyan number on the left is the index

rich.print(fl_univ.loc[651])  # pulls out data from that row

# reset index with unit id
# fl_univ.index = fl_univ['UNITID'] #unitID is now the row name
fl_univ.index = fl_univ['INSTNM']
rich.print(fl_univ)
rich.print(fl_univ.loc['Stetson University'])  # pulls out data from that row
# remember, iloc always needs a number. Loc does not. iloc takes row integer, loc takes name
# rich.print(fl_univ ['Stetson University']) #Would look for a column named stetson university
# will gather street address of stetson. At will isolate row column
# at is like loc, but faster
rich.print(fl_univ.at['Stetson University', 'ADDR'])

rich.print(fl_univ.describe())  # takes every column, counts records
rich.print(fl_univ[['ADDR', 'CITY']].count())  # counts records for each column


# df_finaid = pd.read_csv("sfa2122.csv", encoding='latin1')
# df_finaid_dictionary = pd.read_excel("sfa2122.xlsx", sheet_name="varlist")
# print(df_finaid)
# print(df_finaid_dictionary)
# stetson_finaid = df_finaid[stetson['UNITID'] == df_finaid['UNITID']].iloc[0].to_dict()
# stetson_finaid_newkeys = {}
# for key in stetson_finaid:
#     new_key = df_finaid_dictionary[df_finaid_dictionary['varname'] == key]['varTitle']
#     if len(new_key) > 0:
#         new_key = new_key.iloc[0]
#         stetson_finaid_newkeys[new_key] = stetson_finaid[key]
# rich.print(stetson_finaid_newkeys)
