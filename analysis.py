import pandas as pd
import matplotlib.pyplot as plt

# Load CSV files
sales = pd.read_csv("sales.csv")
monthly = pd.read_csv("monthly.csv")
international = pd.read_csv("international.csv")
profit = pd.read_csv("profit.csv")

# Convert columns to numeric
cols = ["Flipkart MRP", "Limeroad MRP", "Myntra MRP", "Paytm MRP", "Snapdeal MRP"]

for col in cols:
    if col in monthly.columns:
        monthly[col] = pd.to_numeric(monthly[col], errors='coerce')
    if col in profit.columns:
        profit[col] = pd.to_numeric(profit[col], errors='coerce')

international["GROSS AMT"] = pd.to_numeric(international["GROSS AMT"], errors='coerce')

# Total Sales
print("Total Sales:", international["GROSS AMT"].sum())

# 1. Sales by Platform
monthly[cols].sum().plot(kind="bar", title="Sales by Platform")
plt.show()

# 2. Monthly Sales Trend
international.groupby("Months")["GROSS AMT"].sum().plot(kind="line", title="Monthly Sales Trend")
plt.show()


# Sales by Top 10 Customers
top_customers = international.groupby("CUSTOMER")["GROSS AMT"].sum().sort_values(ascending=False).head(10)
top_customers.plot(kind="bar", title="Top 10 Customers by Sales")
plt.show()

# 4. Profit Comparison
profit[cols].sum().plot(kind="bar", title="Profit Comparison by Platform")
plt.show()