import multiprocessing
import numpy as np
import time

def cpu_stress_test(duration):
    """Function to perform intensive CPU operations for a given duration."""
    end_time = time.time() + duration
    while time.time() < end_time:
        # Perform intensive computation
        np.dot(np.random.random((1000, 1000)), np.random.random((1000, 1000)))

if __name__ == "__main__":
    # Define the duration of the stress test in seconds
    test_duration = 10  # 10 seconds

    # Get the number of available CPU cores
    num_cores = multiprocessing.cpu_count()
    print(f"Using {num_cores} CPU cores")

    # Create a pool of worker processes
    pool = multiprocessing.Pool(processes=num_cores)

    # Start the stress test on all CPU cores
    pool.map(cpu_stress_test, [test_duration] * num_cores)

    # Close the pool and wait for all processes to finish
    pool.close()
    pool.join()

    print("CPU stress test completed")