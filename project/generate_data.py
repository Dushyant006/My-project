
import pandas as pd
import numpy as np
from datetime import datetime, timedelta

print("🔄 Starting data generation...")

# 1. Set up a timeline for 2 years (730 days)
start_date = datetime(2024, 5, 25)
dates = [start_date + timedelta(days=i) for i in range(730)]

data = []

# 2. Generate daily costs with realistic trends
for date in dates:
    base_cost = 150.0  
    days_elapsed = (date - start_date).days
    growth_trend = days_elapsed * 0.15  
    
    if date.weekday() < 5:
        seasonality = np.random.uniform(20, 40)  
    else:
        seasonality = np.random.uniform(-10, 5)   
        
    random_noise = np.random.uniform(-15, 15)
    daily_cost = round(base_cost + growth_trend + seasonality + random_noise, 2)
    usage_hours = int(np.random.randint(18, 25)) 
    
    data.append([date.strftime('%Y-%m-%d'), 'AWS Cloud Infrastructure', 'Engineering', daily_cost, usage_hours])

# 3. Convert to a Pandas DataFrame and save to CSV
df = pd.DataFrame(data, columns=['log_date', 'service_name', 'department', 'daily_cost', 'usage_hours'])
df.to_csv('historical_cloud_costs.csv', index=False)

print("\n🎉 SUCCESS! 'historical_cloud_costs.csv' has been created.")
print("-" * 50)
print("👀 HERE IS A PREVIEW OF THE DATA GENERATED:")
print("-" * 50)
print(df.head(10))  # This forces Python to print the first 10 rows on your screen
print("-" * 50)

# This stops the window from closing instantly if you double-clicked the file
input("\nPress ENTER to close this window...")
print("devesh")