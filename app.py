#app.py

# Required imports
import os
# import sys
# import ast
import numpy
import cv2
from PIL import Image
from flask import Flask, request, jsonify, after_this_request

# Initialize Flask app
app = Flask(__name__)

@app.route('/classifier', methods=['POST'])
def classifier():
    try:
        @after_this_request
        def add_header(response):
            response.headers.add('Access-Control-Allow-Origin', '*')
            return response

        #read image file string data
        filestr = request.files['test_image'].read()
        #convert string data to numpy array
        npimg = numpy.frombuffer(filestr, numpy.uint8)
        # convert numpy array to image
        img = cv2.imdecode(npimg, cv2.IMREAD_UNCHANGED)

        #image shape
        print("image shape:", img.shape)
        # my_response = jsonify(shape=img.shape)
        # print(my_response)

        return jsonify(imageshape=img.shape)

    except Exception as e:
        return f"An Error Occured: {e}"


port = int(os.environ.get('PORT', 8080))
if __name__ == '__main__':
    # app.run(debug=True, threaded=True, host='0.0.0.0', port=port)
    app.run(debug=True, threaded=True, host='localhost', port=port)
