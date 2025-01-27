import numpy as np
import os
import pandas as pd
import matplotlib.pyplot as plt
from evaluation import get_range_proba
from sklearn.metrics import f1_score, precision_score, recall_score
def plot_points(file, result1, result2, version1, version2):
    data = pd.read_csv(file)#.iloc[60:, :]
    r1 = pd.read_csv(result1)
    r2 = pd.read_csv(result2)

    data["time"] = pd.to_datetime(data["timestamp"], unit='s')
    plt.figure(figsize=(19.2, 13.4), dpi=80)
    plt.subplot(2, 1, 1)
    plt.title(file.split("/")[-1])
    plt.plot(data["time"].values, data["value"].values)
    plt.scatter(data[ data["anomaly"] == 1]["time"], data[ data["anomaly"] == 1 ]["value"], c = "red", s = 110, label = "ground truth")

    data.index = data["timestamp"]
    data = data.loc[r2["timestamp"][0]:, :]
    data.index = range(len(data))

    r1["anomaly"] = get_range_proba(r1["anomaly"].values, data["anomaly"].values)
    r2["anomaly"] = get_range_proba(r2["anomaly"].values, data["anomaly"].values)


    plt.axvline(x=data.loc[0, "time"],ls="-",c="green")
    plt.axhline(y=np.median(data["value"].values), ls="-", c="purple")
    plt.scatter(data[r1["anomaly"] == 1]["time"], data[r1["anomaly"] == 1]["value"], c = "greenyellow", s = 80, label = version1)
    plt.scatter(data[r2["anomaly"] == 1]["time"], data[r2["anomaly"] == 1]["value"], c="black", s=50, label=version2)
    plt.legend()
    plt.subplot(2, 1, 2)
    plt.axvline(x=data.loc[0, "time"], ls="-", c="green")
    data = pd.read_csv(file)
    data["time"] = pd.to_datetime(data["timestamp"], unit='s')
    co_disp = list(r1["score"])
    co_disp = [0.0] * (len(data) - len(r1)) + co_disp
    plt.plot(data["time"].values, co_disp)

    plt.savefig("./contest_pic/" + file.split("/")[-1] + ".jpg")
if __name__ == "__main__":
    dir = "../3.11/"
    version1 = "IF"
    version2 = "IF"
    for file in os.listdir("../contest_data/"):
        plot_points("../contest_data/"+file,
                    dir + version1 + "/test-" + version1 + file,
                    dir + version2 + "/test-" + version2 + file, version1, version2)



