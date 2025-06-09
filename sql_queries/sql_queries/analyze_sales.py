import sqlite3
from datetime import datetime, timedelta

DB = 'sales.db'

# Query 1: Total sales for March 2024
QUERY_MARCH_TOTAL = """
SELECT SUM(amount) FROM orders
WHERE strftime('%Y-%m', order_date) = '2024-03';
"""

# Query 2: Top-spending customer
QUERY_TOP_CUSTOMER = """
SELECT customer, SUM(amount) as total_spent FROM orders
GROUP BY customer
ORDER BY total_spent DESC
LIMIT 1;
"""

# Query 3: Average order value for last 3 months (Jan-Mar 2024)
QUERY_AVG_ORDER = """
SELECT AVG(amount) FROM orders
WHERE order_date >= '2024-01-01' AND order_date <= '2024-03-31';
"""

def run_query(query):
    with sqlite3.connect(DB) as conn:
        cur = conn.cursor()
        cur.execute(query)
        return cur.fetchone()

def main():
    march_total = run_query(QUERY_MARCH_TOTAL)[0]
    top_customer, top_total = run_query(QUERY_TOP_CUSTOMER)
    avg_order = run_query(QUERY_AVG_ORDER)[0]

    print(f"Total sales for March 2024: {int(march_total):,}")
    print(f"Top-spending customer: {top_customer} ({int(top_total):,})")
    print(f"Average order value (Jan-Mar 2024): {int(avg_order):,}")

if __name__ == '__main__':
    main()
