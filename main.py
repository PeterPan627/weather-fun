import requests
import csv
import xarray
import os
import pandas
import numpy as np
from sklearn.preprocessing import StandardScaler
from scipy.cluster import hierarchy
from helper_functions import *
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans
from mpl_toolkits.mplot3d import Axes3D

if __name__ == "__main__":

    # Import dataframe
    df = import_data()

    # Fix the units
    fix_units(df)

    # Transform the sunlight column
    normalise_sun(df)
    df['Sunshine'] = df['Sunshine'].clip(0.0, 1.0)
    df['MaxWindSpeed'] = df['MaxWindSpeed'].clip(0.0, 75.0)

    df.dropna(inplace = True)

    # Scale columns using normal transform
    scaler = StandardScaler()
    dfscaled = df.copy()
    dfscaled[df.columns] = scaler.fit_transform(df[df.columns])

    # cluster and plot
    keys = ['Rainfall', 'Sunshine', 'MaxWindSpeed']

    kmeans = KMeans(n_clusters=5, random_state=0).fit(dfscaled[keys])
    fig = plt.figure()
    ax = Axes3D(fig)
    ax.scatter(*(df[i] for i in keys), c=kmeans.labels_)
    ax.set_xlabel(keys[0])
    ax.set_ylabel(keys[1])
    ax.set_zlabel(keys[2])
    plt.show()
