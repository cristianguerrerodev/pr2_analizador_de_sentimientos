
from flask import Flask,render_template,url_for,request
from flask import Flask, render_template, request
from werkzeug.utils import secure_filename
import nltk
from nltk.sentiment.vader import SentimentIntensityAnalyzer
from sentiment_analysis_spanish import sentiment_analysis
nltk.download('vader_lexicon')

app = Flask(__name__)

@app.route('/')
def index():
	return render_template("index.html")

@app.route('/process',methods=["POST"])
def process():
	if request.method == 'POST':
		taskoption = request.form['taskoption']
		rawtext = request.form['rawtext']
		results = []

		if taskoption == 'english':
			sid = SentimentIntensityAnalyzer()
			result_dic = sid.polarity_scores(rawtext)
			results = []
		
			for key in result_dic:
				results.append(f'{key}: {result_dic[key]}')
		elif taskoption == 'spanish':
			sentiment = sentiment_analysis.SentimentAnalysisSpanish()
			results.append(f'Puntuación: {sentiment.sentiment(rawtext)}')

	return render_template("index.html",results=results)

if __name__ == '__main__':
	app.run(debug=True)