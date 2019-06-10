//The video link: https://drive.google.com/drive/folders/1mZqibMHWzRkjeHw3zMiRLBiBjEgV4CWp?usp=sharing
package map;
import java.io.File;
import java.io.IOException;
import java.net.URL;
import java.awt.Graphics;
import java.awt.Image;
import javax.swing.ImageIcon;

import java.awt.BorderLayout;
import java.awt.EventQueue;

import javax.swing.JFrame;
import javax.swing.JPanel;
import javax.swing.border.EmptyBorder;
import javax.swing.JLabel;

import java.awt.Font;
import java.awt.event.MouseAdapter;
import java.awt.event.MouseEvent;
import java.io.File;
import java.io.FileNotFoundException;
import java.util.HashMap;
import java.util.Scanner;
import java.awt.*;
import java.awt.geom.Line2D;
import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.net.MalformedURLException;
import java.net.URLConnection;
import java.util.ArrayList;
import java.util.logging.Level;
import java.util.logging.Logger;
import javafx.util.Duration;
import java.net.URI;
import java.awt.Desktop;
import java.net.URISyntaxException;

 /**
     * importing classes that are required for background image.
     */
 
public class KitchenMap extends javax.swing.JFrame {
 public static ArrayList<String> coor = new ArrayList<String>();
 public static int signalStart=0;
   
   
    
    public KitchenMap() {
        initComponents();
        
    }

