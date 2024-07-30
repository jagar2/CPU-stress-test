import multiprocessing
import numpy as np
import time
import os

def cpu_stress_test(duration):
    """Function to perform intensive CPU operations for a given duration."""
    start_time = time.time()
    end_time = start_time + duration
    ops_count = 0
    
    while time.time() < end_time:
        # Perform intensive computation
        np.dot(np.random.random((1000, 1000)), np.random.random((1000, 1000)))
        ops_count += 1
    
    core_id = os.getpid()
    end_time = time.time()
    elapsed_time = end_time - start_time
    return core_id, ops_count, elapsed_time

if __name__ == "__main__":
    # Define the duration of the stress test in seconds
    test_duration = 10  # 10 seconds

    # Get the number of available CPU cores
    num_cores = multiprocessing.cpu_count()
    print(f"Using {num_cores} CPU cores")

    # Create a pool of worker processes
    pool = multiprocessing.Pool(processes=num_cores)

    # Start the stress test on all CPU cores
    results = pool.map(cpu_stress_test, [test_duration] * num_cores)

    # Close the pool and wait for all processes to finish
    pool.close()
    pool.join()

    # Generate the report
    total_operations = 0
    total_time = 0

    print("\nCPU Stress Test Report:")
    print(f"{'Core ID':<10}{'Operations':<15}{'Time (s)':<10}")
    print("-" * 35)

    for core_id, ops_count, elapsed_time in results:
        print(f"{core_id:<10}{ops_count:<15}{elapsed_time:<10.2f}")
        total_operations += ops_count
        total_time += elapsed_time

    avg_operations = total_operations / num_cores
    avg_time = total_time / num_cores

    print("\nSummary:")
    print(f"Total operations performed: {total_operations}")
    print(f"Total time taken (s): {total_time:.2f}")
    print(f"Average operations per core: {avg_operations:.2f}")
    print(f"Average time per core (s): {avg_time:.2f}")
    print("CPU stress test completed")
