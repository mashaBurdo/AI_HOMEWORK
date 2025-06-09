import sqlite3

# Create and populate the orders table
def setup_database():
    conn = sqlite3.connect('sales.db')
    c = conn.cursor()
    c.execute('''
        CREATE TABLE IF NOT EXISTS orders (
            id INTEGER PRIMARY KEY,
            customer TEXT,
            amount REAL,
            order_date DATE
        )
    ''')
    c.execute('DELETE FROM orders')  # Clear table if rerun
    c.executemany('''
        INSERT INTO orders (customer, amount, order_date) VALUES (?, ?, ?)
    ''', [
        ('Alice', 5000, '2024-03-01'),
        ('Bob', 8000, '2024-03-05'),
        ('Alice', 3000, '2024-03-15'),
        ('Charlie', 7000, '2024-02-20'),
        ('Alice', 10000, '2024-02-28'),
        ('Bob', 4000, '2024-02-10'),
        ('Charlie', 9000, '2024-03-22'),
        ('Alice', 2000, '2024-03-30'),
    ])
    conn.commit()
    conn.close()

if __name__ == '__main__':
    setup_database()
    print('Database setup complete.')
