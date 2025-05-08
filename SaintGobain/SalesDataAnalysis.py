import pandas as pd
import numpy as np

# Random seed for reproducibility
np.random.seed(42)

# Sample data
product_ids = ['P001', 'P002', 'P003', 'P004', 'P005']
stores = ['Store A', 'Store B', 'Store C', 'Store D']
promotion_types = ['Discount', 'Buy One Get One Free', 'Flash Sale', 'No Promotion']
days_of_week = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']

# Generate data
data = {
    'product_id': np.random.choice(product_ids, 10000),
    'store_location': np.random.choice(stores, 10000),
    'promotion_type': np.random.choice(promotion_types, 10000),
    'sales': np.random.randint(100, 1000, size=10000),
    'day_of_week': np.random.choice(days_of_week, 10000),
    'date': pd.date_range(start='2022-01-01', periods=10000, freq='D')
}

# Create the DataFrame
df = pd.DataFrame(data)
print(df)
