import pickle
def main():
	            		
        with open('db.txt') as f:
    		lines = f.readlines()
    	c=len(lines)
    	pos=neg=0
    	for line in lines:
    		if line[0]=='+':
    			pos=pos+1
    		elif line[0]=='-':
    			neg=neg+1
    	
    	priorpos=float(pos)/c         

    	priorneg=float(neg)/c          


      	print priorpos,priorneg
  
     	
    	pickle.dump(lines,open( "result.txt", "wb" ) )
    	
    		
main()

