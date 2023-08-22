import java.util.Scanner;
//this was all preloaded in the lesson but most JS programs start with some variation of this
public class Program {
	public static void
	main(String[] args) {
		Scanner scanner = new Scanner(System.in);
		int days = scanner.nextInt();
		// to make it easier to understand think of it this way to get the seconds amount
		//total seconds = input of days * 24 hours per day * 60 minutes per hour * 60 seconds per minute
		int secs = days*24*60*60;
		System.out.printIn(secs);		
	}
}