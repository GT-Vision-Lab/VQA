__author__='aagrawal'

# This code is based on the code written by Tsung-Yi Lin for MSCOCO Python API available at the following link: 
# (https://github.com/tylin/coco-caption/blob/master/pycocoevalcap/eval.py).

class VQAEval:
	def __init__(self, vqa, vqaRes, n=2):
		self.n 			  = n
		self.accuracy     = {}
		self.evalQA       = {}
		self.evalQuesType = {}
		self.evalAnsType  = {}
		self.vqa 		  = vqa
		self.vqaRes       = vqaRes
		self.params		  = {'question_id': vqaRes.getQuesIds()}
	
	def evaluate(self):
		quesIds = [quesId for quesId in self.params['question_id'] if quesId in self.vqa.getQuesIds()]
		gts = {}
		res = {}
		for quesId in quesIds:
			gts[quesId] = self.vqa.qa[quesId]
			res[quesId] = self.vqaRes.qa[quesId]
		
		# =================================================
		# Compute accuracy
		# =================================================
		accQA       = []
		accQuesType = {}
		accAnsType  = {}
		print "computing accuracy"
		for quesId in quesIds:
			resAns      = res[quesId]['answer']
			gtAns       = [ans['answer'] for ans in gts[quesId]['answers']]
			matchingAns = [ans for ans in gtAns if ans==resAns]
			acc         = float(len(matchingAns))/len(gtAns)
			quesType    = gts[quesId]['question_type']
			ansType     = gts[quesId]['answer_type']
			accQA.append(acc)
			if quesType not in accQuesType:
				accQuesType[quesType] = []
			accQuesType[quesType].append(acc)
			if ansType not in accAnsType:
				accAnsType[ansType] = []
			accAnsType[ansType].append(acc)
			self.setEvalQA(quesId, acc)
			self.setEvalQuesType(quesId, quesType, acc)
			self.setEvalAnsType(quesId, ansType, acc)
		self.setAccuracy(accQA, accQuesType, accAnsType)
		print "Done computing accuracy"

	def setAccuracy(self, accQA, accQuesType, accAnsType):
		self.accuracy['overall']         = round(100*float(sum(accQA))/len(accQA), self.n)
		self.accuracy['perQuestionType'] = {quesType: round(100*float(sum(accQuesType[quesType]))/len(accQuesType[quesType]), self.n) for quesType in accQuesType}
		self.accuracy['perAnswerType']   = {ansType:  round(100*float(sum(accAnsType[ansType]))/len(accAnsType[ansType]), self.n) for ansType in accAnsType}
			
	def setEvalQA(self, quesId, acc):
		self.evalQA[quesId] = round(100*acc, self.n)

	def setEvalQuesType(self, quesId, quesType, acc):
		if quesType not in self.evalQuesType:
			self.evalQuesType[quesType] = {}
		self.evalQuesType[quesType][quesId] = round(100*acc, self.n)
	
	def setEvalAnsType(self, quesId, ansType, acc):
		if ansType not in self.evalAnsType:
			self.evalAnsType[ansType] = {}
		self.evalAnsType[ansType][quesId] = round(100*acc, self.n)

