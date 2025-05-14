
import tensorflow as tf
hello = tf.constant('Hello World!')
sess = tf.Session()
print(sess.run(hello))
print("TensorFlow Version:{} ".format(tf.__version__))
