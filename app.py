from flask import Flask, render_template, request
from werkzeug import secure_filename
import os

app = Flask(__name__)

@app.route('/upload', methods = ['GET', 'POST'])
def upload_file():
	
	if request.method == 'POST':
		f = request.files['file']
		f.save(secure_filename(f.filename))
		try:
			file = open(f.filename, 'r')
			results = file.read()
		except:
			results = 'Error reading file'
		file.close()
		f.close()
		os.remove(f.filename)

		return results

	return render_template('upload.html')

if __name__ == '__main__':
	app.run(debug = False)