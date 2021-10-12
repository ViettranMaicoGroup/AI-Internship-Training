import numpy as np
import pandas as pd

def load_df(path):
    try:
        return pd.read_csv(path)
    except Exception:
        print("Something went wrong! No such file!")
        return
if __name__ == "__main__":
    df =  load_df("Machine_Learning_Libraries\\dataset.csv")
    #a
    print(df[:50])
    #b
    print(df.iloc[:, 1:4])
    #c
    active = {}
    active_minutes = df.iloc[:, 4]
    # print(active_minutes)
    active_minutes_array = np.array(active_minutes)
    print(active_minutes_array)
    for i in range(len(active_minutes_array)):
        if active_minutes_array[i] > 100:
            active[i] = active_minutes_array[i]
    print(active)