import json
import matplotlib.pyplot as plt

def read_data(filename='utilization_log.json'):
    with open(filename, 'r') as f:
        lines = f.readlines()
        data = [json.loads(line) for line in lines]
    return data

def plot_data(data):
    timestamps = [entry['timestamp'] for entry in data]
    cpu_power = [entry['power']['power_cpu'] for entry in data]
    memory_power = [entry['power']['power_memory'] for entry in data]
    nic_power = [entry['power']['power_nic'] for entry in data]
    total_power = [entry['power']['total_power'] for entry in data]

    plt.figure(figsize=(10, 5))
    
    plt.plot(timestamps, cpu_power, label='CPU Power (W)')
    plt.plot(timestamps, memory_power, label='Memory Power (W)')
    plt.plot(timestamps, nic_power, label='NIC Power (W)')
    plt.plot(timestamps, total_power, label='Total Power (W)', linestyle='--')

    plt.xlabel('Timestamp')
    plt.ylabel('Power (Watts)')
    plt.legend()
    plt.show()

if __name__ == "__main__":
    data = read_data()
    plot_data(data)
