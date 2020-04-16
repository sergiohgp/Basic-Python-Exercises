/**
 * 
 */
package workshop2;
import java.util.ArrayList;
import java.util.Scanner;

/**
 * @author sergiohgp
 *
 */
public class WorkShop2 {

	/**
	 * @param args
	 */
	public static void main(String[] args) {
		// TODO Auto-generated method stub
		
		// 1. Defensive programming and validation loop!
		// 2. Array, ArrayList, LinkList
		// 3. DataBase Connectivity
		
		// Declare
//		int num, sum = 0;
//		Scanner keyboard;
//		char anwser;
//		
//		while(true) {
//			
//			try {
//				keyboard = new Scanner(System.in);
//				System.out.println("Enter a number between 0 and 100: ");
//				num = keyboard.nextInt();
//				
//				if (num > 100 || num < 0) {
//					System.out.println("Input is put of range.");
//					System.out.println("Try again.");
//				}
//				else {
//					sum += num;
//					System.out.println("Type yes if you have any other number: ");
//					anwser = keyboard.next().charAt(0);
//					
//					if (anwser == 'n' || anwser == 'N') {
//						System.out.println("The sum is " + sum);
//						System.out.println("Thanks for using the program!");
//						break;
//					}
//					
//				}
//				
//				
//			}
//			catch (Exception e) {
//				System.out.println("Wrong type of input!");
//				System.out.println("Try again.");
//			}
//
//		}
		
		
		
		// ============================ DATA COLLECTION ======================== //
		
		int [] arr = new int [5]; // size has to be declared // type has to be declared
		arr[0] = 5;
		
			for (int i = 0; i < arr.length; i++) {
				System.out.println("arr[" + i + "] = " + arr[i]);
			}
			
			for (int number : arr) { //pick each index value and place into variable number
				System.out.println(number);
			}
			
		Rectangle rec1 = new Rectangle(3,4);
		System.out.println(rec1);
		
		//toString() is a method that includes in any class
		
		System.out.println(rec1.toString());
			
		Rectangle [] recArr = new Rectangle[5];
		
			for (int i = 0; i < recArr.length; i++) {
				recArr[i] = new Rectangle(i, i+2);
			}
			
			for (Rectangle rectangle : recArr) {
				System.out.println(rectangle);
			}
			
		// ================ ArrayList and LinkList ===========//
			
		// 1. Dynamic! By default, it holds 10 memory locations
		// 2. ArrayList can only hold objects
				
		ArrayList<Rectangle> recArrList = new ArrayList<Rectangle> ();
		ArrayList<String> stringArrList = new ArrayList<String> ();
		
		// Boxing and unboxing
		ArrayList<Float> floatArrList = new ArrayList<Float> ();
		floatArrList.add(3.45f);
		floatArrList.add(13.45f);
		floatArrList.add(3.45f);
		floatArrList.add(32.45f);
		
		// to get indivudual number from the array
		System.out.println(floatArrList.get(0));
		
		// insert in a specific location in the array
		floatArrList.add(2, 11.11f);
		
		
		
		
		ArrayList<Double> doubleArrList = new ArrayList<Double> ();
		double a = 6.5;
		
		// search for differences between lists (ArrList and LinkList)
	}

}


