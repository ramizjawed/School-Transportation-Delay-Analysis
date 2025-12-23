import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from datetime import datetime, timedelta

# --- STEP 1: GENERATE SAMPLE DATA ---
# (Simulating a real school district dataset)
np.random.seed(42)
rows = 200
routes = ['Route_A', 'Route_B', 'Route_C', 'Route_D', 'Route_E']
days = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday']

data = {
    'Route_ID': [np.random.choice(routes) for _ in range(rows)],
    'Day_of_Week': [np.random.choice(days) for _ in range(rows)],
    'Scheduled_Hour': [np.random.choice([7, 8, 14, 15]) for _ in range(rows)], # AM/PM shifts
    'Scheduled_Min': [np.random.choice([0, 15, 30, 45]) for _ in range(rows)],
}

df = pd.DataFrame(data)

# Create Timestamps
df['Scheduled_Arrival'] = pd.to_datetime('2023-10-02') + \
                          pd.to_timedelta(df['Scheduled_Hour'], unit='h') + \
                          pd.to_timedelta(df['Scheduled_Min'], unit='m')

# Simulate delays (Random noise + some routes being naturally slower)
# Some routes have a higher 'mean' delay to simulate traffic patterns
delay_noise = np.random.normal(loc=5, scale=10, size=rows) 
df['Actual_Arrival'] = df['Scheduled_Arrival'] + pd.to_timedelta(delay_noise, unit='m')

# --- STEP 2: DATA PROCESSING ---
# Calculate Delay in Minutes
df['Delay_Min'] = (df['Actual_Arrival'] - df['Scheduled_Arrival']).dt.total_seconds() / 60

# Add a Status Column based on delay threshold
def categorize_delay(x):
    if x <= 0: return 'Early/On-Time'
    elif x <= 10: return 'Minor Delay'
    else: return 'Major Delay'

df['Status'] = df['Delay_Min'].apply(categorize_delay)

# --- STEP 3: SUMMARY STATISTICS ---
print("--- SUMMARY STATISTICS ---")
stats = df.groupby('Route_ID')['Delay_Min'].agg(['mean', 'max', 'std']).round(2)
print(stats)

# --- STEP 4: VISUALIZATION ---
sns.set_theme(style="whitegrid")
plt.figure(figsize=(12, 6))

# Subplot 1: Average Delay per Route
plt.subplot(1, 2, 1)
sns.barplot(data=df, x='Route_ID', y='Delay_Min', palette='viridis', ci=None)
plt.title('Average Delay by Route (Minutes)')
plt.axhline(df['Delay_Min'].mean(), color='red', linestyle='--', label='Overall Avg')
plt.legend()

# Subplot 2: Delay Status Distribution
plt.subplot(1, 2, 2)
df['Status'].value_counts().plot.pie(autopct='%1.1f%%', colors=['#66b3ff','#99ff99','#ff9999'])
plt.title('Arrival Status Breakdown')

plt.tight_layout()
plt.show()