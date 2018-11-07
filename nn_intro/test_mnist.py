import numpy as np
import tensorflow as tf
from tensorflow.examples.tutorials.mnist import input_data



mnist = input_data.read_data_sets('/tmp/MNIST_data')

x,y = mnist.train.next_batch(10)

print y
