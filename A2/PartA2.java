package stopword;
import java.util.*;
import java.util.regex.Pattern;
import java.io.*;


public class PartA2
{
    
    public static Boolean isStopWord(String word, String[] stopWords)
    {
	boolean found = false;   	
	found=Arrays.asList(stopWords).contains(word);
	return found;
    }
    public static int compareWords(String word1, String word2)
    {
	return word1.compareToIgnoreCase(word2);
    }
    private static String RESULT_FNAME = "result.txt";
    public static void main(String[] arg) throws IOException
    {
    	File file1 = new File("intext.txt");
        File file2 = new File("outtext.txt"); 
        char CharCounter = 0;       
        BufferedReader in = (new BufferedReader(new FileReader(file1)));
        PrintWriter out = (new PrintWriter(new FileWriter(file2)));
        int ch1;
        int ch;
        while ((ch = in.read()) != -1){
            
            ch1 = Character.toLowerCase(ch);            
            out.write(ch1);
        }
        in.close();
        out.close();	

	String[] stopWords = readStopWords("stopwords.txt");
	removeStopWords("outtext.txt", stopWords);

    }

    
    public static String[] readStopWords(String stopWordsFilename) 
    {
	String[] stopWords = null;
	try
	    {
		Scanner stopWordsFile = new Scanner(new File(stopWordsFilename));
		//int numStopWords = stopWordsFile.nextInt();
		stopWords = new String[94];
		for (int i = 0; i < 94; i++)
		    stopWords[i] = stopWordsFile.next();

		stopWordsFile.close();
	    }
	catch (FileNotFoundException e)
	    {
		System.err.println(e.getMessage());
		System.exit(-1);
	    }

	return stopWords;
    }

    
    public static void removeStopWords(String textFilename, String[] stopWords)
    {
	String word;
	try
	    {
		Scanner textFile = new Scanner(new File(textFilename));
		textFile.useDelimiter(Pattern.compile("[ \t,.;:?!'\"0123456789!@#$%^&*()_={}|:;'<,>.?/]+"));

		PrintWriter outFile = new PrintWriter(new File(RESULT_FNAME));

		System.out.println("\nRemoving:");
		while (textFile.hasNext())
		    {
			word = textFile.next();
			if (isStopWord(word, stopWords))
			    System.out.print(word + " ");
			else
			    outFile.print(word + " ");
		    }
		System.out.println("\n\nText after removing stop words is in " + RESULT_FNAME);
		outFile.println();

		textFile.close();
		outFile.close();
	    }
	catch (FileNotFoundException e)
	    {
		System.err.println(e.getMessage());
		System.exit(-1);
	    }

    }

}