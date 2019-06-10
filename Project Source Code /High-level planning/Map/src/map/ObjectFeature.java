/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */
package map;

import java.util.HashMap;

/**
 *
 * @author lois
 */
public class ObjectFeature {
    public static final HashMap<String, String> featureObject = new <String,String> HashMap();
    static{
        featureObject.put("potatoes", "drawer");
         featureObject.put("onion", "refrigerator");
         featureObject.put("apple", "refrigerator");
         featureObject.put("tomato", "refrigerator");
         featureObject.put("knife", "drawer");
         featureObject.put("dish_towel", "right_handle_cabinet");
         featureObject.put("sauce","left_handle_cabinet");
         featureObject.put("pear","left_handle_cabinet");
        
    }
    Action action=new Action();
    
    public String[][] getEndPostion(String[] obj){
        String[][] endposition=new String[obj.length][2];
        int length= obj.length/2;
        for(int i=0;i<obj.length;i++){
            
                if (i<(obj.length)/2){
                    endposition[i][0]=obj[i];
                    endposition[i][1]=action.getendPostion(obj[(length+i)]);
                    //System.out.println(length+i);
                            //action.getendPostion(obj[(length+i)]);
                    
                }
                else{
                    endposition[i][0]=obj[i];
                    endposition[i][1]=action.getendPostion(obj[i]);
                }
                
            
        }
//        for(int i=0;i<obj.length;i++){
//            for(int j=0;j<2;j++){
//                System.out.println(endposition[i][j]);
//            }
//        }
        return endposition;
    }
    
    public String[] ObjectFeature(String[] ob){
        
         
         
         
      
         String[] features=new String[ob.length];
         
         Boolean diag = true;
         
     
         
         
         for (int i = 0; i < ob.length; i++) { 
             
              
               if(diag && (!action.Action(ob[i]).equals("Wrong input"))){

                    features[i] = featureObject.get(action.Action(ob[i]));
                    
                    //System.out.println(action.getendPostion(ob[i]));
                } // map the verb to the object
               
               else if(featureObject.get(ob[i]) != null){

                    features[i] = featureObject.get(ob[i]); 
                    //check whether we have the objects
                   
                }
                
                else if(ob[i].equals("end")){
                   
                    features[i]="end";
                }
                else {
                    features[i]="Wrong recipe";

                }
            }
         
      
        return features;
    }
    
    public String[][] getobject(String ob[]){
        String[][] objectandLocation=new String[ob.length][2];
        Boolean diag = true;
        
        
        for (int i = 0; i < ob.length; i++) { 
             
              
               if(diag && (!action.Action(ob[i]).equals("Wrong input"))){
                   
                   objectandLocation[i][0] = action.Action(ob[i]);
                   objectandLocation[i][1]= featureObject.get(action.Action(ob[i]));
                   
                    //System.out.println(action.getendPostion(ob[i]));
                } // map the verb to the object
               
               else if(featureObject.get(ob[i]) != null){
                   
                   objectandLocation[i][0]= ob[i];
                   objectandLocation[i][1] = featureObject.get(ob[i]); 
                   //check whether we have the objects
                   
                }
                
                else if(ob[i].equals("end")){

                }
               
            }
//        for(int i=0; i<objectandLocation.length;i++){
//            for(int j=0; j<2;j++){
//                System.out.println(objectandLocation[i][j]);
//            }
//        }
        return objectandLocation;
    }
    

    
}
