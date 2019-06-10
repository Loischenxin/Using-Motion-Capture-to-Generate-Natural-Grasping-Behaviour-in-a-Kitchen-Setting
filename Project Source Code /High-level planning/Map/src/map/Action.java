/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */
package map;

import java.util.HashMap;
import java.util.Set;

/**
 *
 * @author lois
 */
public class Action {
    public static final HashMap<String, String[]> actionTools = new <String,String[]> HashMap();
     static{
        String[] cutarr={"knife","cutting_board"};
        String[] washarr={"dish_towel","sink"};
        actionTools.put("cut", cutarr);
        actionTools.put("wash",washarr);
     }
    public String Action(String act){
        
       // HashMap<String, String[]> actionTools = new <String,String[]> HashMap();
//        String[] cutarr={"knife","cutting_board"};
//        String[] washarr={"dish_towel","sink"};
//        actionTools.put("cut", cutarr);
//        actionTools.put("wash",washarr);

        String tools="wrong input";
        
        if(actionTools.get(act) !=null){
            tools = actionTools.get(act)[0];
        }
        else{
            tools = "Wrong input";
        }
        return tools;
        
    }
    
    public String getendPostion(String enp){
         String endPost=actionTools.get(enp)[1];
         return endPost;
         
    }

//   public String getVerb(){
//       Set keyset=actionTools.keySet();
//       
//   }
//    public static void main(String args[]){
//        Action a=new Action();
//        System.out.print(a.Action("wash"));
//    }
}
