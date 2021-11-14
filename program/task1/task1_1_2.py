import pandas as pd
data = pd.read_excel("非洲通讯产品销售数据.xlsx")


# %%
def add_date(x):
    temp = x
    for i, rows in temp.iterrows():
        if i > 15:
            i = 0
        if i < 4:
            x.loc[i, "同比销售额"] = 0
        else:
            tongbixiaoshoue = rows['销售额'] - temp.loc[i - 4, '销售额']
            #
            x.loc[i, "同比销售额"] = tongbixiaoshoue
    return x

    # x['同比销售额'] = x.销售额.diff(4)
    # x['同比利润'] = x.利润.diff(4)
    # for i in x['销售额'] - x['同比销售额']:
    #
    # print(x['销售额'] - x['同比销售额'])
    # if (x['销售额'] - x['同比销售额'])==0.0:
    #     x['销售额季度增长率']=100
    # else:
    #     x['销售额季度增长率'] = x['同比销售额'] / (x['销售额'] - x['同比销售额']) * 100
    pass


country = data.groupby("服务分类")
country_Season = country.resample('Q', on='日期').agg({'销售额': 'sum', '利润': 'sum'}).reset_index()
country_Season = country_Season.groupby("服务分类")
beishu = 0
result=pd.DataFrame()
for group in country_Season:
    df = group[1]
    row = df.shape[0]
    for count in range(row):
        if count < 4:
            df.loc[16 * beishu + count, "同比销售额"] = 0
            df.loc[16 * beishu + count, "同比利润"] = 0
        else:
            tongbixiaoshoue = df.loc[16 * beishu + count, '销售额'] - df.loc[16 * beishu + count - 4, '销售额']
            tongbilirun = df.loc[16 * beishu + count, "利润"] - df.loc[16 * beishu + count - 4, '利润']
            #
            df.loc[16 * beishu + count, "同比销售额"] = tongbixiaoshoue
            df.loc[16 * beishu + count, "同比利润"] = tongbilirun
            if df.loc[16 * beishu + count - 4, '利润'] < 0 and df.loc[16 * beishu + count, '利润'] > 0:
                df.loc[16 * beishu + count, "同比利润季度增长率"] = 100 * (
                    abs(tongbilirun / df.loc[16 * beishu + count - 4, '利润']))
            else:
                df.loc[16 * beishu + count, "同比利润季度增长率"] = 100 * (
                            tongbilirun / df.loc[16 * beishu + count - 4, '利润'])

            if df.loc[16 * beishu + count - 4, '销售额'] < 0 and df.loc[16 * beishu + count, '销售额'] > 0:
                df.loc[16 * beishu + count, "同比销售额季度增长率"] = 100 * (
                    abs(tongbixiaoshoue / df.loc[16 * beishu + count - 4, '销售额']))
            else:
                df.loc[16 * beishu + count, "同比销售额季度增长率"] = 100 * (
                            tongbixiaoshoue / df.loc[16 * beishu + count - 4, '销售额'])

    beishu = beishu + 1
    # for i, rows in df.iterrows():
    #     if i < 4:
    #         df.loc[i, "同比销售额"] = 0
    #     else:
    #         tongbixiaoshoue = rows['销售额'] - df.loc[i - 4, '销售额']
    #         #
    #         df.loc[i, "同比销售额"] = tongbixiaoshoue
    print(df)
    result=result.append(df)
# country_Season = country_Season.apply(add_date)
# print(country_Season)
print(result)
result.to_csv("服务分类销售额利润季度增长率.csv", encoding="utf-8_sig",index=False)
