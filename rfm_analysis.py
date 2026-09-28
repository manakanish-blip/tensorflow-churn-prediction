import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# 1. GENERATE A REALISTIC "DIRTY" DATASET
# This simulates a messy Excel sheet an employer might hand you
dirty_data = {
    'Transaction_ID': [101, 102, 103, 104, 104, 105, 106, 107, 108, 109], # 104 is duplicated
    'Store_Region': ['North', 'South', 'East', 'West', 'West', 'North', np.nan, 'East', 'South', 'West'], # Missing value
    'Order_Date': ['2026-01-10', '12-02-2026', '2026-03-15', '2026-04-20', '2026-04-20', '2026-05-02', '2026-05-14', '06/01/2026', '2026-06-10', '2026-06-15'], # Inconsistent formats
    'Revenue': [5000, 7500, np.nan, 3200, 3200, 9100, 4300, 6200, np.nan, 8800] # Missing values
}

df = pd.DataFrame(dirty_data)
print("--- ❌ MESSY RAW DATA ---")
print(df)
print("\n" + "="*60 + "\n")

# 2. THE DATA CLEANING PHASE
# Step A: Remove exact duplicate rows
df = df.drop_duplicates()

# Step B: Handle missing values
# For Store_Region, we fill the missing value with 'Unknown'
df['Store_Region'] = df['Store_Region'].fillna('Unknown')

# For Revenue, we fill missing values with the median revenue of the stores so it doesn't skew trends
median_revenue = df['Revenue'].median()
df['Revenue'] = df['Revenue'].fillna(median_revenue)

# Step C: Fix inconsistent date formats into standard YYYY-MM-DD format
df['Order_Date'] = pd.to_datetime(df['Order_Date'], errors='coerce', format='mixed')

print("---  CLEANED DATASET ---")
print(df)
print("\n" + "="*60 + "\n")

# 3. DATA AGGREGATION & TREND ANALYSIS
# Extract Month from our clean date column to find Monthly Growth
df['Month'] = df['Order_Date'].dt.strftime('%B')

# Group by month and sum the revenue
monthly_sales = df.groupby('Month', sort=False)['Revenue'].sum().reset_index()

print("--- 📈 MONTHLY SALES PERFORMANCE TREND ---")
print(monthly_sales)

# 4. DATA VISUALIZATION
# Plotting the clean trend using Matplotlib
plt.figure(figsize=(8, 4))
plt.plot(monthly_sales['Month'], monthly_sales['Revenue'], marker='o', color='#1a365d', linewidth=2)
plt.title('Store Revenue Trend Analysis (2026)', fontsize=12, fontweight='bold', color='#1a365d')
plt.xlabel('Month', fontsize=10)
plt.ylabel('Total Revenue (INR)', fontsize=10)
plt.grid(axis='y', linestyle='--', alpha=0.7)

# Save the visualization as an image to upload to GitHub
plt.savefig('monthly_revenue_trend.png', dpi=300, bbox_inches='tight')
print("\n[Success] Visualization saved as 'monthly_revenue_trend.png'")