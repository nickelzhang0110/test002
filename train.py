
import time
import tensorflow as tf
print('tensorflow version: ', tf.__version__)

for i in range(300):
  print('training: {}/300'.format(i))
  time.sleep(1)


