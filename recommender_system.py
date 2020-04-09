import tensorflow as tf
from tensorflow.keras.layers import Input, Dense, Embedding, Flatten, Concatenate
from tensorflow.keras.models import Model
from tensorflow.keras.optimizers import SGD, Adam

from sklearn.utils import shuffle

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

import requests

url = 'http://files.grouplens.org/datasets/movielens/ml-20m.zip'
r = requests.get(url, allow_redirects=True)