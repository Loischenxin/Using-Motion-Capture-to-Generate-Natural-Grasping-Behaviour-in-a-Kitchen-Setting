/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */
package map;

import java.io.File;
import java.io.FileNotFoundException;
import java.util.ArrayList;
import java.util.Arrays;
import java.util.HashMap;
import java.util.Scanner;
import javax.lang.model.element.Element;

/**
 *
 * @author lois
 */
public class Coordinate {
    
    private double dis;
    private String endRec="";
    public HashMap<String, double[]> objects = new <String, double[]>HashMap();
    public static ArrayList<double[]> arrayList = new ArrayList<double[]>();
    private static double SHORTEST_DISTANCE = Double.MAX_VALUE;
    private static ArrayList<Integer> PATH;
    private static ArrayList<Integer> TYPE;

    public HashMap<double[],String>findObj= new <double[],String>HashMap();
    public static ArrayList<String> pathorder=new ArrayList<String>();
    public static HashMap<String, String> reflect = new <String, String>HashMap(); // Map object and "smart" strategy
   
    
    public void Coordinate (ArrayList<String> coor) throws Exception{
        //KitchenMap getcor=new KitchenMap();
        
        File file = new File("/Users/lois/Desktop/Map/input.txt");
       try{ Scanner node= new Scanner(file);
        //HashMap<String, double[]> objects = new <String, double[]>HashMap(); //Map object name and their coordinate
       
       
        
       
        
 
//        System.out.println("Please enter the objects in the kitchen: (e.g. door drawer)");
        String in = node.nextLine();
        String[] object = in.split(" ");

        for(int i = 0; i < object.length; i++){
//            System.out.println("Plesase enter the coordinate of" + " "+ object[i] + "(e.g. 1,0)");
            String temp = coor.get(i);
            
            
            
//            while(!temp.contains(",")){
//                System.out.println("Wrong format!");
//                System.out.println("Please enter the correct coordinate of " + " "+ object[i] + "(e.g. 1,0)");
//                temp = node.nextLine();
//            }
            
            String[] str = temp.split(",");
            double[] arr = new double[2];
           
            for(int j = 0; j < 2; j++){
                
                    arr[j] = Double.parseDouble(str[j]);
                
            }
            
            
            objects.put(object[i], arr); //map object and their coordinate
            findObj.put(arr, object[i]);
            
        }
         String hand = node.nextLine();
         
        reflect.put("door", hand);
        reflect.put("drawer", hand);
        reflect.put("right_handle_cabinet","left hand");
        reflect.put("left_handle_cabinet","right hand");
        reflect.put("refrigerator", hand);
        
       
        
        
        int signal = 1;
        

        while(signal == 1){
          System.out.println("Enter your recipe: (e.g. door refrigerator drawers)");
            String input = node.nextLine();
            String[] splitsen=input.split(" ");
           
            new ParserTest().parserAction(input);
            
            
            String[] instruct =  new ParserTest().parserAction(input);//enter the instruct to the charater
//            for(int i=0; i<instruct.length;i++){
//                System.out.println(instruct[i]);
//            }
            

            ObjectFeature takeobject= new ObjectFeature();
            //String[][] endposition=takeobject.getEndPostion(instruct);
            
            String[] nodes= takeobject.ObjectFeature(instruct);//recognize the position of object 
            // map the action to the tools, than map the tools to the features.
            //map the objetcs to the features.
            
            //takeobject.getobject(instruct);
            
            double[][] arr = new double[(nodes.length)*2+1][2];//node postion
            
           
            
  
            System.out.print("\nYour recipe is: "+input+"\n");
            
            

            for (int i = 0; i < nodes.length; i++) {
                //System.out.println(nodes[i]);
                if(objects.get(nodes[i]) != null){
                    double[] coordinate = objects.get(nodes[i]);
                    arr[i] = coordinate;
                    
                }
                else if(nodes[i].equals("end")){
                    signal = 0;
                    System.out.println("Complete");
                }
                else {
                    System.out.println("Wrong input, enter again.");
                    signal = 2;
                    break;
                }
            }
            
           
            

            if(signal == 0){
                break;
            }else if(signal == 2){
                signal = 1;
                continue;
            }
            
            //get the endpostion
            String[][] endposition=takeobject.getEndPostion(instruct);
            //get the endpostion coordinate
             double endcoordinate[][]=new double[nodes.length][2];
             
             //add the end postion in the arr==> 
             //now fist 4 node represent the object position,last 4 node represent end postion
             for(int j=0; j<nodes.length;j++){
                 if(objects.get(endposition[j][1]) != null){
                    double[] ecoordinate = objects.get(endposition[j][1]);
                    arr[(nodes.length)+j] = ecoordinate;
                }
             }
             arr[nodes.length*2]=objects.get(object[0]);
             
             
//            for(int i=0; i<nodes.length*2;i++){
//                System.out.println("arr cod");
//                for(int j=0;j<2;j++){
//                    System.out.println(arr[i][j]);
//                }
//            }


            System.out.println("\n"+"the distance matrix:");
           double[][] matrix = new double[nodes.length*2+1][nodes.length*2+1];

           for(int first=0; first < nodes.length*2+1; first++){
               for(int sec=0; sec < nodes.length*2+1; sec++){

                    dis=Math. sqrt((arr[sec][0]-arr[first][0])*(arr[sec][0]-arr[first][0])
                            + (arr[sec][1]-arr[first][1])*(arr[sec][1]-arr[first][1]));
                    matrix[first][sec] = dis;
                    System.out.print(matrix[first][sec]);
                    System.out.print(" ");
               }
               System.out.print("\n");
           }
           
           
           
           ArrayList<Node> nodeList = new ArrayList<Node>();
           
           for(int i=0; i<nodes.length*2; i++){
               if(i<nodes.length){
                    nodeList.add(new Node(arr[i][0],arr[i][1],i+1,i+1));}
               else{
                   nodeList.add(new Node(arr[i][0],arr[i][1],i+1,(nodes.length-i-1)));
               }
               
           }
           //add door as start posotion at last
           nodeList.add(new Node(arr[nodes.length*2][0],arr[nodes.length*2][1],(nodes.length*2+1),0));
           nodeList.get(nodes.length*2).check=true;//check the door as start postion
           
            ArrayList<Integer> path = new ArrayList<Integer>();
            path.add(nodeList.get(nodes.length*2).getNodeId());
            ArrayList<Integer> type = new ArrayList<Integer>();
            type.add(nodeList.get(nodes.length*2).getType());
            //find the shortest path
            findPath(matrix, nodeList, type, nodeList.get(nodes.length*2), path, 0);
            System.out.println(SHORTEST_DISTANCE);
             for(int n:PATH){
            System.out.print(n);
            System.out.print(" ");
        }
            System.out.print("\n Type list:");

             for(int n:TYPE){
            System.out.print(n);
            System.out.print(" ");
        }
             //print the shortest path in text.
             System.out.println("\n");
             for(int i=0;i<PATH.size();i++){
                 if(PATH.get(i)<=nodes.length){
                     arrayList.add(arr[PATH.get(i)-1]);
                     System.out.print(nodes[PATH.get(i)-1]+" ");
                     pathorder.add(nodes[PATH.get(i)-1]);
                     
                 }else if(PATH.get(i)>nodes.length && PATH.get(i)<=nodes.length*2){
                     arrayList.add(arr[PATH.get(i)-1]);
                     System.out.print(endposition[PATH.get(i)-nodes.length-1][1]+" ");
                     pathorder.add(endposition[PATH.get(i)-nodes.length-1][1]);
                 
                 }else if(PATH.get(i)>nodes.length+1){
                     arrayList.add(objects.get(object[0]));
                     System.out.print(object[0]+" ");
                     pathorder.add(object[0]);
                 }
             }
            for(int i=0;i<pathorder.size();i++){
                for(int j=i+1;j<pathorder.size();j++){
                    if(pathorder.get(i).equals(pathorder.get(j))){
                        pathorder.remove(i);
                        i--;
                        break;

                    }
                }
            }
            System.out.println("\n");
            for(int i=0; i<pathorder.size();i++){
                System.out.print(pathorder.get(i)+" ");
            }
             System.out.println("\n");
             //System.out.print(pathorder.get(0));
             

          findPath(pathorder,instruct);


            //long start = System.currentTimeMillis();
            //TSP ff = new TSP(matrix);
            //System.out.println("路径是：" + ff.getFirnalRoad())


            //System.out.println("plan order：" + ff.getFirnalCityFlow());
//            String[] temp = ff.getFirnalCityFlow().split("->");
//            String obj[]=new String [nodes.length];
//            int [] ref = new int[nodes.length];
//            for(int i=0; i<nodes.length; i++){
//                ref[i]=Integer.parseInt(temp[i]);
//                obj[i]=nodes[ref[i]];
//            }
//
//           System.out.println("\n"+"path order:");
//            for (int i=0; i<nodes.length;i++){
//                if(i != nodes.length - 1){
//                    System.out.print((i+1)+" go to the "+obj[i]+" and use "+reflect.get(obj[i])+" to open it."+"\n");
//                }else{
//                    System.out.println((i+1)+" go to the "+obj[i]+" and use "+reflect.get(obj[i])+" to open it."+"\n"+
//                            (i+2)+". Back to the "+obj[0]);
//                }
//            }
//            
//            for(int j=0;j<nodes.length;j++){
//                arrayList.add(objects.get(obj[j]));
//            }





            //System.out.println("minimal value of path：" + ff.getMin());
           // System.out.println("生成所有合法城市流用时：" + ff.getAllFlowTime());
            //System.out.println("动态规划求解过程用时：" + ff.getGuihuaTime());// enter each coordinate of each object
           
//            for(int z=0;z<nodes.length;z++){
//                for(int i=0;i<2;i++){
//                  System.out.println(arrayList.get(z)[i]);
//                }
//               
//           }
           
           
        
        }
       }catch(FileNotFoundException e){
        }
       
    }
    