    /**
     * This method is called from within the constructor to initialize the form.
     * WARNING: Do NOT modify this code. The content of this method is always
     * regenerated by the Form Editor.
     */
    @SuppressWarnings("unchecked")
    // <editor-fold defaultstate="collapsed" desc="Generated Code">//GEN-BEGIN:initComponents
    private void initComponents() {

        jPanel1 = new javax.swing.JPanel();
        jButton1 = new javax.swing.JButton();
        Rcabinet = new javax.swing.JButton();
        Lcabinet = new javax.swing.JButton();
        doorL = new javax.swing.JButton();
        doorR = new javax.swing.JButton();
        FridgeL = new javax.swing.JButton();
        FridgeR = new javax.swing.JButton();
        DrawerL = new javax.swing.JButton();
        DrawerR = new javax.swing.JButton();
        coordinate = new javax.swing.JLabel();
        map = new javax.swing.JLabel();

        setDefaultCloseOperation(javax.swing.WindowConstants.EXIT_ON_CLOSE);

        jPanel1.setLayout(null);

        jButton1.setText("get path");
        jButton1.addActionListener(new java.awt.event.ActionListener() {
            public void actionPerformed(java.awt.event.ActionEvent evt) {
                jButton1ActionPerformed(evt);
            }
        });
        jPanel1.add(jButton1);
        jButton1.setBounds(860, 550, 140, 40);

        Rcabinet.setText("open cabinet");
        Rcabinet.addActionListener(new java.awt.event.ActionListener() {
            public void actionPerformed(java.awt.event.ActionEvent evt) {
                RcabinetActionPerformed(evt);
            }
        });
        jPanel1.add(Rcabinet);
        Rcabinet.setBounds(810, 200, 110, 29);

        Lcabinet.setText("open cabinet");
        Lcabinet.addActionListener(new java.awt.event.ActionListener() {
            public void actionPerformed(java.awt.event.ActionEvent evt) {
                LcabinetActionPerformed(evt);
            }
        });
        jPanel1.add(Lcabinet);
        Lcabinet.setBounds(810, 330, 110, 29);

        doorL.setText("open door Left");
        doorL.addActionListener(new java.awt.event.ActionListener() {
            public void actionPerformed(java.awt.event.ActionEvent evt) {
                doorLActionPerformed(evt);
            }
        });
        jPanel1.add(doorL);
        doorL.setBounds(650, 470, 120, 29);

        doorR.setText("open door Right");
        doorR.addActionListener(new java.awt.event.ActionListener() {
            public void actionPerformed(java.awt.event.ActionEvent evt) {
                doorRActionPerformed(evt);
            }
        });
        jPanel1.add(doorR);
        doorR.setBounds(650, 560, 130, 30);

        FridgeL.setText("open Refrigerator Left");
        FridgeL.addActionListener(new java.awt.event.ActionListener() {
            public void actionPerformed(java.awt.event.ActionEvent evt) {
                FridgeLActionPerformed(evt);
            }
        });
        jPanel1.add(FridgeL);
        FridgeL.setBounds(400, 320, 170, 29);

        FridgeR.setText("open Refrigerator Right");
        FridgeR.addActionListener(new java.awt.event.ActionListener() {
            public void actionPerformed(java.awt.event.ActionEvent evt) {
                FridgeRActionPerformed(evt);
            }
        });
        jPanel1.add(FridgeR);
        FridgeR.setBounds(400, 450, 170, 29);

        DrawerL.setText("open drawer Left");
        DrawerL.addActionListener(new java.awt.event.ActionListener() {
            public void actionPerformed(java.awt.event.ActionEvent evt) {
                DrawerLActionPerformed(evt);
            }
        });
        jPanel1.add(DrawerL);
        DrawerL.setBounds(90, 210, 130, 30);

        DrawerR.setText("open drawer Right");
        DrawerR.addActionListener(new java.awt.event.ActionListener() {
            public void actionPerformed(java.awt.event.ActionEvent evt) {
                DrawerRActionPerformed(evt);
            }
        });
        jPanel1.add(DrawerR);
        DrawerR.setBounds(90, 420, 140, 30);

        coordinate.setText("The coordinate of each objects");
        coordinate.setToolTipText("");
        jPanel1.add(coordinate);
        coordinate.setBounds(400, 20, 200, 20);
        jPanel1.addMouseListener(new MouseAdapter(){

            public void mouseClicked(MouseEvent e){

                if(coor.size()<7){
                    coordinate.setText("X= "+ e.getX()+ " ; Y= "+e.getY());
                    Graphics g = getGraphics();
                    g.setColor(Color.BLUE);
                    g.fillOval(e.getX()-15, e.getY()+7, 30, 30);
                    coor.add(e.getX()+","+e.getY());
                    System.out.println(coor);
                }
            }

        });

        map.setIcon(new javax.swing.ImageIcon(getClass().getResource("/map/kit.jpg"))); // NOI18N
        jPanel1.add(map);
        map.setBounds(0, 0, 1050, 594);

        javax.swing.GroupLayout layout = new javax.swing.GroupLayout(getContentPane());
        getContentPane().setLayout(layout);
        layout.setHorizontalGroup(
            layout.createParallelGroup(javax.swing.GroupLayout.Alignment.LEADING)
            .addComponent(jPanel1, javax.swing.GroupLayout.PREFERRED_SIZE, 1052, javax.swing.GroupLayout.PREFERRED_SIZE)
        );
        layout.setVerticalGroup(
            layout.createParallelGroup(javax.swing.GroupLayout.Alignment.LEADING)
            .addComponent(jPanel1, javax.swing.GroupLayout.DEFAULT_SIZE, 594, Short.MAX_VALUE)
        );

        pack();
    }// </editor-fold>//GEN-END:initComponents

