import psutil
import time
import json

def get_system_utilization():
    utilization_data = {}
    
    # CPU Utilization
    utilization_data['cpu_percent'] = psutil.cpu_percent(interval=1)
    
    # Memory Utilization
    mem = psutil.virtual_memory()
    utilization_data['memory_percent'] = mem.percent
    
    # NIC Utilization
    net = psutil.net_io_counters()
    utilization_data['bytes_sent'] = net.bytes_sent
    utilization_data['bytes_recv'] = net.bytes_recv
    
    return utilization_data

def simulate_power_measurement(utilization):
    # Simulated power consumption in Watts
    # These formulas are placeholders and should be replaced with real measurement data
    power_cpu = utilization['cpu_percent'] * 0.5
    power_memory = utilization['memory_percent'] * 0.2
    power_nic = (utilization['bytes_sent'] + utilization['bytes_recv']) / 1e6 * 0.1  # Arbitrary factor

    total_power = power_cpu + power_memory + power_nic
    return {
        'power_cpu': power_cpu,
        'power_memory': power_memory,
        'power_nic': power_nic,
        'total_power': total_power
    }

def log_data(data, filename='utilization_log.json'):
    with open(filename, 'a') as f:
        json.dump(data, f)
        f.write('\n')

if __name__ == "__main__":
    while True:
        utilization = get_system_utilization()
        power = simulate_power_measurement(utilization)
        
        data_entry = {
            'timestamp': time.time(),
            'utilization': utilization,
            'power': power
        }
        
        log_data(data_entry)
        
        print(f"Logged data: {data_entry}")
        
        # Collect data every 5 seconds
        time.sleep(5)