    private static void findPath(double[][] matrix, ArrayList<Node> nodeList,ArrayList<Integer> typeList, Node current, ArrayList<Integer> path, double currentDistance){
        int curr = current.getNodeId();
        double min = Double.MAX_VALUE;
        boolean isFound = false;
        ArrayList<Node> tempList = new ArrayList<Node>();
        
        for(Node n:nodeList){
            tempList.add(n.clone());
        }
        for(Node temp : tempList){
            if(!temp.check){
                isFound = true;
                //复制当前已走路径的状态
                ArrayList<Integer> tempType = new ArrayList<Integer>(typeList);
                boolean isValid = false;

                int type = temp.getType();

                if(type < 0){
                    //Ei
                    //Ei 要在 Si后面
                    for(int t: tempType){
                        //如果前面已经有了Si
                        if(t == -type){
                            isValid = true;
                            break;
                        }
                    }
                    
                }else if(type==0){
                     isValid=true;
                     
                            }
                else{
                    //Si

                    //Si不能作为终点
                    if(tempType.size() == nodeList.size() - 1){
                        continue;
                    }
                    isValid = true;

                    //两个S后面一定要跟一个Ei
                    int sNumber = 0;
                    for(int i = tempType.size() - 1; i >= 0; i--){
                        //如果前面已经有两个Si
                        if (sNumber == 2){
                            isValid=false;
                            break;
                        }
                        //如果是Si
                        if(tempType.get(i) > 0){
                            sNumber++;
                        }else{
                            isValid = true;
                            break;
                        }
                    }
                }


                if(!isValid){
                    continue;
                }

                ArrayList<Integer> tempPath = new ArrayList<Integer>(path);

                //假设走temp这个点
                tempPath.add(temp.getNodeId());
                tempType.add(type);

                temp.check = true;
                findPath(matrix, tempList, tempType, temp, tempPath, currentDistance + matrix[curr - 1][temp.getNodeId() - 1]);
                //还原回去
                temp.check = false;
            }
        }

        if(!isFound){
            //如果所有点都走完就判断是否是当前最短路径
            if (currentDistance < SHORTEST_DISTANCE){
                SHORTEST_DISTANCE = currentDistance;
                PATH = path;
                TYPE = typeList;
            }
        }
    }
    
//      reflect.put("door", hand);
//        reflect.put("drawer", hand);
//        reflect.put("right_handle_cabinet","left hand");
//        reflect.put("left_handle_cabinet","right hand");
//        reflect.put("refrigerator", hand);
    private static void findPath(ArrayList<String> path, String[] instruction){
        ObjectFeature position= new ObjectFeature();
        String[][] objMachPlace=position.getobject(instruction);// the array includes the opject and thier postion
        
        int right=0;
        int left=0;
        
        //ArrayList<String> openhand =new ArrayList<String>();
        //ArrayList<String> objtaking=new ArrayList<String>();
        for(int i=0;i<path.size();i++){
            if(path.get(i).equals("door")){
                //openhand.add(reflect.get("door"));
                System.out.println((i+1)+"."+" Use the "+reflect.get("door")+" to open the door.");
                }//use which hand to open the door
            
            if(path.get(i).equals("drawer")){
                String ob=" ";
                if(right * left == 0){  //check use which hand to open the drawer
                    if(right==1){
                        //openhand.add("left hand");
                        System.out.println((i+1)+"."+" Use "+"the left hand"+" to open the drawer.");
                    }else if(left==1){
                    //openhand.add("right hand");
                        System.out.println((i+1)+"."+" Use "+"the ringt hand"+" to open the drawer.");
                    }else if(right==0 && left==0){
                        //openhand.add(reflect.get("drawer"));
                        System.out.println((i+1)+"."+" Use the "+reflect.get("drawer")+" to open the drawer.");
                    }else if(right==1 && left==1){
                        System.out.println((i+1)+". Put all the objects on the table abd"+" use the "
                                +reflect.get("drawer")+" to open the drawer.");
                    }
                    
                }
                
                for(int j=0; j<objMachPlace.length;j++){ // when open the drawer to pick the object
                    if(objMachPlace[j][1]=="drawer"){
                       ob= objMachPlace[j][0];           
                    } 
                }
                
                if(right * left == 0){  //check use which hand to open the drawer
                    if(right==1){
                        //openhand.add("left hand");
                        System.out.println("Then"+" use "+"the left hand"+" to pick up the "+ob+".");
                        left=1;
                    }else if(left==1){
                        System.out.println("Then"+" use "+"the right hand"+" to pick up the "+ob+".");
                        right=1;
                    }else if(right==0 && left==0){
                        System.out.println("Then"+" use "+"the right hand"+" to pick up the "+ob+".");
                        right=1;
                        
                    }
                    
                }
            }
            
            if(path.get(i).equals("right_handle_cabinet")){
                String ob=" ";
                if(right * left == 0){  //check use which hand to open the drawer
                    if(right==1){
                        //openhand.add("left hand");
                        System.out.println((i+1)+"."+" Use "+"the left hand"+" to open the right handle cabinet.");
                    }else if(left==1){
                    //openhand.add("right hand");
                        System.out.println((i+1)+"."+"Transfer the object from the left hand to the right hand and then use left hand to open the right handle cabinet");
                        left=0;
                        right=1;
                    }else if(right==0 && left==0){
                        //openhand.add(reflect.get("drawer"));
                        System.out.println((i+1)+"."+" Use the "+reflect.get("right_handle_cabinet")+" to open the right handle cabinet.");
                    }else if(right==1 && left==1){
                        System.out.println((i+1)+". Put all the objects on the table and"+" use the "+reflect.get("right_handle_cabinet")+" to open the right handle cabinet.");
                    }
                    
                }
                
                for(int j=0; j<objMachPlace.length;j++){ // when open the drawer to pick the object
                    if(objMachPlace[j][1]=="right_handle_cabinet"){
                       ob= objMachPlace[j][0];           
                    } 
                }
                
                if(right * left == 0){  //check use which hand to open the drawer
                    if(right==1){
                        //openhand.add("left hand");
                        System.out.println("Then"+" use "+"the left hand"+" to pick up the "+ob+".");
                        left=1;
                    }else if(left==1){
                        System.out.println("Then"+" use "+"the right hand"+" to pick up the "+ob+".");
                        right=1;
                    }else if(right==0 && left==0){
                        System.out.println("Then"+" use "+"the right hand"+" to pick up the "+ob+".");
                        right=1;
                        
                    }
                    
                }
            }
            
            
            if(path.get(i).equals("left_handle_cabinet")){
                String ob=" ";
                if(right * left == 0){  //check use which hand to open the drawer
                    if(right==1){
                        
                        System.out.println((i+1)+"."+"Transfer the object from the left hand to the right hand and then use left hand to open the right handle cabinet");
                        right=0;
                        left=1;
                        
                    }else if(left==1){
 
                        System.out.println((i+1)+"."+" Use "+"the right hand"+" to open the left handle cabinet.");
                       
                    }else if(right==0 && left==0){
                        //openhand.add(reflect.get("drawer"));
                        System.out.println((i+1)+"."+" Use the "+reflect.get("left_handle_cabinet")+" to open the left handle cabinet.");
                    }else if(right==1 && left==1){
                        System.out.println((i+1)+". Put all the objects on the table and"+" use the "+reflect.get("left_handle_cabinet")+" to open the left handle cabinet.");
                    }
                    
                }
                
                for(int j=0; j<objMachPlace.length;j++){ // when open the drawer to pick the object
                    if(objMachPlace[j][1]=="left_handle_cabinet"){
                       ob= objMachPlace[j][0];           
                    } 
                }
                
                if(right * left == 0){  //check use which hand to open the drawer
                    if(right==1){
                        //openhand.add("left hand");
                        System.out.println("Then"+" use "+"the left hand"+" to pick up the "+ob+".");
                        left=1;
                    }else if(left==1){
                        System.out.println("Then"+" use "+"the right hand"+" to pick up the "+ob+".");
                        right=1;
                    }else if(right==0 && left==0){
                        System.out.println("Then"+" use "+"the right hand"+" to pick up the "+ob+".");
                        right=1;
                        
                    }
                    
                }
            }
            
            
            if(path.get(i).equals("refrigerator")){
                String ob=" ";
                if(right * left == 0){  //check use which hand to open the drawer
                    if(right==1){
                        //openhand.add("left hand");
                        System.out.println((i+1)+"."+" Use the "+"left hand"+" to open the refrigerator.");
                    }else if(left==1){
                    //openhand.add("right hand");
                        System.out.println((i+1)+"."+" Use the "+"ringt hand"+" to open the refrigerator.");
                    }else if(right==0 && left==0){
                        //openhand.add(reflect.get("drawer"));
                        System.out.println((i+1)+"."+" Use the "+reflect.get("drawer")+" to open the refrigerator.");
                    }else if(right==1 && left==1){
                        System.out.println((i+1)+". Put all the objects on the table abd"+" use the "+reflect.get("refrigerator")+"to open the drawer.");
                    }
                    
                }
                
                for(int j=0; j<objMachPlace.length;j++){ // when open the drawer to pick the object
                    if(objMachPlace[j][1]=="refrigerator"){
                       ob= objMachPlace[j][0];           
                    } 
                }
                
                if(right * left == 0){  //check use which hand to open the drawer
                    if(right==1){
                        //openhand.add("left hand");
                        System.out.println("Then"+" use "+"the left hand"+" to pick up the "+ob+".");
                        left=1;
                    }else if(left==1){
                        System.out.println("Then"+" use "+"the right hand"+" to pick up the "+ob+".");
                        right=1;
                    }else if(right==0 && left==0){
                        System.out.println("Then"+" use "+"the right hand"+" to pick up the "+ob+".");
                        right=1;
                        
                    }
                    
                }
            }
            
            if(path.get(i)=="sink"){
                right=0;
                left=0;
                System.out.println((i+1)+". Place the objects from both hands into the sink.");
                
            }
            
            if(path.get(i)=="cutting_board"){
                right=0;
                left=0;
                System.out.println((i+1)+". Place the objects from both hands on the cutting board.");
                
            }
            
                
        }
            
        
        
        
    }

    
}
