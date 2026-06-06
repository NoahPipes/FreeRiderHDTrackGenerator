//import java.awt.geom.Point2D;
import java.awt.Color;
import java.io.File;
import java.io.PrintWriter;
import java.util.*;
import java.lang.Math;
import java.lang.System;
import java.io.IOException;
import java.util.Random;

public class Track {
	//Track length
	private int trackLength = 500;
	
	//Physic line variables
	private int lineLength = 100;
	private Point2D start = new Point2D(-100, 100);
	private Point2D end = new Point2D(100, -100); //(100, -100)
	
	//Angle variables
	private int newAngle;
	private int oldAngle = 35;
	private int angleVariation = 6;
	
	//Boost variables (unused)
	private int boostProbability = 10;
	private Point2D boostPos = new Point2D(0, 0);
	
	//Checkpoint variables
	private int checkpointFrequency = 100;
	private Point2D checkpointPos = new Point2D();
	
	//Gray line variables
	private int density = 1;
	private int distance = 0;
	private Point2D grayStart = new Point2D(0, 0);
	private Point2D grayEnd = new Point2D(0, 0);
	
	//Teleport variables
	private Point2D teleportStart = new Point2D(start.getX() - 80, start.getY() + 100000);
	private Point2D teleportEnd = new Point2D();
	
	private Color rgb = new Color(0, 0, 0);
	
	//Strings
	private ArrayList<String> phyLines = new ArrayList<String>();
	private ArrayList<String> grayLines = new ArrayList<String>(Arrays.asList("#"));
	private ArrayList<String> powerups = new ArrayList<String>(Arrays.asList("#"));
	
	//Angle limits
	private int upperLimit = -20; //-45
	private int lowerLimit = 89; //22
	private boolean goingUp = true;
	private int angleBias = 0;
	
	private int counter = 0;
	
	//Base32 alphabet
	private final String alphabet = "0123456789abcdefghijklmnopqrstuv";
	
	//Star location
	private Point2D starPos = new Point2D();
	
	//random number generator
	Random rand = new Random();
	
/* 	public void main(String[] args) {
		generate();
	} */
	
	public void generate() {
		//starting platform
		phyLines.add(newLine(start.getX(), start.getY(), start.getX() + 300, start.getY()));
		start.setLocation(start.getX() + 300, start.getY());
		for (int x = 0; x < trackLength; x++) {
			// System.out.println("x: " + x);
			
			//change angle of line
			newAngle = newAngle();
			// System.out.println("here first");
			while (newAngle <= upperLimit || newAngle >= lowerLimit) {
				newAngle = newAngle();
			}
			
			// System.out.println("newAngle: " + newAngle);
			
			//set old angle to current angle
			oldAngle = newAngle;
			
			// System.out.println("here");

			
			//calculate endpoint
			end.setLocation(start.getX() + (Math.cos(Math.toRadians(newAngle)) * lineLength), start.getY() + (Math.sin(Math.toRadians(newAngle))) * lineLength);
			// System.out.println("End: " + end);
			// System.out.println("Problem: " + (Math.sin(Math.toRadians(newAngle))) * lineLength);
			//add to physics line array
			phyLines.add(newLine(start.getX(), start.getY(), end.getX(), end.getY()));
			
			start.setLocation(end.getX(), end.getY());
			
			counter++;
			
			for (int y = 0; y < rand.nextInt(50); y++) {
				// grayStart.setLocation(start.getX() + rand.nextInt(6401) - 3200, start.getY() + rand.nextInt(6401) - 3200);
				// grayEnd.setLocation(end.getX() + rand.nextInt(6401) - 3200, end.getY() + rand.nextInt(6401) - 3200);
				// grayLines.add(newLine(grayStart.getX(), grayStart.getY(), grayEnd.getX(), grayEnd.getY()));
				grayLines.add(newCircle(start.getX() + rand.nextInt(3600) - 1800, start.getY() + rand.nextInt(2000) - 1000, rand.nextInt(400)));
			}
			
			//add checkpoints at regular intervals
			if (counter % checkpointFrequency == 0) {
				checkpointPos.setLocation(end.getX() + (Math.cos(Math.toRadians(newAngle-90)) * 50), end.getY() + (Math.sin(Math.toRadians(newAngle - 90))) * 50);
				powerups.add(newPowerup(checkpointPos.getX(), checkpointPos.getY(), "C"));
				angleBias = rand.nextInt(13) - 10; //second number is always 3 less than the first number
			}
			// System.out.println("End of loop");
			if (counter % (trackLength / 100) == 0) {
				System.out.println(counter / (double) trackLength);
			}
			
		}
			
		//add star to end of track	
		starPos.setLocation(end.getX() + (Math.cos(Math.toRadians(newAngle-90)) * 50), end.getY() + (Math.sin(Math.toRadians(newAngle - 90))) * 50);
		powerups.add(newPowerup(starPos.getX(), starPos.getY(), "T"));
		
		//add both teleporters to the track
		teleportEnd.setLocation(end.getX(), end.getY() - 100000);
		powerups.add(newTeleport(teleportStart.getX(), teleportStart.getY(), teleportEnd.getX(), teleportEnd.getY()));
		
		//name text file
		try {
			PrintWriter textFile = new PrintWriter("Free Rider Tracks\\track - " + System.currentTimeMillis() + ".txt", "UTF-8");
			
			System.out.println("Creating file");
			
			//write physics lines to file
			for (String i : phyLines) {
				textFile.print(i);
			}
			System.out.println("Physics lines done");		
			
			//write gray lines to file
			for (String i : grayLines) {
				textFile.print(i);
			}
			System.out.println("Gray lines done");
			
			//write powerups to file
			for (String i : powerups) {
				textFile.print(i);
			}
			System.out.println("Powerups done");
			
			textFile.close();
		} catch (IOException e) {
			// System.out.println("Oops!");
            e.printStackTrace();
        }
		
		
	}
	
	private int newAngle() {
		return (int) (Math.random() * (2*angleVariation + 1)) - angleVariation + oldAngle + angleBias;
	}
	
	//convert double to base32 string
	private String b32(double num) {
		return Integer.toString((int) Math.round(num), 32);
	}
	
	private String newLine(double x1, double y1, double x2, double y2) {
		return b32(x1) + " " + b32(y1) + " " + b32(x2) + " " + b32(y2) + ",";
	}
	
	private String newPowerup(double x, double y, String powerupCode) {
		return powerupCode + " " + b32(x) + " " + b32(y) + ",";
	}
	
	private String newTeleport(double x1, double y1, double x2, double y2) {
		return "W " + b32(x1) + " " + b32(y1) + " " + b32(x2) + " " + b32(y2) + ",";
	}
	
	private String newCircle(double x, double y, double radius) {
		String answer = "";
		for (int t = 0; t < 360; t++) {
			answer += newLine(Math.cos(Math.toRadians(t)) * radius + x, Math.sin(Math.toRadians(t)) * radius + y, Math.cos(Math.toRadians(t+1)) * radius + x, Math.sin(Math.toRadians(t+1)) * radius + y);
		}
		return answer;
	}
}