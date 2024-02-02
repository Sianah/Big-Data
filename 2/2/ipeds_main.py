import pandas as pd
import rich

df = pd.read_csv("hd2022.csv", encoding='latin1')
print(df)
print(df.columns)
print(df.shape)
print(df['INSTNM'])
stetson = df[df['INSTNM'] == 'Stetson University'].iloc[0]
rich.print(stetson.to_dict())

df_finaid = pd.read_csv("sfa2122.csv", encoding='latin1')
df_finaid_dictionary = pd.read_excel("sfa2122.xlsx", sheet_name="varlist")
print(df_finaid)
print(df_finaid_dictionary)
stetson_finaid = df_finaid[stetson['UNITID'] == df_finaid['UNITID']].iloc[0].to_dict()
stetson_finaid_newkeys = {}
for key in stetson_finaid:
    new_key = df_finaid_dictionary[df_finaid_dictionary['varname'] == key]['varTitle']
    if len(new_key) > 0:
        new_key = new_key.iloc[0]
        stetson_finaid_newkeys[new_key] = stetson_finaid[key]
rich.print(stetson_finaid_newkeys)
