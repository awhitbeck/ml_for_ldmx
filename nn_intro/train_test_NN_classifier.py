#!/usr/bin/env python

"""TensorFlow MNIST classifier
Description simple NN to classify MNIST digits
Author: Andrew Whitbeck
Date: Nov 7 2018
"""

import sys
import numpy as np
import tensorflow as tf
from tensorflow.examples.tutorials.mnist import input_data

IMAGE_SIZE = 28*28
BATCH_SIZE = 500
NEURONS_PER_LAYER = 200
#HIDDEN_LAYERS = 2

def weight_variable(shape):
    # From the mnist tutorial
    initial = tf.truncated_normal(shape, stddev=0.1)
    return tf.Variable(initial)

def bias_variable(shape):
    initial = tf.constant(0.1, shape=shape)
    return tf.Variable(initial)

def fc_layer(previous, input_size, output_size):
    W = weight_variable([input_size, output_size])
    b = bias_variable([output_size])
    return tf.matmul(previous, W) + b

def neural_network(x):
    # first fully connected layer using tanh activation
    l1 = tf.nn.tanh(fc_layer(x, IMAGE_SIZE, NEURONS_PER_LAYER))
    # second fully connected layer using tanh activation
    l2 = tf.nn.tanh(fc_layer(l1, NEURONS_PER_LAYER, NEURONS_PER_LAYER))
    # third fully connected layer using tanh activation
    l3 = tf.nn.tanh(fc_layer(l2, NEURONS_PER_LAYER, NEURONS_PER_LAYER))
    # fourth fully connected layer using tanh activation
    l4 = tf.nn.tanh(fc_layer(l3, NEURONS_PER_LAYER, NEURONS_PER_LAYER))
    # output layer with 10 neurons using sigmoid activation
    out = tf.nn.sigmoid(fc_layer(l2, NEURONS_PER_LAYER, 10))
    return out

def compute_loss(x,y):
    # let's use an l2 loss on the output image
    loss = tf.reduce_mean(tf.nn.softmax_cross_entropy_with_logits_v2(logits=x,labels=y))
    return loss

def main(train=True):
    # initialize the data
    mnist = input_data.read_data_sets('/tmp/MNIST_data',one_hot=True)

    # placeholders for the images
    x = tf.placeholder(tf.float32, shape=[None, IMAGE_SIZE])
    y = tf.placeholder(tf.int64, shape=[None, 10])
    
    # build the model
    output = neural_network(x)
    loss = compute_loss(output,y)

    # and we use the Adam Optimizer for training
    train_step = tf.train.AdamOptimizer(1e-4).minimize(loss)

    # init saver
    saver = tf.train.Saver()

    correct_pred = tf.equal(tf.argmax(output, 1), tf.argmax(y, 1))
    accuracy = tf.reduce_mean(tf.cast(correct_pred, tf.float32))

    # Run the training loop
    with tf.Session() as sess:

        if train :
            print "[[[ TRAINING ]]]"
            sess.run(tf.global_variables_initializer())
            for i in range(20001):
                batch_x,batch_y = mnist.train.next_batch(BATCH_SIZE)
                feed = {x : batch_x, y : batch_y}
                if i % 500 == 0:
                    train_loss = sess.run(loss,
                            feed_dict=feed)
                    print("step %d, training loss: %g" % (i, train_loss))

                train_step.run(feed_dict=feed)

            saver.save(sess,'/tmp/nn_model.ckpt')
        else :
            print "[[[ TESTING ]]]"
            saver.restore(sess, "/tmp/nn_model.ckpt")
            batch_x=mnist.test.images
            batch_y=mnist.test.labels
            feed = {x:batch_x,y:batch_y}
            test_loss,test_accuracy = sess.run([loss,accuracy],feed_dict=feed)
            print("training loss: %g" % (test_loss))
            print "accuracy: ",test_accuracy

if __name__ == '__main__':
    main(int(sys.argv[1]))
