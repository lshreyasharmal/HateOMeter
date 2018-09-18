import numpy as np
from sklearn.linear_model import LogisticRegression
from stop_words import get_stop_words
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.svm import LinearSVC
from sklearn import svm
from sklearn.neural_network import MLPClassifier
import re
from nltk.corpus import stopwords
import nltk
from stop_words import get_stop_words
from sklearn.naive_bayes import GaussianNB
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer as VS


nltk.download ('stopwords')
stop_words = get_stop_words('en')
gnb = GaussianNB()
analyzer = VS()

stopwords_list = stopwords.words('english') + stopwords.words('portuguese')
tvd = TfidfVectorizer(analyzer='word',
                     ngram_range=(1, 3),
                     min_df=0.003,
                     max_df=0.01,
                     max_features=5000,
                     norm='l1',
                     # smooth_idf=0,
                     stop_words=stopwords_list)

htmlRegex = re.compile(r'([a-z]*>)')

Spl_char = [",","-",".",";",">","<","=","&",":","#","!"]

def get_features(trainX):
	new_comments = tvd.fit_transform(trainX)
	return new_comments




def train(trainX,trainY,Test,count):
	new_comments = get_features(trainX)
	new_comments = new_comments.toarray()
	model = svm.LinearSVC(random_state=0,C=0.35)
	# model = MLPClassifier(hidden_layer_sizes=(100,50),
	#   activation='relu', max_iter=100, verbose=10, alpha=1e-4, 
	#   solver='sgd',tol=1e-4, random_state=1,  learning_rate_init=.1)
	# gnb.fit(new_comments,trainY)

	model = model.fit(new_comments,trainY)
	print new_comments
	print trainY
	tes = tvd.transform(Test)
	tes = tes.toarray()
	result = model.predict(tes)
	# result = gnb.predict(tes)
	#We need to calculate the score here
	num_ones=0
	for i in range(len(result)):
		if(result[i]=="1"):
			num_ones+=1
		print "predicted = " + result[i] + " " + Test[i]
	score = ((num_ones*1.0)*100)/count
	print "Score: " + str(score)
	return score 



def runningFunc(test_data):
	

	#Test Data Created
	Test=[]
	TempTest = []
	count =0
	negCount = 0
	for item in test_data['table']:
		
		# print(item['id'], item['message'])
		if(re.search(htmlRegex,item['message'])):
			continue
		else:
			count+=1
			# Test.append(item['message'].strip())
			TempTest.append(item['message'].strip())

			# try vader
			# vs = analyzer.polarity_scores(item['message'])
			# print item['message'].strip() , "   ", vs['compound']

	for testD in TempTest:
		tempTest = ""
		testSplit = testD.split()
		for word in testSplit:
			for sp in Spl_char:
				word = word.replace(sp,"")
			if word not in stop_words:
				tempTest+=word+" "
			
		tempTest = tempTest.strip()
		# try vader
		vs = analyzer.polarity_scores(tempTest)
		print tempTest , "  " , vs['compound']
		if (vs['compound']<-0.5):	
			negCount+=1

		Test.append(tempTest)


	#Training Set
	with open ('/home/shreya/Desktop/hate_o_meter/static/shreya.txt','r') as mfile:
		content = mfile.readlines()
	trainY = []
	zero = []
	ones = []
	num0 = 0
	num1 = 0
	trainX = []

	for line in content:
		line = line.strip()
		line = line.split(',')
		tempStr = ""
		lineSplit = line[1].split()
		for word in lineSplit:
			for sp in Spl_char:
				# print sp
				word = word.replace(sp,"")
			if word not in stop_words:
				tempStr=tempStr+word+" "
			

		tempStr = tempStr.strip()
		# print tempStr



		if(line[2]=='0'):
			zero.append(tempStr)
			num0+=1
		else:
			ones.append(tempStr)
			num1+=1
	# print str(num1)+ " ppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppp"

	for i in range(458):
		trainX.append(zero[i])
		if(i%1==0): 
			trainX.append(ones[i])
		trainY.append('0')
		if(i%1==0):
			trainY.append('1')

	trainY = np.array(trainY)
	trainX = np.array(trainX)
	# print trainX
	# print trainY
	Test = np.array(Test)
	# score = train(trainX,trainY,Test,count)
	# print Test, count;
	# print score
	score = float(negCount)*100/count
	print 'negCount = ' , negCount
	print 'count = ', count
	return score, count
				