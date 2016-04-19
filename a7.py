#!/usr/bin/env python
import pickle
import math

def main():
	lines = pickle.load( open( "result.txt", "rb" ) )
	
	poslines=[]
	neglines=[]
	
	for line in lines:
		if line[0]=='+':
			poslines.append(line)
		elif line[0]=='-':
			neglines.append(line)
	
	i=j=0
	newlines=[]
		
	while i < len(poslines) or i < len(neglines):
		if i < len(poslines):
			newlines.append(poslines[i])
		if i < len(neglines):
			newlines.append(neglines[i])
		i=i+1
		
	lines=newlines
	reviewcount=len(lines)
	grpsize= int((reviewcount-1)/10)+1
	
	acsum=0
	
	for i in range(10):
	
		train=lines[0:grpsize*i]+lines[grpsize*(i+1):]
		trainlen=len(train)
		totalwordsinp=1
		totalwordsinn=1
		vocab=[]
		for line in train:
			line=line.strip().split(" ")
			if line[0] == '+':
				for word1,word2 in zip(line, line[1:] ) :
					totalwordsinp+=1
					if str(" ".join([word1, word2])) not in vocab:
						vocab.append(str(" ".join([word1, word2])))
					if word1 not in vocab:
						vocab.append(word1)
					if word2 not in vocab:
						vocab.append(word2)	
						
			elif line[0] == '-':
				for word1,word2 in zip(line, line[1:] ) :
					totalwordsinn+=1
					if str(" ".join([word1, word2])) not in vocab:
						vocab.append(str(" ".join([word1, word2])))
					if word1 not in vocab:
						vocab.append(word1)
					if word2 not in vocab:
						vocab.append(word2)
					
		vocabulary=len(vocab)
	
		cp=cn=0
	    	for line in train:
	    		if line[0]=='+':
	    			cp=cp+1
	    		elif line[0]=='-':
	    			cn=cn+1
	    	
	    	priorp=float(cp)/trainlen
	    	priorn=float(cn)/trainlen
	    	
	    	
	    	
	    	test=lines[grpsize*i:grpsize*(i+1)]
	    	filestream1=open("bigram_vocabulary.txt", 'r')
	    	bigrams=filestream1.readlines()
	    	filestream=open("predictnew.txt", 'w')
	    	for line in test:
	    		uniqueugwords=[]
	    		uniquebgwords=[]
	    		words=line.strip().split(" ")
	    		for word1,word2 in zip(words, words[1:] ) :
	    			if str(" ".join([word1, word2])) in bigrams and str(" ".join([word1, word2])) not in uniquebgwords:
	    				uniquebgwords.append(str(" ".join([word1, word2])))
	    			if word1 not in uniqueugwords:
	    				uniqueugwords.append(word1)
	    			if word2 not in uniqueugwords:
	    					uniqueugwords.append(word2)
	    		probuwp=[]
	    		probuwn=[]
	    	
	    		for word in uniqueugwords:
	    			countwp=countwn=0
	    			for line2 in train:
	    				line2=line2.strip().split(" ")
					if line2[0] == '+':
						for word2 in line2:
							if word == word2:
								countwp+=1
					elif line2[0] == '-':
						for word2 in line2:
							if word == word2:
								countwn+=1
					 
	    			probuwp.append(float(countwp+1)/(totalwordsinp+vocabulary))
	    			probuwn.append(float(countwn +1)/(totalwordsinn+vocabulary))
	    			
	    		probbwp=[]
	    		probbwn=[]
	    	
	    		for word in uniquebgwords:
	    			countbwp=countbwn=0
	    			word=word.strip().split(" ")
	    			for line2 in train:
	    				line2=line2.strip().split(" ")
					if line2[0] == '+':
						for i in range(len(line2)-1):
							if word[0] == line2[i] and word[1] == line2[i+1] :
								countbwp+=1
					elif line2[0] == '-':
						for i in range(len(line2)-1):
							if word[0] == line2[i] and word[1] == line2[i+1] :
								countbwn+=1
					 
	    			probbwp.append(float(countbwp+1)/(totalwordsinp+vocabulary))
	    			probbwn.append(float(countbwn +1)/(totalwordsinn+vocabulary))
	    			
	    		probp=math.log(priorp)
	    		probn=math.log(priorn)
	    		for word1,word2 in zip(words[0::2], words[1::2] ) :
	    			try:
		    			ind=uniquebgwords.index(str(" ".join([word1, word2])))
		    			probp+=math.log(float(probbwp[ind]))
	    				probn+=math.log(float(probbwn[ind]))
				except:
					ind1=uniqueugwords.index(word1)
					ind2=uniqueugwords.index(word2)
	    				probp+=math.log(float(probuwp[ind1]))
	    				probn+=math.log(float(probuwn[ind1]))
	    				probp+=math.log(float(probuwp[ind2]))
	    				probn+=math.log(float(probuwn[ind2]))
	    			
	    		
	    		if probp < probn:
	    			filestream.write('- ')
	    			filestream.write(' '.join(words[1:]))
	    			filestream.write('\n')
	    		else:	
	    			filestream.write('+ ')
	    			filestream.write(' '.join(words[1:]))
	    			filestream.write('\n')
	    			
	    	filestream.close()
	    	
	    	accuracy=tp=tn=fp=fn=0
	    	file1 = open('predictnew.txt', 'r')
	    	j=0
		for line1 in file1.readlines():
			line2=test[j].strip().split(" ")
			j+=1
	    		if line1[0]=='+' and  line2[0]=='+' :
				tp=tp+1
			if line1[0]=='-' and  line2[0]=='-' :
				tn=tn+1
			if line1[0]=='+' and  line2[0]=='-' :
				fp=fp+1
			if line1[0]=='-' and  line2[0]=='+' :
				fn=fn+1
			
		
		
		accuracy=float((tp+tn))/(tp+tn+fp+fn)	
		print "Accuracy ",i+1," : ", accuracy
		acsum+=accuracy
		
	print "Average Accuracy: ", acsum/10
	
main()
    		
    	
    	
