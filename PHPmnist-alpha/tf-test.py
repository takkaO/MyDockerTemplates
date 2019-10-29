import os
import numpy as np
import tensorflow as tf
import cv2
import sys


def loadImage(path):
	img = cv2.imread(path, 0)	# gray scale
	return img.reshape(784)

def main(img_path):
	end = "<br/>"
	#end = "\n"
	input_image = loadImage(img_path)

	#initializer = tf.contrib.layers.variance_scaling_initializer()
	hidden_size = 50
	input_size = 784
	output_size = 10
	save_dir = "model"

	x = tf.placeholder(tf.float32, [None, input_size])
	y = tf.placeholder(tf.float32, [None, output_size])

	X = tf.reshape(x, shape=[-1, 28, 28, 1])
	X = tf.keras.layers.Conv2D(32, (3, 3), activation="relu")(X)
	X = tf.keras.layers.MaxPool2D()(X)
	X = tf.keras.layers.Flatten()(X)
	X = tf.keras.layers.Dense(hidden_size, activation="relu")(X)
	logits = tf.keras.layers.Dense(output_size)(X)

	loss = tf.nn.softmax_cross_entropy_with_logits_v2(
		logits=logits,
		labels=y
	)

	#opt = tf.train.GradientDescentOptimizer(0.00001).minimize(loss)  # SGD
	opt = tf.train.AdamOptimizer().minimize(loss)

	correct_prediction = tf.equal(tf.argmax(logits, 1), tf.argmax(y, 1))
	accurancy = tf.reduce_mean(tf.cast(correct_prediction, tf.float32))

	init = tf.global_variables_initializer()

	#print("Train start")
	with tf.Session() as sess:
		if os.path.exists("./" + save_dir + "/test_model.index"):
			print("Load model", end=end)
			saver = tf.train.Saver()
			saver.restore(sess, "./" + save_dir + "/test_model")
		else:
			print("Error load model!", end=end)
			exit(1)

		result = sess.run(tf.nn.softmax(logits), feed_dict={x: [input_image]})
		max_index = sess.run(tf.argmax(result, 1))
		print("Number     : ", max_index[0], end=end)
		print("Probability: ", result[0][max_index][0]*100.0, " %", end=end)
		

if __name__ == "__main__":
	os.environ['TF_CPP_MIN_LOG_LEVEL'] = '3'
	tf.reset_default_graph()
	main(sys.argv[1])