    private void jButton1ActionPerformed(java.awt.event.ActionEvent evt) {//GEN-FIRST:event_jButton1ActionPerformed
     if(coor.size()==7){
            Coordinate go =new Coordinate();
            try { 
                go.Coordinate(coor);
            } catch (Exception ex) {
                Logger.getLogger(KitchenMap.class.getName()).log(Level.SEVERE, null, ex);
            }
//                           int x=50;
//                           int y=50;
                           Graphics g = getGraphics();//draw a red line to show the shortest path
                           Graphics2D g2 =(Graphics2D) g;
                           g2.setColor(Color.red);
                           g2.setStroke(new BasicStroke(5));
                           for(int i=0;i<go.arrayList.size()-1;i++){
                           g2.draw(new Line2D.Double(go.arrayList.get(i)[0], go.arrayList.get(i)[1]+20, go.arrayList.get(i+1)[0], 
                                    go.arrayList.get(i+1)[1]+20));
                           
                            Point sw = new Point((int)go.arrayList.get(i)[0], (int)go.arrayList.get(i)[1]+20);
                            Point ne = new Point((int)go.arrayList.get(i+1)[0], (int)go.arrayList.get(i+1)[1]+20);
                           drawArrowHead(g2,ne,sw,Color.red);
                           try {
                                    Thread.sleep(1000);
                                } catch (InterruptedException ex) {
                                    Logger.getLogger(KitchenMap.class.getName()).log(Level.SEVERE, null, ex);
                                }
                           } 
                           
//                           g.setColor(Color.RED);
//                           g.fillOval(x, y, 30, 30);


//                           for(int z=0;z<go.arrayList.size();z++){
//                                for(int i=0;i<2;i++){
//                                System.out.println(go.arrayList.get(z)[i]);
//                            }
//                                
//               
//           }
                           

     }
                
    }//GEN-LAST:event_jButton1ActionPerformed

    private void RcabinetActionPerformed(java.awt.event.ActionEvent evt) {//GEN-FIRST:event_RcabinetActionPerformed

        String url = "file:///Users/lois/Desktop/Map/src/map/cabinetRight.avi";

        if(Desktop.isDesktopSupported()){
            Desktop desktop = Desktop.getDesktop();
            try {
                desktop.browse(new URI(url));
            } catch (IOException | URISyntaxException e) {
                // TODO Auto-generated catch block
                e.printStackTrace();
            }
        }else{
            Runtime runtime = Runtime.getRuntime();
            try {
                runtime.exec("xdg-open " + url);
            } catch (IOException e) {
                // TODO Auto-generated catch block
                e.printStackTrace();
            }
        }


    }//GEN-LAST:event_RcabinetActionPerformed

    private void LcabinetActionPerformed(java.awt.event.ActionEvent evt) {//GEN-FIRST:event_LcabinetActionPerformed
         String url = "file:///Users/lois/Desktop/Map/src/map/cabinetLeft.avi";

        if(Desktop.isDesktopSupported()){
            Desktop desktop = Desktop.getDesktop();
            try {
                desktop.browse(new URI(url));
            } catch (IOException | URISyntaxException e) {
                // TODO Auto-generated catch block
                e.printStackTrace();
            }
        }else{
            Runtime runtime = Runtime.getRuntime();
            try {
                runtime.exec("xdg-open " + url);
            } catch (IOException e) {
                // TODO Auto-generated catch block
                e.printStackTrace();
            }
        }
    }//GEN-LAST:event_LcabinetActionPerformed

    private void doorLActionPerformed(java.awt.event.ActionEvent evt) {//GEN-FIRST:event_doorLActionPerformed
 String url = "file:///Users/lois/Desktop/Map/src/map/DoorLeft.avi";

        if(Desktop.isDesktopSupported()){
            Desktop desktop = Desktop.getDesktop();
            try {
                desktop.browse(new URI(url));
            } catch (IOException | URISyntaxException e) {
                // TODO Auto-generated catch block
                e.printStackTrace();
            }
        }else{
            Runtime runtime = Runtime.getRuntime();
            try {
                runtime.exec("xdg-open " + url);
            } catch (IOException e) {
                // TODO Auto-generated catch block
                e.printStackTrace();
            }
        }        // TODO add your handling code here:
    }//GEN-LAST:event_doorLActionPerformed

