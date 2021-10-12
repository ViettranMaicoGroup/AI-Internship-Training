import numpy as np
import pandas as pd

def load_df(path):
    try:
        return pd.read_csv(path)
    except Exception:
        print("Something went wrong! No such file!")
        return

def print_array(arr):
    active = {}
    for i in range(len(arr)):
        if arr[i] > 100:
            active[i] = arr[i]
    return active

if __name__ == "__main__":
    df =  load_df("Machine_Learning_Libraries\\dataset.csv")
    #a
    print(df[:50])
    #b
    print(df.iloc[:, 1:4])
    #c
    active_minutes = df.iloc[:, 4]
    print(active_minutes)

    active_minutes_array = np.array(active_minutes)
    print(active_minutes_array)
    print(print_array(active_minutes_array))