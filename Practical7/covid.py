import pandas as pd
import os
import matplotlib.pyplot as plt
import numpy as np
os.chdir("/Users/misaki/IBI1_2022-23/Practical7")
covid_data = pd.read_csv("full_data.csv")
print(covid_data.iloc[0:1001:100,0:5]) #There is correct code for showing the second column from every 100th row from the first 1000 rows

print(covid_data.loc[covid_data['location'] == "Afghanistan","total_cases"]) #show “total cases” for all rows corresponding to Afghanistan.
my_columns = [False, False, True,True,False,False]
new_data = covid_data.loc[covid_data['date'] == '2020-03-31',my_columns]
mean_data=new_data.describe()
print( mean_data.iloc[1,0:2])

new_data.iloc[:,0].plot.box()
plt.show()
new_data.iloc[:,1].plot.box()
plt.show()

my_columns = [True, False, True,True,False,False]
world_dates = covid_data.iloc[:,my_columns]
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
my_columns=[True,False,True,False,False,False]
df=covid_data.iloc[:,my_columns]
df.groupby=df.groupby("date",as_index=False).sum(numeric_only=True)
world_new_cases=df.groupby.iloc[:,1]
world_dates=df.groupby.iloc[:,0]
my_columns=[True,False,False,True,False,False]
df=covid_data.iloc[:,my_columns]
df.groupby=df.groupby("date",as_index=False).sum(numeric_only=True)
world_new_deaths=df.groupby.iloc[:,1]
plt.scatter(world_dates,world_new_cases,c='#E053A3',alpha=0.5,marker='o')
plt.scatter(world_dates,world_new_deaths,c='aqua',alpha=0.5,marker='o')
plt.xlabel('date',c='orange')
plt.ylabel('number',c='orange')
plt.tick_params(axis='x',colors='orange')
plt.tick_params(axis='y',colors='orange')
plt.show()

print("my question is What proportion of cases have died in the Germany?")
Ger_data=covid_data.loc[covid_data['location'] == 'Germany',['new_cases','new_deaths']]
Ger_new_data=Ger_data.describe()
print("the answer is", Ger_new_data.iloc[1,1] / Ger_new_data.iloc[1,0])
