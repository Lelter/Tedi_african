import pandas as pd
# df2 =pd.read_excel('2_2_1.xlsx',0)
# df3=df2.groupby(["地区","服务分类"]).resample('Q', on='日期').agg({'销售额':'sum','利润':'sum'}).reset_index()
df=pd.read_excel("2_2_4.xlsx")
zzl=[]
lrzzl=[]
for i in range(0,df.shape[0]):
    if i%16<4:
        zzl.append(0)
        lrzzl.append(0)
    else:
        if df.iloc[i-4]["销售额"]>0:
            zzl.append((df.iloc[i]["销售额"]-df.iloc[i-4]["销售额"])/df.iloc[i-4]["销售额"])
        else:
            # zzl.append((df.iloc[i]["销售额"]-df.iloc[i-4]["销售额"])/df.iloc[i-4]["销售额"])
            # lrzzl.append((df.iloc[i]["利润"]-df.iloc[i-1]["利润"])/abs(df.iloc[i-1]["利润"]))
            zzl.append("")
        if df.iloc[i-4]["利润"]==0:
            lrzzl.append("")
            #lrzzl.append((df.iloc[i]["利润"]-df.iloc[i-4]["利润"])/df.iloc[i-4]["利润"])
        else:
            # zzl.append((df.iloc[i]["销售额"]-df.iloc[i-4]["销售额"])/df.iloc[i-4]["销售额"])
            # lrzzl.append((df.iloc[i]["利润"]-df.iloc[i-1]["利润"])/abs(df.iloc[i-1]["利润"]))
            lrzzl.append((df.iloc[i]["利润"] - df.iloc[i - 4]["利润"]) / abs(df.iloc[i - 4]["利润"]))
df["销售额增长率"] = zzl
df["利润增长率"] = lrzzl
df.to_excel("2_2_5.xlsx",index=False)