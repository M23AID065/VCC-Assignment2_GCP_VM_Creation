import psutil
import time

def stress_cpu(cores=2, duration=30):
    print(f"Running CPU stress test on {cores} cores for {duration} seconds...")
    end_time = time.time() + duration
    while time.time() < end_time:
        [x**2 for x in range(10000)]

if __name__ == "__main__":
    cores = int(input("Enter number of CPU cores to use (default: 2): ") or 2)
    duration = int(input("Enter duration in seconds (default: 30): ") or 30)
    stress_cpu(cores, duration)