    private void doorRActionPerformed(java.awt.event.ActionEvent evt) {//GEN-FIRST:event_doorRActionPerformed
        String url = "file:///Users/lois/Desktop/Map/src/map/DoorRight.avi";

               if(Desktop.isDesktopSupported()){
                   Desktop desktop = Desktop.getDesktop();
                   try {
                       desktop.browse(new URI(url));
                   } catch (IOException | URISyntaxException e) {
                       // TODO Auto-generated catch block
                       e.printStackTrace();
                   }
               }else{
                   Runtime runtime = Runtime.getRuntime();
                   try {
                       runtime.exec("xdg-open " + url);
                   } catch (IOException e) {
                       // TODO Auto-generated catch block
                       e.printStackTrace();
                   }
               }        // TODO add your handling code here:
    }//GEN-LAST:event_doorRActionPerformed

    private void FridgeLActionPerformed(java.awt.event.ActionEvent evt) {//GEN-FIRST:event_FridgeLActionPerformed
 String url = "file:///Users/lois/Desktop/Map/src/map/FridgeLeft.avi";

        if(Desktop.isDesktopSupported()){
            Desktop desktop = Desktop.getDesktop();
            try {
                desktop.browse(new URI(url));
            } catch (IOException | URISyntaxException e) {
                // TODO Auto-generated catch block
                e.printStackTrace();
            }
        }else{
            Runtime runtime = Runtime.getRuntime();
            try {
                runtime.exec("xdg-open " + url);
            } catch (IOException e) {
                // TODO Auto-generated catch block
                e.printStackTrace();
            }
        }        // TODO add your handling code here:
    }//GEN-LAST:event_FridgeLActionPerformed

    private void FridgeRActionPerformed(java.awt.event.ActionEvent evt) {//GEN-FIRST:event_FridgeRActionPerformed
        String url = "file:///Users/lois/Desktop/Map/src/map/FridgeRight.avi";

               if(Desktop.isDesktopSupported()){
                   Desktop desktop = Desktop.getDesktop();
                   try {
                       desktop.browse(new URI(url));
                   } catch (IOException | URISyntaxException e) {
                       // TODO Auto-generated catch block
                       e.printStackTrace();
                   }
               }else{
                   Runtime runtime = Runtime.getRuntime();
                   try {
                       runtime.exec("xdg-open " + url);
                   } catch (IOException e) {
                       // TODO Auto-generated catch block
                       e.printStackTrace();
                   }
               }        // TODO add your handling code here:
    }//GEN-LAST:event_FridgeRActionPerformed

    private void DrawerLActionPerformed(java.awt.event.ActionEvent evt) {//GEN-FIRST:event_DrawerLActionPerformed
         String url = "file:///Users/lois/Desktop/Map/src/map/openDrawersLeft.avi";

        if(Desktop.isDesktopSupported()){
            Desktop desktop = Desktop.getDesktop();
            try {
                desktop.browse(new URI(url));
            } catch (IOException | URISyntaxException e) {
                // TODO Auto-generated catch block
                e.printStackTrace();
            }
        }else{
            Runtime runtime = Runtime.getRuntime();
            try {
                runtime.exec("xdg-open " + url);
            } catch (IOException e) {
                // TODO Auto-generated catch block
                e.printStackTrace();
            }
        }        // TODO add your handling code here:
    }//GEN-LAST:event_DrawerLActionPerformed

    private void DrawerRActionPerformed(java.awt.event.ActionEvent evt) {//GEN-FIRST:event_DrawerRActionPerformed
        String url = "file:///Users/lois/Desktop/Map/src/map/OpenDrawerRight.avi";

        if(Desktop.isDesktopSupported()){
            Desktop desktop = Desktop.getDesktop();
            try {
                desktop.browse(new URI(url));
            } catch (IOException | URISyntaxException e) {
                // TODO Auto-generated catch block
                e.printStackTrace();
            }
        }else{
            Runtime runtime = Runtime.getRuntime();
            try {
                runtime.exec("xdg-open " + url);
            } catch (IOException e) {
                // TODO Auto-generated catch block
                e.printStackTrace();
            }
        }
    }//GEN-LAST:event_DrawerRActionPerformed

    
    
