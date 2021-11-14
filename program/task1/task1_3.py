import pandas as pd
e_data =pd.read_excel('SalespersonData.xlsx')
#print(e_data)
#print(e_data.info())
#print(list(e_data.groupby('销售经理')))
df=e_data.groupby("销售经理")["销售合同"].sum().reset_index()
df.to_excel("1_3_1.xlsx",index=False)
list1=list(e_data.groupby("销售经理",axis=0)["成交率"])
list2=list(e_data.groupby("销售经理",axis=0)["销售合同"])
Cjl=[]
# print(list1)
# print(list2)
#
# print(len(list1))
# print(len(list2))
for i in range(0,len(list1)):
    sum=0
    sumsucess=0
    l1=list1[i][1].values
    l2=list2[i][1].values
    for j in range(0,len(list1[i][1])):
        #print(float(list2[i][1][j])/float(list1[i][1][j]))
        #sum=sum+float(list2[i][1][j])/float(list1[i][1][j])
        sum = sum + float(l2[j]) / float(l1[j])
        sumsucess=sumsucess+float(l2[j])
    ave= sumsucess/sum
    Cjl.append(ave)
   #

#df.to_excel("out.xlsx",index=False)
#print(df[0][1])
# df =pd.read_excel('SalespersonData.xlsx')
df["成交率"]=Cjl
#
df.to_excel("1_3_2.xlsx",index=False)