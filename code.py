# --------------
#Importing header files
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

#Path of the file

data=pd.read_csv(path)
data.rename(columns = {'Total':'Total_Medals'}, inplace = True)
data.head(10)
#Code starts here



# --------------
#Code starts here
data['Better_Event']=np.where(data['Total_Summer']==data['Total_Winter'],'Both',np.where(data['Total_Summer']>data['Total_Winter'],'Summer','Winter'))
better_event=data['Better_Event'].value_counts().idxmax()
print(better_event)




# --------------
#Code starts here
top_countries=data[['Country_Name','Total_Summer', 'Total_Winter','Total_Medals']]
top_countries=top_countries[:-1]


def top_ten(df,col):
    country_list=[]
    top_10=df.nlargest(10,[col])
    country_list=list(top_10['Country_Name'])
    return country_list

top_10_summer=top_ten(top_countries,'Total_Summer')
top_10_winter=top_ten(top_countries,'Total_Winter')
top_10=top_ten(top_countries,'Total_Medals')

common=list(set(top_10) & set(top_10_summer) & set(top_10_winter))
# print(top_10_summer)
# print(top_10_winter)
# print(top_10)
print(common)


# --------------
#Code starts here
summer_df=data[data['Country_Name'].isin(top_10_summer)]
winter_df=data[data['Country_Name'].isin(top_10_winter)]
top_df=data[data['Country_Name'].isin(top_10)]

plt.bar(summer_df['Country_Name'], summer_df['Total_Summer'])
plt.xlabel('Country_Name', fontsize=5)
plt.ylabel('Total_Summer', fontsize=5)
plt.show()

plt.bar(winter_df['Country_Name'], winter_df['Total_Winter'])
plt.xlabel('Country_Name', fontsize=5)
plt.ylabel('Total_Winter', fontsize=5)
plt.show()

plt.bar(top_df['Country_Name'], top_df['Total_Medals'])
plt.xlabel('Country_Name', fontsize=5)
plt.ylabel('Total_Medals', fontsize=5)
plt.show()


# --------------
#Code starts here
summer_df['Golden_Ratio']=summer_df['Gold_Summer']/summer_df['Total_Summer']
summer_max_ratio=round(summer_df.loc[summer_df['Golden_Ratio'].idxmax()]['Golden_Ratio'],2)
summer_country_gold=summer_df.loc[summer_df['Golden_Ratio'].idxmax()]['Country_Name']

winter_df['Golden_Ratio']=winter_df['Gold_Winter']/winter_df['Total_Winter']
winter_max_ratio=round(winter_df.loc[winter_df['Golden_Ratio'].idxmax()]['Golden_Ratio'],2)
winter_country_gold=winter_df.loc[winter_df['Golden_Ratio'].idxmax()]['Country_Name']

top_df['Golden_Ratio']=top_df['Gold_Total']/top_df['Total_Medals']
top_max_ratio=round(top_df.loc[top_df['Golden_Ratio'].idxmax()]['Golden_Ratio'],2)
top_country_gold=top_df.loc[top_df['Golden_Ratio'].idxmax()]['Country_Name']
print(top_max_ratio)
print(winter_max_ratio)
print(summer_max_ratio)
print(top_country_gold)
print(winter_country_gold)
print(summer_country_gold)


# --------------
#Code starts here
data_1=data[:-1]
data_1['Total_Points']=data['Gold_Total']*3+data['Silver_Total']*2+data['Bronze_Total']
most_points=data_1.loc[data_1['Total_Points'].idxmax()]['Total_Points']
best_country=data_1.loc[data_1['Total_Points'].idxmax()]['Country_Name']
print(best_country)
print(most_points)


# --------------
#Code starts here
best=data[data['Country_Name']==best_country][['Gold_Total','Silver_Total','Bronze_Total']]
print(best)
best.plot.bar()
plt.xlabel('United States')
plt.ylabel('Medals Tally')
plt.xticks(rotation=45)
plt.show()


