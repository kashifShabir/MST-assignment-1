import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

# Function to read data from a CSV file
def read_data(filename):
    df = pd.read_csv(filename, header=None)
    timestamps = df[0]
    x_arr = df[1]
    y_arr = df[2]
    z_arr = df[3]
    return timestamps, x_arr, y_arr, z_arr

# Function to calculate the magnitude
def calculate_magnitude(x_arr, y_arr, z_arr):
    mag_arr = []
    for i in range(len(x_arr)):
        x = x_arr[i]
        y = y_arr[i]
        z = z_arr[i]
        m = np.linalg.norm((x, y, z))
        mag_arr.append(m)
    return mag_arr
# Function to calculate the dynamic threshold using a simple rolling average
def calculate_dynamic_threshold(mag_arr, window_size=50):
    threshold_values = []
    for i in range(len(mag_arr)):
        start = max(0, i - window_size)
        end = i + 1
        window = mag_arr[start:end]
        threshold = np.mean(window)
        threshold_values.append(threshold)
    return threshold_values

# Function to count steps with a dynamic threshold
def count_steps_with_dynamic_threshold(timestamps, mag_arr, threshold_values):
    steps = []
    
    for i in range(1, len(timestamps)):
        cur_val = mag_arr[i]
        prev_val = mag_arr[i - 1]
        threshold = threshold_values[i]
        
        if cur_val >= threshold and prev_val < threshold:
            steps.append(timestamps[i])
    
    return steps

# Function to plot data
def plot_data(timestamps, x_arr, y_arr, z_arr, mag_arr, threshold_values):
    plt.figure(1)
    plt.plot(timestamps, x_arr, color='pink', label='X')
    plt.plot(timestamps, y_arr, color='yellow', label='Y')
    plt.plot(timestamps, z_arr, color='green', label='Z')
    plt.legend()
    plt.xlabel('Timestamps')
    plt.ylabel('Acceleration')
    plt.title('Accelerometer Data')
    
    plt.figure(2)
    plt.plot(timestamps, mag_arr, color='red', label='Magnitude')
    plt.plot(timestamps, threshold_values, color='blue', label='Dynamic Threshold')
    plt.legend()
    plt.xlabel('Timestamps')
    plt.ylabel('Magnitude and threshold')
    plt.title('with Dynamic Threshold')
    
    plt.show()

def main():
    timestamps, x_arr, y_arr, z_arr = read_data("kashif.csv")
    mag_arr = calculate_magnitude(x_arr, y_arr, z_arr)
    
    window_size = 50
    threshold_values = calculate_dynamic_threshold(mag_arr, window_size=window_size)
    
    steps = count_steps_with_dynamic_threshold(timestamps, mag_arr, threshold_values)
    
    print('The timestamps at which steps were taken:', steps)
    print('Number of steps:', len(steps))
    
    plot_data(timestamps, x_arr, y_arr, z_arr, mag_arr, threshold_values)

if __name__ == "__main__":
    main()
