#app.py

# Required imports
import os
import sys
import ast
from PIL import Image
from flask import Flask, request, jsonify

# Initialize Flask app
app = Flask(__name__)

@app.route('/classifier', methods=['POST'])
def classifier():
    try:
        # targetUrl = request.json['targetUrl']
        # objectData = request.data['objectData']
        # app.logger.info("object data found:", objectData)
        # print(request.data)
        # byte_str = request.data
        # dict_str = byte_str.decode("UTF-8")
        # mydata = ast.literal_eval(dict_str)
        #
        # target_image = mydata['imageUrl']
        # object_data = mydata['objectData']
        # print("Image location:", target_image)
        # print("Object data:", object_data)

        return jsonify({"success": True}) , 200
    except Exception as e:
        return f"An Error Occured: {e}"

    # input_bucket = './images/'
    # output_bucket = './output'
    #
    # if len(sys.argv) != 3:
    #     print('Requires Usage: watermark.py \'image file\' \'logo file \'')
    #     sys.exit()
    # else:
    #     input_image = sys.argv[1]
    #     lgo = sys.argv[2]
    #
    # # Download logo
    # logo = Image.open(lgo)
    # logoWidth = logo.width
    # logoHeight = logo.height
    #
    # # Grab photo name
    # filename = str(input_image.replace(input_bucket, ''))
    #
    # # Download photo
    # image = Image.open(input_image)
    # imageWidth = image.width
    # imageHeight = image.height
    #
    # # Modify and save photo
    # try:
    #     image.paste(logo, (int((imageWidth - logoWidth)/2), int((imageHeight - logoHeight)/2)), logo)
    #     image.save(output_bucket + '/watermark_' + filename)
    #     print('SUCCESS')
    #
    # except:
    #     image.paste(logo, (int((imageWidth - logoWidth)/2), int((imageHeight - logoHeight)/2)), logo)
    #     image.save(output_bucket + '/watermark_'  + filename)
    #     print('FAILURE')
    # return 'Hello World from Python Flask!'

port = int(os.environ.get('PORT', 8080))
if __name__ == '__main__':
    app.run(debug=True, threaded=True, host='0.0.0.0', port=port)
