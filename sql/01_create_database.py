import pandas as pd
import sqlite3

master_df = pd.read_csv(
    "../Data/processed/master_dataset_featured.csv"
)

conn = sqlite3.connect(
    "../Data/processed/olist_analytics.db"
)

master_df.to_sql(
    "sales_data",
    conn,
    if_exists="replace",
    index=False
)

print("Database Created Successfully")

conn.close()