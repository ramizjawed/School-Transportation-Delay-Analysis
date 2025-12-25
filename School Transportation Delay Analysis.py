import pandas as pd
import matplotlib.pyplot as plt

bus_data = {
    'Bus_Name': ['Rungta Bus1', ' Rungta Bus2', 'Rungta Bus3', 'Rungta Bus4'],
    'Time_Scheduled': ['08:00', '08:05', '08:10', '08:15'],
    'Time_Arrival': ['08:11', '08:12', '08:15', '08:23']
}

df = pd.DataFrame(bus_data)

print("Bus Timing Data")
print(df)

df['Time_Scheduled'] = pd.to_datetime(df['Time_Scheduled'])
df['Time_Arrival'] = pd.to_datetime(df['Time_Arrival'])

df['Delay'] = (df['Time_Arrival'] - df['Time_Scheduled']).dt.seconds / 60

print("\nBus Delay Data")
print(df)

avg_delay = df['Delay'].mean()
max_delay = df['Delay'].max()
min_delay = df['Delay'].min()

print("\nSummary")
print("Average Delay:", avg_delay)
print("Maximum Delay:", max_delay)
print("Minimum Delay:", min_delay)

plt.bar(df['Bus_Name'], df['Delay'])
plt.xlabel("Bus")
plt.ylabel("Delay in Minutes")
plt.title("School Bus Delay Analysis")
plt.show()

