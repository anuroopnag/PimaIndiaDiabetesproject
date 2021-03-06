# -*- coding: utf-8 -*-
"""PimaDiabetesProject

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1SHcqkKaN2f2P3CgST8KGKZFO_c95PTop
"""

from google.colab import files
uploaded = files.upload()

from pandas import read_csv
filename = "pima-indians-diabetes.data - pima-indians-diabetes.data.csv"
names = ['preg', 'plas', 'pres', 'skin', 'test', 'mass', 'pedi', 'age', 'class']
data = read_csv(filename, names=names)
data.head(20)

data.tail()

data.shape

data.dtypes

data.describe()

from pandas import set_option
set_option('display.width', 100)
set_option('precision', 3)
data.describe()

class_counts = data.groupby('class').size()
print(class_counts)

data.skew()

get_ipython().run_line_magic('matplotlib', 'inline')
from matplotlib import pyplot
data.hist()
pyplot.show()

data.plot(kind='density', subplots=True, layout=(3,3), sharex=False)
pyplot.show()

import numpy
correlations = data.corr()
fig = pyplot.figure()
ax = fig.add_subplot(111)
cax = ax.matshow(correlations, vmin=-1, vmax=1)
fig.colorbar(cax)
ticks = numpy.arange(0,9,1)
ax.set_xticks(ticks)
ax.set_yticks(ticks)
ax.set_xticklabels(names)
ax.set_yticklabels(names)
pyplot.show()

from pandas.plotting import scatter_matrix
scatter_matrix(data)
pyplot.show()

