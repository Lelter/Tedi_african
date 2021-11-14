from __future__ import print_function

import pandas as pd
import pmdarima as pm
import statsmodels.api as sm

data = pd.read_csv("result/服务分类销售额利润季度增长率.csv")
print(data)
dta = list(data["销售额"])
print(dta)
row = data.shape[0]
print(row)
countries = 3
for i in range(0, countries):
    dta = list(data["销售额"])[i * 16:i * 16 + 16]
    print(dta)
    dta = pd.Series(dta)
    dta.index = pd.Index(sm.tsa.datetools.dates_from_range('2017Q1', '2020Q4'))
    model = pm.auto_arima(dta, start_p=1, start_q=1,
                          max_p=8, max_q=8, m=1,
                          start_P=0, seasonal=False,
                          max_d=3, trace=True,
                          information_criterion='aic',
                          error_action='ignore',
                          suppress_warnings=True,
                          stepwise=False)
    forecast = model.predict(2)  # 预测未来10年的数据
    result = forecast[0]
    if result < 0:
        result = 0
    for j in range(16):
        data.loc[j + 16 * i, "第一季度预测销售额"] = result
data.to_csv("result/国家预测.csv", index=False, encoding="utf-8_sig")
for i in range(0, countries):
    dta = list(data["利润"])[i * 16:i * 16 + 16]
    # dta=[item *10 for item in dta]
    print(dta)
    dta = pd.Series(dta)
    dta.index = pd.Index(sm.tsa.datetools.dates_from_range('2017Q1', '2020Q4'))
    model = pm.auto_arima(dta, start_p=1, start_q=1,
                          max_p=8, max_q=8, m=2,
                          start_P=0, seasonal=True,
                          max_d=3, trace=True,
                          information_criterion='aic',
                          error_action='ignore',
                          suppress_warnings=True,
                          stepwise=False)
    forecast = model.predict(2)  # 预测未来10年的数据
    result = forecast[0]

    for j in range(16):
        data.loc[j + 16 * i, "第一季度预测利润"] = result
data.to_csv("result/服务分类预测.csv", index=False, encoding="utf-8_sig")

# dta=pd.Series(dta)
# train=dta[0:12]
# test=dta[12:16]
# print(train,test)
# train.index= pd.Index(sm.tsa.datetools.dates_from_range('2017Q1','2019Q4'))
# dta.index = pd.Index(sm.tsa.datetools.dates_from_range('2017Q1','2020Q4'))
# train.plot(figsize=(12,8))
# plt.title('dta')
# print('dta:',train)
# model = pm.auto_arima(dta, start_p=1, start_q=1,
#                            max_p=8, max_q=8, m=1,
#                            start_P=0, seasonal=False,
#                            max_d=3, trace=True,
#                            information_criterion='aic',
#                            error_action='ignore',
#                            suppress_warnings=True,
#                            stepwise=False)
# forecast = model.predict(7)#预测未来10年的数据
# print(forecast)
