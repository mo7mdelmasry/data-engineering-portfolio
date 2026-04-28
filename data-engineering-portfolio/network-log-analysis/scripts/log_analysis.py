import pandas as pd

# Load data
df = pd.read_csv('../data/network_logs.csv')

# Clean data
df = df.dropna()

# Top IPs
top_ips = df['source_ip'].value_counts()

print(top_ips)