# 指定行列全零矩阵
from numpy import zeros, ones
print(zeros((3, 2)))
# 全一
print(ones((3, 2)))
import tensorflow as tf
_x = tf.Variable(tf.zeros([2, 3]))
init = tf.global_variables_initializer()
with tf.Session() as sess:
  sess.run(init)
  result = sess.run(_x)
  print(result)
