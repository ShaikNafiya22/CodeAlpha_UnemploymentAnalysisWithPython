import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
# import plotly.express as px
# %matplotlib inline

data1 = pd.read_excel(r"C:\Users\syeda\OneDrive\Documents\un1.xlsx")
data2 = pd.read_excel(r"C:\Users\syeda\OneDrive\Documents\un2020.xlsx")
data1.head()
data1.info()
data1.describe()
data1.shape
data1.columns = data1.columns.str.strip()
# Handling missing values
data1.dropna(inplace=True)
data1.isnull().sum()
# 1. Unemployment Rate Distribution by Region
plt.figure(figsize=(15, 7))
sns.barplot(x="Region", y="Estimated Unemployment Rate (%)", data=data1, ci=None, palette="magma")
plt.xticks(rotation=90)
plt.title("Unemployment Rate by Region")
plt.ylabel("Unemployment Rate (%)")
plt.xlabel("Region")
# plt.show()
# 2. Box Plot for Labor Participation Rate
plt.figure(figsize=(15,7))
sns.barplot(x = "Region", y = "Estimated Labour Participation Rate (%)", data = data1, ci = None, capsize=0.2, palette="Set2")
plt.title("Labour participation Rate by Region")
plt.xticks(rotation = 90)
plt.show()
# plt.figure(figsize=(12, 6))
# sns.boxplot(x="Region", y="Estimated Labour Participation Rate (%)", data=data1, palette="Spectral")
# plt.title("Labor Participation Rate by Region")
# plt.xticks(rotation=90)
# plt.tight_layout()
# plt.show()
#Average Metrics by Region
avg_metrics = data1.groupby('Region')[['Estimated Unemployment Rate (%)', 
                                       'Estimated Labour Participation Rate (%)']].mean()
avg_metrics
# 3. Average Unemployment Rate Plot
avg_metrics.sort_values(by="Estimated Unemployment Rate (%)", ascending=False).plot(kind="bar", figsize=(10, 6))
plt.title("Average Unemployment and Labor Participation Rate by Region")
plt.ylabel("Percentage")
plt.tight_layout()
# plt.show()
#4. Area-wise Data
data1["Area"].value_counts()
sns.countplot(x="Area",data=data1)
# plt.show()
# 5. Pair Plot for Key Metrics
pair_data = data1[["Estimated Unemployment Rate (%)", "Estimated Employed", 
                   "Estimated Labour Participation Rate (%)"]]
sns.pairplot(pair_data, diag_kind="kde", palette="husl", markers="o")
plt.suptitle("Relationship Between Key Metrics", y=1.02)
# plt.show()
data2.head()
data2.describe
data2.isnull().sum()
data2.columns = data2.columns.str.strip()
print(data2.columns)
data2.columns= ["States","Date","Frequency",
               "Estimated Unemployment Rate",
               "Estimated Employed",
               "Estimated Labour Participation Rate",
               "Region","longitude","latitude"]
data2.columns
# Converting 'Date' column to datetime
data2['Date'] = pd.to_datetime(data2['Date'], errors='coerce')
data2 = data2.dropna(subset=['Date'])
# FILTERING DATA FOR THE COVID-19 PERIOD (2020)
covid_data = data2[data2['Date'].dt.year == 2020]
# QUESTION 1: What was the overall trend in unemployment during COVID-19?
plt.figure(figsize=(12, 6))
sns.lineplot(data=covid_data, x='Date', y='Estimated Unemployment Rate', hue='Region', palette='tab10')
plt.title("Trend of Unemployment Rate During COVID-19 (2020)")
plt.xlabel("Date")
plt.ylabel("Estimated Unemployment Rate (%)")
plt.grid(True)
# plt.show()
# QUESTION 2: Which regions were most affected during the COVID-19 pandemic?
plt.figure(figsize=(10, 6))
sns.boxplot(data=covid_data, x='Region', y='Estimated Unemployment Rate', palette='Set2')
plt.title("Unemployment Rate by Region During COVID-19 (2020)")
plt.xticks(rotation=45)
plt.grid(True)
# plt.show()
# QUESTION 3: Were there any seasonal trends in unemployment during the pandemic?
covid_data['Month'] = covid_data['Date'].dt.month
monthly_avg = covid_data.groupby('Month')['Estimated Unemployment Rate'].mean().reset_index()

plt.figure(figsize=(10, 6))
sns.lineplot(x='Month', y='Estimated Unemployment Rate', data=monthly_avg, marker='o', color='blue')
plt.title("Seasonal Trends in Unemployment Rate During COVID-19 (2020)")
plt.xlabel("Month")
plt.ylabel("Average Unemployment Rate (%)")
plt.grid(True)
# plt.show()
# QUESTION 4: States most impacted by unemployment during COVID-19
state_avg = covid_data.groupby('States')['Estimated Unemployment Rate'].mean().sort_values(ascending=False).head(10)
plt.figure(figsize=(12, 6))
sns.barplot(x=state_avg.values, y=state_avg.index, palette='viridis')
plt.title("Top 10 States Most Impacted by Unemployment During COVID-19 (2020)")
plt.xlabel("Average Unemployment Rate (%)")
plt.ylabel("States")
plt.grid(True)
# plt.show()