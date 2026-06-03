import sqlite3
import pandas as pd

conn = sqlite3.connect(
    "../Data/processed/olist_analytics.db"
)

query = """
SELECT
    customer_state,
    ROUND(SUM(revenue),2) AS total_revenue
FROM sales_data
GROUP BY customer_state
ORDER BY total_revenue DESC
LIMIT 10;
"""

result = pd.read_sql(query, conn)

print(result)

conn.close()