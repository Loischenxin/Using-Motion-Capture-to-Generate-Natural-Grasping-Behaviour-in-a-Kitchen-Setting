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
public class Node {
     private int nodeId;
    private double[] coordinate;
    boolean check = false;
    private int type;

    private Node(){}

    Node(double x, double y, int id, int type){ 
    // tpye positive = start postion, negative = end postion
        this.coordinate = new double[]{x,y};
        this.nodeId = id;
        this.type = type;
    }

    int getType(){ return this.type; }

    double[] getCoordinate(){
        return this.coordinate;
    }

    int getNodeId(){
        return this.nodeId;
    }

    public Node clone(){
        Node n = new Node();
        n.nodeId = this.nodeId;
        n.coordinate = this.coordinate;
        n.check = this.check;
        n.type = this.type;

        return n;
    }
}