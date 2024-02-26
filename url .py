import pandas as pd
import ast

df=pd.read_excel("Electronics-Raw - Copy (1).xlsx",sheet_name="Sheet1")
df2=pd.read_excel("Electronics-Raw - Copy (1).xlsx",sheet_name="Sheet2")

url_list=set(df2['url'])


for index, row in df.iterrows():
     data=ast.literal_eval(row['attributes'])
     for k,v in data.items():
        if isinstance(v,dict):
            if 'url' in v and v['url'] in url_list:
                v.pop('url')
     df.at[index, 'attributes'] = str(data)

df.to_excel("Modified_Electronics.xlsx", index=False)