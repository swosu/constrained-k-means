# General imports. 
import numpy as np
import pandas as pd

# You have to adapt this 3 variables to your specific case.
num_clusters = 7
filename = "zoo.data.csv"
name_of_first_column_to_be_ignored = 'animal name'

# Read the CSV file with the Pandas lib.
path_dir = "//home//tohka//Desktop//constrained-k-means"
dataframe = pd.read_csv( path_dir + filename, encoding = "cp1252", sep = ';' ) # "ISO-8859-1")
df = dataframe.copy(deep=True)
# df.head(5)[df.columns[0:4]]
df.head(5)



# Prepares the dataset to delete the columns that aren't used:
#  'animal name'
#
#  Replaces the 'X' by 1.0 and the NAN for 0.0 making something like hot encoding.

if name_of_first_column_to_be_ignored in df.columns:
    df = df.drop(name_of_first_column_to_be_ignored, 1)

#df = df.replace(to_replace="X", value=1.0)
#df = df.fillna(0.0)   # Fill the NAN (Not a Num)
df.head(5)



# Apply the K-Means Clustering algoritms.
from sklearn.cluster import KMeans

#num_clusters = 7

km = KMeans(n_clusters=num_clusters, random_state=1)
new = df._get_numeric_data()
km.fit(new)
predict=km.predict(new)
df_kmeans = df.copy(deep=True)
df_kmeans['Cluster KMeans'] = pd.Series(predict, index=df_kmeans.index)
df_kmeans.head(20)

# Saving to kmeans CSV file.

# Gets the original data frame and adds to it one column in the end with the id of the cluster.

df_kmeans_orig = dataframe.copy(deep=True)
df_kmeans_orig['Cluster KMeans'] = pd.Series(predict, index=df_kmeans.index)

# Because we would like to have the column in the begining of the table, in the
# second position to facilitates comparisions.
# We are going to alter the order of the columns with a neat trick!
cols = df_kmeans_orig.columns.tolist()
cols = cols[0:1] + [cols[-1]] + cols[1:-2]
df_kmeans_orig = df_kmeans_orig[cols]


df_kmeans_orig = df_kmeans_orig.fillna("")           # assigns df to a new dataframe

filename_kmenas = filename[0:-4] + "_kmeans_" + str(num_clusters) + ".csv"
path_kmeans = path_dir + filename_kmenas
df_kmeans_orig.to_csv(path_or_buf = path_kmeans, sep = ";")
print("The file was generated!")

# Implementation of the Elbow method for KMeans.
# This method discover in a "scientific" way the best number of cluster to specify to the KMeans algorithm.

from sklearn.cluster import KMeans

#matplotlib inline

import matplotlib
import matplotlib.pyplot as plt

Ks = range(1, 25)
km = [KMeans(n_clusters=i, random_state=1) for i in Ks]
my_matrix = df._get_numeric_data()
score = [km[i].fit(my_matrix).score(my_matrix) for i in range(len(km))]

plt.plot(Ks, score)
plt.show()
