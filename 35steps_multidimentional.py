#importing libraries to use
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

# Function to count steps
def count_steps(timestamps, mag_arr, threshold=11):
    steps = []
    pre_val = mag_arr[0]
    
    for i in range(1, len(timestamps)):
        cur_val = mag_arr[i]
        if cur_val >= threshold and pre_val < threshold:
            steps.append(timestamps[i])
        pre_val = cur_val
    
    return steps

# Function to plot data
def plot_data(timestamps, x_arr, y_arr, z_arr, mag_arr):
    plt.figure(1)
    plt.plot(timestamps, x_arr, color='pink', label='X')
    plt.plot(timestamps, y_arr, color='yellow', label='Y')
    plt.plot(timestamps, z_arr, color='green', label='Z')
    plt.title('Acceleration Data')
    plt.show()
    plt.figure(2)
    plt.plot(timestamps, mag_arr, color='red', label='Magnitude')
    plt.title('Magnitude of Data')
    plt.show()

def main():
    timestamps, x_arr, y_arr, z_arr = read_data("kashif.csv")
    mag_arr = calculate_magnitude(x_arr, y_arr, z_arr)
    steps = count_steps(timestamps, mag_arr)
    
    print('The timestamps at which steps were taken:', steps)
    print('Number of steps:', len(steps))
    plot_data(timestamps, x_arr, y_arr, z_arr, mag_arr)

if __name__ == "__main__":
    main()
