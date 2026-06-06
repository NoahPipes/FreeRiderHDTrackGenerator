
public class Point2D {
	private double x;
	private double y;
	
	Point2D() {
		this.x = 0;
		this.y = 0;
	}
	
	Point2D(double x, double y) {
		this.x = x;
		this.y = y;
	}
	
	public void setLocation(double x, double y) {
		this.x = x;
		this.y = y;
	}
	
	public double getX() {
		return this.x;
	}
	
	public double getY() {
		return this.y;
	}
	
	public String toString() {
		return this.x + ", " + this.y;
	}
}