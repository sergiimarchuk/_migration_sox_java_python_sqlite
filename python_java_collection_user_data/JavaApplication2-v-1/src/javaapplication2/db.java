/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */
package javaapplication2;
import java.sql.*;
import javax.swing.*;
import javax.swing.JOptionPane;


/**
 *
 * @author Sergii.Marchuk
 */
public class db {
    
    Connection conn = null;
    public static Connection java_db(){
        
        
        try{
            
            Class.forName("org.sqlite.JDBC");
            //Connection conn = DriverManager.getConnection("jdbc:sqlite:C:\\Users\\sergii.marchuk\\Desktop\\untitled.db");
            Connection conn = DriverManager.getConnection("jdbc:sqlite:/opt/dev-py/untitled.db");
            return conn;
            
            
        }catch (Exception e){
            JOptionPane.showMessageDialog(null,e);
            return null;
            
        }
        
        
    }
    
}
