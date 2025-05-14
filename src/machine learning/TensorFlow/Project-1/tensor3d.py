import tensorflow as tf
my_tensor = tf.constant(1,name="my_Scalar")
print(my_tensor)

with tf.Session() as sess:
    tensor_3d = tf.constant([
                            [[1, 4, 1],[1, 6, 8]],
                            [[4, 0, 1], [3, 5, 9]]
                            ])
    print(sess.run(tensor_3d))
