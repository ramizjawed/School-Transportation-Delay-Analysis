# **School Transportation Delay Analysis**

**Minor Project – Pandas**

---

## **1. Introduction**

School transportation system students ke liye bahut important hota hai. Agar bus late aati hai, to students ko problem hoti hai aur classes bhi miss hoti hain.
Is project ka aim **school buses ke arrival time ko analyze karna** aur **delay trends nikalna** hai.

---

## **2. Objective**

* Bus arrival time aur scheduled time ka analysis
* Delay calculate karna
* Maximum aur average delay find karna
* Visualization ke through delay trend samajhna

---

## **3. Tools & Libraries Used**

* Python
* Pandas
* Matplotlib

---

## **4. Dataset Description**

Dataset me following columns hain:

* `Bus_ID` – Bus ka number
* `Scheduled_Time` – Bus ka fixed arrival time
* `Actual_Time` – Bus ka real arrival time

---

## **5. Python Code (Pandas Project)**

```python
# School Transportation Delay Analysis
# Minor Project - Pandas

import pandas as pd
import matplotlib.pyplot as plt

# bus timing data
bus_data = {
    'Bus_Name': ['Rungta Bus1', ' Rungta Bus2', 'Rungta Bus3', 'Rungta Bus4'],
    'Time_Scheduled': ['08:00', '08:05', '08:10', '08:15'],
    'Time_Arrival': ['08:11', '08:12', '08:15', '08:23']
}

df = pd.DataFrame(bus_data)

print("Bus Timing Data")
print(df)

# convert time into proper format
df['Time_Scheduled'] = pd.to_datetime(df['Time_Scheduled'])
df['Time_Arrival'] = pd.to_datetime(df['Time_Arrival'])

# calculate delay
df['Delay'] = (df['Time_Arrival'] - df['Time_Scheduled']).dt.seconds / 60

print("\nBus Delay Data")
print(df)

# basic summary
avg_delay = df['Delay'].mean()
max_delay = df['Delay'].max()
min_delay = df['Delay'].min()

print("\nSummary")
print("Average Delay:", avg_delay)
print("Maximum Delay:", max_delay)
print("Minimum Delay:", min_delay)

# graph
plt.bar(df['Bus_Name'], df['Delay'])
plt.xlabel("Bus")
plt.ylabel("Delay in Minutes")
plt.title("School Bus Delay Analysis")
plt.show()




```

---

## **6. Explanation of Code**

* Pehle bus timing ka **DataFrame** banaya
* Scheduled aur Actual time ko **datetime format** me convert kiya
* Delay calculate kiya **minutes me**
* `describe()` function se **summary statistics** nikale
* Line chart ke through **delay trend visualize** kiya

---

## **7. Output & Analysis**

* Kuch buses me zyada delay dekha gaya
* Average delay easily identify ho gaya
* Visualization se clear hota hai kaunsi bus regularly late hai

---

## **8. Conclusion**

Is project se pata chalta hai ki:

* School buses me delay ek common problem hai
* Pandas aur visualization ka use karke delay trends easily analyze ho sakte hain
* Management is data ka use karke **better scheduling** kar sakti hai

---

## **9. Future Scope**

* Real-time GPS data use kiya ja sakta hai
* Weather aur traffic data add kiya ja sakta hai
* Predictive analysis bhi possible hai

---

