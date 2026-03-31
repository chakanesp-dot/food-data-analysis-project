import sqlite3
import pandas as pd

print("Starting SQL Analysis...\n")

# Load CSV
data = pd.read_csv("food_sales_data.csv")

# Create database
conn = sqlite3.connect("food_sales.db")

# Save data into SQL table
data.to_sql("food_sales", conn, if_exists="replace", index=False)

print("Database created successfully!\n")

# Query 1: Sales by Category
query1 = """
SELECT Category, SUM(Sales) as Total_Sales
FROM food_sales
GROUP BY Category
"""
print("Sales by Category:\n")
print(pd.read_sql(query1, conn))

# Query 2: Top Selling Products
query2 = """
SELECT Product, Sales
FROM food_sales
ORDER BY Sales DESC
"""
print("\nTop Selling Products:\n")
print(pd.read_sql(query2, conn))

# Query 3: High Sugar Products
query3 = """
SELECT Product, Sugar
FROM food_sales
WHERE Sugar > 25
"""
print("\nHigh Sugar Products:\n")
print(pd.read_sql(query3, conn))

conn.close()

print("\nSQL Analysis Completed!")