    private void drawArrowHead(Graphics2D g2, Point tip, Point tail,Color color){
        g2.setPaint(color);
        double dy=tip.y-tail.y;
        double dx=tip.x-tail.x;
        double theta = Math.atan2(dy, dx);
        double x,y,rho=theta+Math.toRadians(40);
        for (int j=0;j<2;j++){
            x=tip.x-20*Math.cos(rho);
            y=tip.y-20*Math.sin(rho);
            g2.draw(new Line2D.Double(tip.x,tip.y,x,y));
            rho=theta-Math.toRadians(40);
                    
        }
        
    }
    /**
     * @param args the command line arguments
     */
    
//    public static boolean isComplete(int size){
//        if(size == 5){
//            return true;
//        }else{
//            return false;
//        }
//    }
    
  
    public static void main(String args[]) throws Exception {
        /* Set the Nimbus look and feel */
        //<editor-fold defaultstate="collapsed" desc=" Look and feel setting code (optional) ">
        /* If Nimbus (introduced in Java SE 6) is not available, stay with the default look and feel.
         * For details see http://download.oracle.com/javase/tutorial/uiswing/lookandfeel/plaf.html 
         */
        try {
            for (javax.swing.UIManager.LookAndFeelInfo info : javax.swing.UIManager.getInstalledLookAndFeels()) {
                if ("Nimbus".equals(info.getName())) {
                    javax.swing.UIManager.setLookAndFeel(info.getClassName());
                    break;
                }
            }
        } catch (ClassNotFoundException ex) {
            java.util.logging.Logger.getLogger(KitchenMap.class.getName()).log(java.util.logging.Level.SEVERE, null, ex);
        } catch (InstantiationException ex) {
            java.util.logging.Logger.getLogger(KitchenMap.class.getName()).log(java.util.logging.Level.SEVERE, null, ex);
        } catch (IllegalAccessException ex) {
            java.util.logging.Logger.getLogger(KitchenMap.class.getName()).log(java.util.logging.Level.SEVERE, null, ex);
        } catch (javax.swing.UnsupportedLookAndFeelException ex) {
            java.util.logging.Logger.getLogger(KitchenMap.class.getName()).log(java.util.logging.Level.SEVERE, null, ex);
        }
        //</editor-fold>

        /* Create and display the form */
        java.awt.EventQueue.invokeLater(new Runnable() {
            public void run() {
                KitchenMap kit=new KitchenMap();
                kit.setVisible(true);
                kit.setTitle("Kitchen Map");
                
            }
        });
        
//        while(true){
//            //System.out.println(coor.size());
//            int size = coor.size();
//            
//            if(isComplete(size)){
//                Coordinate go =new Coordinate();
//                go.Coordinate(coor); 
//                signalStart=1;
//                System.out.println(signalStart);
//                break;
//            }
//            Thread.sleep(100);
//
//        }

    }
    
//     public void paint(Graphics G){
//     
//       {
//            super.paint(G);
//            G.setColor(Color.RED);
//            G.fillOval(50, 50, 30, 30);
//            
//       }
//       
//
//    }

    // Variables declaration - do not modify//GEN-BEGIN:variables
    private javax.swing.JButton DrawerL;
    private javax.swing.JButton DrawerR;
    private javax.swing.JButton FridgeL;
    private javax.swing.JButton FridgeR;
    private javax.swing.JButton Lcabinet;
    private javax.swing.JButton Rcabinet;
    private javax.swing.JLabel coordinate;
    private javax.swing.JButton doorL;
    private javax.swing.JButton doorR;
    private javax.swing.JButton jButton1;
    private javax.swing.JPanel jPanel1;
    private javax.swing.JLabel map;
    // End of variables declaration//GEN-END:variables

    

}
