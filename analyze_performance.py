import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Path to the log file generated by NFVPerf
log_file = '/var/log/nfvperf.log'

# Read the log file into a DataFrame
data = pd.read_csv(log_file)

# Display the first few rows of the data to understand its structure
print(data.head())

# Generate a summary table for the performance metrics
performance_table = data.describe()
print(performance_table)

# Save the summary table to a CSV file
performance_table.to_csv('performance_summary.csv')

# Plotting the performance metrics
plt.figure(figsize=(14, 7))

# Latency plot
plt.subplot(1, 2, 1)
sns.lineplot(x='timestamp', y='latency', data=data)
plt.title('Latency Over Time')
plt.xlabel('Time')
plt.ylabel('Latency (ms)')

# Throughput plot
plt.subplot(1, 2, 2)
sns.lineplot(x='timestamp', y='throughput', data=data)
plt.title('Throughput Over Time')
plt.xlabel('Time')
plt.ylabel('Throughput (Mbps)')

# Save the plots as an image file
plt.savefig('performance_metrics.png')
plt.show()
