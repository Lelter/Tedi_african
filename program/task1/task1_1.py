# %%
import pandas as pd

data = pd.read_excel("非洲通讯产品销售数据.xlsx")
# %%
country = data.groupby("服务分类")
country_Year = country.resample('A', on='日期').agg({'销售额': 'sum', '利润': 'sum'}).reset_index()
# country_Year = country_Year.groupby("国家")
# print(type(country_Year))
# for i in country_Year:
#     print(type(i))
# for i in country_Year:
#     print(i)
# %%

row = country_Year.shape[0] / 4
count = 0
for i in range(0, int(row), 1):
    for j in range(4):
        # for j in range(4):
        country_Year.loc[4 * i, "销售额年度同比增长率"] = 0
        country_Year.loc[1 + 4 * i, "销售额年度同比增长率"] = 100*(
                (country_Year.loc[1 + 4 * i, "销售额"] - country_Year.loc[4 * i, "销售额"]) / country_Year.loc[
            4 * i, "销售额"])
        country_Year.loc[2 + 4 * i, "销售额年度同比增长率"] = 100*(
                (country_Year.loc[2 + 4 * i, "销售额"] - country_Year.loc[1 + 4 * i, "销售额"]) / country_Year.loc[
            1 + 4 * i, "销售额"])
        country_Year.loc[3 + 4 * i, "销售额年度同比增长率"] = 100*(
                (country_Year.loc[3 + 4 * i, "销售额"] - country_Year.loc[2 + 4 * i, "销售额"]) / country_Year.loc[
            2 + 4 * i, "销售额"])

        country_Year.loc[4 * i, "利润年度同比增长率"] = 0
        if country_Year.loc[1 + 4 * i, "利润"] > 0 and country_Year.loc[4 * i, "利润"] < 0:
            country_Year.loc[1 + 4 * i, "利润年度同比增长率"] = abs(100*
                (country_Year.loc[1 + 4 * i, "利润"] - country_Year.loc[4 * i, "利润"]) / country_Year.loc[
                    4 * i, "利润"])
        else:
            country_Year.loc[1 + 4 * i, "利润年度同比增长率"] = 100*(
                    (country_Year.loc[1 + 4 * i, "利润"] - country_Year.loc[4 * i, "利润"]) / country_Year.loc[
                4 * i, "利润"])
        if country_Year.loc[2 + 4 * i, "利润"] > 0 and country_Year.loc[1 + 4 * i, "利润"] < 0:
            country_Year.loc[2 + 4 * i, "利润年度同比增长率"] = abs(100*(
                    (country_Year.loc[2 + 4 * i, "利润"] - country_Year.loc[1 + 4 * i, "利润"]) / country_Year.loc[
                1 + 4 * i, "利润"]))
        else:
            country_Year.loc[2 + 4 * i, "利润年度同比增长率"] = 100*(
                    (country_Year.loc[2 + 4 * i, "利润"] - country_Year.loc[1 + 4 * i, "利润"]) / country_Year.loc[
                1 + 4 * i, "利润"])
        if country_Year.loc[3 + 4 * i, "利润"] > 0 and country_Year.loc[2 + 4 * i, "利润"] < 0:
            country_Year.loc[3 + 4 * i, "利润年度同比增长率"] = abs(100*(
                    (country_Year.loc[3 + 4 * i, "利润"] - country_Year.loc[2 + 4 * i, "利润"]) / country_Year.loc[
                2 + 4 * i, "利润"]))
        else:
            country_Year.loc[3 + 4 * i, "利润年度同比增长率"] = 100*(
                    (country_Year.loc[3 + 4 * i, "利润"] - country_Year.loc[2 + 4 * i, "利润"]) / country_Year.loc[
                2 + 4 * i, "利润"])
country_Year=country_Year.round(2)
country_Year.to_csv("result/服务分类年度同比增长率.csv", encoding='utf-8_sig', index=False)
