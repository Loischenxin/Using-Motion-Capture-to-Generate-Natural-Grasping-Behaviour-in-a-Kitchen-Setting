/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */
package map;

/**
 *
 * @author lois
 */
import java.io.FileInputStream;
import java.io.InputStream;
import java.util.HashSet;
import java.util.Set;

import opennlp.tools.cmdline.parser.ParserTool;
import opennlp.tools.parser.Parse;
import opennlp.tools.parser.Parser;
import opennlp.tools.parser.ParserFactory;
import opennlp.tools.parser.ParserModel;

public class ParserTest {  //opennlp
    static Set<String> nounPhrases = new HashSet<>();
 static Set<String> adjectivePhrases = new HashSet<>();
 static Set<String> verbPhrases = new HashSet<>();
 
 //private static String line = "You should cut the tomatoes then wash the potatoes";
 
 public void getNounPhrases(Parse p) {
  if (p.getType().equals("NN") || p.getType().equals("NNS") ||  p.getType().equals("NNP") 
    || p.getType().equals("NNPS")) {
          nounPhrases.add(p.getCoveredText()); //extracting the noun parse
  }
     
  if (p.getType().equals("VB") || p.getType().equals("VBP") || p.getType().equals("VBG")|| 
          p.getType().equals("VBD") || p.getType().equals("VBN")) {
      
      verbPhrases.add(p.getCoveredText()); //extracting the verb parse
   }
     
  for (Parse child : p.getChildren()) {
          getNounPhrases(child);
  }
}
 
 public String[] parserAction(String a) throws Exception {
 InputStream is = new FileInputStream("/Users/lois/Desktop/Map/src/map/en-parser-chunking.bin");
 ParserModel model = new ParserModel(is);
 Parser parser = ParserFactory.create(model);
 Parse topParses[] = ParserTool.parseLine(a, parser, 1);
 for (Parse p : topParses){
  //p.show();
  getNounPhrases(p);
 }
 String[] arraynoun = nounPhrases.toArray(new String[0]);
 String[] arrayverb = verbPhrases.toArray(new String[0]);
 String[] combine =new String[arraynoun.length+arrayverb.length];
 int count=0;
 
 for(int i=0; i<arraynoun.length; i++){
      combine[i]=arraynoun[i];
      count++;
 }
 for(int j=0; j<arrayverb.length; j++){
      combine[count++]=arrayverb[j];
      
 }
 return combine;
 
}
    
}
