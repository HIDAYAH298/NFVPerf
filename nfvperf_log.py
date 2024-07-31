import pandas as pd
from datetime import datetime, timedelta

# Generate sample data
timestamps = [datetime(2023, 7, 29, 12, 0, 0) + timedelta(seconds=5*i) for i in range(10)]
latencies = [10 + i for i in range(10)]
throughputs = [100 - i for i in range(10)]

# Create a DataFrame
data = pd.DataFrame({
    'timestamp': timestamps,
    'latency': latencies,
    'throughput': throughputs
})

# Save to CSV
log_file = '/var/log/nfvperf.log'
data.to_csv(log_file, index=False)
print(f"Sample log file saved to {log_file}")
