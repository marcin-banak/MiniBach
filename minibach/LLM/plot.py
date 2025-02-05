import json
import matplotlib.pyplot as plt
import numpy as np


def plot(path):
    load = json.load(open(path))
    print(len(load))
    plt.xlabel("Epochs")
    plt.ylabel("Loss")

    x = [i * 100 for i in range(len(load))]
    plt.plot(x, load)
    plt.show()


def plot_gpt2(path):
    losses = []
    with open(path, "r") as f:
        file = f.readlines()
        for line in file:
            splited = line.split(" ")
            if "loss" in splited[0]:
                losses.append(float(splited[1].replace(",", "")))
    x = [i * 20 for i in range(len(losses))]
    plt.plot(x, losses)
    plt.xlabel("Epochs")
    plt.ylabel("Loss")
    plt.show()


plot("eval/losses_6.json")
# plot_gpt2("eval/gpt2.txt")
