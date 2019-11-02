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

    # Scale columns using normal transform
    scaler = StandardScaler()
    df[df.columns] = scaler.fit_transform(df[df.columns])
    df.dropna(inplace = True)

    # cluster and plot
    clusters = hierarchy.fclusterdata(df[['Temperature', 'Rainfall']], 1, criterion="distance")
    kmeans = KMeans(n_clusters=5, random_state=0).fit(df[['Temperature', 'Humidity', 'Pressure']])
    fig = plt.figure()
    ax = Axes3D(fig)
    ax.scatter(df['Temperature'], df['Humidity'], df['Pressure'], c=kmeans.labels_)
    plt.show()