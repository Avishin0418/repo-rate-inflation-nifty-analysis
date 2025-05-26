import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import statsmodels.api as sm

# Load data
df = pd.read_csv('repo_inflation_nifty.csv')  # your prepared dataset

# Correlation matrix
corr = df.corr()
sns.heatmap(corr, annot=True, cmap='coolwarm')
plt.title('Correlation Matrix')
plt.show()

# Trend plots
fig, ax1 = plt.subplots()
ax1.plot(df['Date'], df['RepoRate'], color='blue', label='Repo Rate')
ax1.set_ylabel('Repo Rate', color='blue')

ax2 = ax1.twinx()
ax2.plot(df['Date'], df['Inflation'], color='red', label='Inflation')
ax2.set_ylabel('Inflation', color='red')
plt.title('Repo Rate vs Inflation Over Time')
plt.show()

# Multi-variable regression
X = df[['RepoRate', 'LaggedRepoRate']]  # adjust based on dataset
y = df['Nifty']
X = sm.add_constant(X)
model = sm.OLS(y, X).fit()
print(model.summary())
