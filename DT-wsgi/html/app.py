from flask import Flask, request, render_template
import numpy as np
import base64
import cv2

def loadimg(img_path):
	img = cv2.imread(img_path, cv2.IMREAD_COLOR)
	return img

app = Flask(__name__)

@app.route("/")
def hello():
	#img = loadimg("0038.jpg")
	#img = np.zeros((5, 5, 3)) # 単色画像を作成
	#test = base64.b64encode(img).decode('utf-8')
	
	with open("./imgs/car.jpg", "rb") as b:
		test = base64.b64encode(b.read()).decode('utf-8')
	#print(test)
	#return render_template("index.html", test_var=test)
	return render_template("index.html")


@app.route('/postText', methods=['POST'])
def lower_conversion():
	print(request.json['text'])
	return "unko"

@app.route("/test")
def hogehoge():
	return "TEST STRING"

if __name__ == "__main__":
	app.run()
