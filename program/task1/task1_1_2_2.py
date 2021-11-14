import pandas as pd

data = pd.read_excel("国家季度_修改.xlsx")
print(data)

#
# country = data.groupby("国家")
# country_Season = country.resample('Q', on='日期').agg({'销售额': 'sum', '利润': 'sum'}).reset_index()
# print(country_Season)
# country_Season = country_Season.groupby("国家")
country_Season = data
temp = pd.DataFrame()
# for group in country_Season:
#     df=group[1]
#     temp=temp.append(df)
# print(temp)
beishu = 0
result = pd.DataFrame()
for i in range(0, 832, 16):
    row = 16
    for count in range(row):
        if count < 4:
            country_Season.loc[16 * beishu + count, "同比销售额"] = 0
            country_Season.loc[16 * beishu + count, "同比利润"] = 0
            country_Season.loc[16 * beishu + count, "同比销售额季度增长率"] = 0
            country_Season.loc[16 * beishu + count, "同比利润季度增长率"] = 0
        else:
            tongbixiaoshoue = country_Season.loc[16 * beishu + count, '销售额'] - country_Season.loc[
                16 * beishu + count - 4, '销售额']
            tongbilirun = country_Season.loc[16 * beishu + count, "利润"] - country_Season.loc[
                16 * beishu + count - 4, '利润']
            country_Season.loc[16 * beishu + count, "同比销售额"] = tongbixiaoshoue
            country_Season.loc[16 * beishu + count, "同比利润"] = tongbilirun

            if country_Season.loc[16 * beishu + count - 4, '利润'] < 0 and country_Season.loc[
                16 * beishu + count, '利润'] > 0:
                country_Season.loc[16 * beishu + count, "同比利润季度增长率"] = 100 * (
                    abs(tongbilirun / country_Season.loc[16 * beishu + count - 4, '利润']))
            else:
                country_Season.loc[16 * beishu + count, "同比利润季度增长率"] = 100 * (
                        tongbilirun / country_Season.loc[16 * beishu + count - 4, '利润'])
            if country_Season.loc[16 * beishu + count - 4, '利润'] == 0 and country_Season.loc[
                16 * beishu + count, '利润'] > 0:
                country_Season.loc[16 * beishu + count, "同比利润季度增长率"] = None
            if country_Season.loc[16 * beishu + count - 4, '利润'] == 0 and country_Season.loc[
                16 * beishu + count, '利润'] < 0: country_Season.loc[16 * beishu + count, "同比利润季度增长率"] = None
            if country_Season.loc[16 * beishu + count - 4, '销售额'] < 0 and country_Season.loc[
                16 * beishu + count, '销售额'] > 0:
                country_Season.loc[16 * beishu + count, "同比销售额季度增长率"] = 100 * (
                    abs(tongbixiaoshoue / country_Season.loc[16 * beishu + count - 4, '销售额']))
            else:
                country_Season.loc[16 * beishu + count, "同比销售额季度增长率"] = 100 * (
                        tongbixiaoshoue / country_Season.loc[16 * beishu + count - 4, '销售额'])
            if country_Season.loc[16 * beishu + count - 4, '销售额'] == 0 and country_Season.loc[
                16 * beishu + count, '销售额'] > 0:
                country_Season.loc[16 * beishu + count, "同比销售额季度增长率"] = None
            if country_Season.loc[16 * beishu + count - 4, '销售额'] == 0 and country_Season.loc[
                16 * beishu + count, '销售额'] < 0: country_Season.loc[16 * beishu + count, "同比销售额季度增长率"] = None
    beishu = beishu + 1
#     # for i, rows in country_Season.iterrows():
#     #     if i < 4:
#     #         country_Season.loc[i, "同比销售额"] = 0
#     #     else:
#     #         tongbixiaoshoue = rows['销售额'] - country_Season.loc[i - 4, '销售额']
#     #         #
#     #         country_Season.loc[i, "同比销售额"] = tongbixiaoshoue
#     print(country_Season)
# country_Season = country_Season.apply(add_date)
# print(country_Season)
print(country_Season)
country_Season.to_csv("国家销售额利润季度增长率.csv", encoding="utf-8_sig", index=False)
