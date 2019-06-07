import tensorflow as tf
import numpy as np

with tf.Session() as sess:
    np_array = np.arange(0,5,step = 0.5)
    tensor_from_numpy = tf.constant(np_array, dtype=tf.float16)
    print (sess.run(tensor_from_numpy))
