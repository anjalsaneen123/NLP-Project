import java.io.BufferedReader;
import java.io.DataInputStream;
import java.io.File;
import java.io.FileInputStream;
import java.io.FileNotFoundException;
import java.io.FileWriter;
import java.io.IOException;
import java.io.InputStream;
import java.io.InputStreamReader;
import java.io.PrintWriter;
import java.util.ArrayList;
import java.util.Collections;
import java.util.Comparator;
import java.util.HashMap;
import java.util.List;
import java.util.Map;
import java.util.Map.Entry;
import java.util.Set;
import java.util.StringTokenizer;
import java.util.regex.Pattern;

public class PartA3 {
    	

	    public static void main(String args[])throws IOException 
	    {
	        Map<String, Integer> wordMap = buildWordMap("result.txt");
	        File file2 = new File("vocabulary.txt");
	        String s="";
	        List<Entry<String, Integer>> list = sortByValueInDecreasingOrder(wordMap);
	        PrintWriter out = (new PrintWriter(new FileWriter(file2)));
	    
	        for (Map.Entry<String, Integer> entry : list) 
	        {
	            if (entry.getValue() > 1) 
	            {
	            	
	            	if(!((entry.getKey().equals("+"))||(entry.getKey().equals("-"))))
	            	{
	            	out.write(entry.getKey());
	            	out.write("\r\n");
	            	}
	                //System.out.println(entry.getKey() + " => " + entry.getValue());
	            }
	            
	        }
	        out.close();
	    }

	    public static Map<String, Integer> buildWordMap(String fileName) 
	    {
	        
	        Map<String, Integer> wordMap = new HashMap<>();
	        try (FileInputStream fis = new FileInputStream(fileName);
	        DataInputStream dis = new DataInputStream(fis);
	        BufferedReader br = new BufferedReader(new InputStreamReader(dis))) 
	        {
	            Pattern pattern = Pattern.compile("\\s+");
	            String line = null;
	            while ((line = br.readLine()) != null) 
	            {	                
	                line = line.toLowerCase();
	                String[] words = pattern.split(line);
	                for (String word : words) 
	                {
	                    if (wordMap.containsKey(word)) 
	                    {
	                        wordMap.put(word, (wordMap.get(word) + 1));
	                    } 
	                    else 
	                    {
	                        wordMap.put(word, 1);
	                    }
	                }
	            }
	        } 
	        catch (IOException ioex) 
	        {
	            ioex.printStackTrace();
	        }
	        return wordMap;
	    }
	    public static List<Entry<String, Integer>> sortByValueInDecreasingOrder(Map<String, Integer> wordMap) 
	    {
	        Set<Entry<String, Integer>> entries = wordMap.entrySet();
	        List<Entry<String, Integer>> list = new ArrayList<>(entries);
	        Collections.sort(list, new Comparator<Map.Entry<String, Integer>>() 
	        {
	        @Override
	        public int compare(Map.Entry<String, Integer> o1, Map.Entry<String, Integer> o2) 
	        {
	        return (o2.getValue()).compareTo(o1.getValue());
	        }
	        });
	        return list;
	    }
}