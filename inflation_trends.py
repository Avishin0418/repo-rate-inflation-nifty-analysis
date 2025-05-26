import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load data
df = pd.read_csv('inflation_data.csv')

# Convert Date column
df['Date'] = pd.to_datetime(df['Date'])

# Plot trends
plt.figure(figsize=(12, 6))
sns.lineplot(x='Date', y='WPI', data=df, label='WPI')
sns.lineplot(x='Date', y='CPI', data=df, label='CPI')
plt.title('Inflation Trends (WPI & CPI)')
plt.xlabel('Date')
plt.ylabel('Index')
plt.legend()
plt.show()

# Highlight events (optional)
events = {'Demonetization': '2016-11-08', 'COVID Lockdown': '2020-03-25'}
for event, date in events.items():
    plt.axvline(pd.to_datetime(date), color='gray', linestyle='--', label=event)

plt.legend()
plt.show()
