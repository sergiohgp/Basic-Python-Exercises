/**
 * 
 */
package workshop2;

/**
 * @author sergiohgp
 *
 */
public class Rectangle {
	
	public Rectangle(double width, double length) {
		super();
		this.width = width;
		this.length = length;
	}
	
	private double width;
	private double length;
	
	public double getWidth() {
		return width;
	}

	public void setWidth(double width) {
		this.width = width;
	}

	public double getLength() {
		return length;
	}

	public void setLength(double lenght) {
		this.length = lenght;
	}
	
	public double getArea() {
		return width * length;
	}


	@Override
	public String toString() {
		return "Rectangle [width=" + width + ", length=" + length + ", area=" + getArea() + "]";
	}
	
	

	
	
	
	
	
		
		

	}

}
