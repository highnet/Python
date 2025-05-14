import tensorflow as tf
my_tensor = tf.constant(1,name="my_Scalar")
print(my_tensor)

with tf.Session() as sess:
    tensor_2d_with_strings = tf.constant([["Petra", "Schmitt"],
                                          ["Max", "Mustermann"],
                                          ["John","Doe"]])
    print(sess.run(tensor_2d_with_strings))
