#!/usr/bin/env python
import sys
def main():
	with open('db.txt') as f:
    		lines = f.readlines()
    	onetime=[]
    	twotime=[]
    	threetime=[]
    	
    	target1=open("vocabulary.txt", 'a+')
    	target2=open("bigram_vocabulary.txt", 'w')
    	for line in lines:
    		line = line.strip().split(" ")
    		for word1,word2 in zip(line, line[1:] ) : 
    			if word1.isalpha() and word2.isalpha():
	    			if str(" ".join([word1, word2])) not in onetime:
	    				onetime.append(" ".join([word1,word2])) 
	    			elif str(" ".join([word1, word2])) not in twotime:
	    				twotime.append(" ".join([word1,word2]))
	    			elif str(" ".join([word1, word2])) not in threetime:
	    				threetime.append(" ".join([word1,word2]))
	    				target1.write(" ".join([word1,word2]))
	    				target1.write("\n") 
	    				target2.write(" ".join([word1,word2]))
	    				target2.write("\n") 
	    							
    	target1.close()
    	target2.close()
main()
