import java.util.Scanner;
class Main { 

	static int findMinLength(String arr[], int m) 
	{ 
		int min = Integer.MAX_VALUE; 
		for (int i = 0; i <= (m - 1); i++) 
		{ 
			if (arr[i].length() < min) { 
				min = arr[i].length(); 
			} 
		} 
		return min; 
	} 

	static boolean allContainsPrefix(String arr[], int m, 
						String str, int start, int end) 
	{ 
		for (int i = 0; i <= (m - 1); i++) 
		{ 
			String arr_i = arr[i]; 
			
			for (int j = start; j <= end; j++) 
				if (arr_i.charAt(j) != str.charAt(j)) 
					return false; 
		} 
		return true; 
	} 

	static String commonPrefix(String arr[], int m) 
	{ 
		int index = findMinLength(arr, m); 
		String prefix = "";  

		int low = 0, high = index; 
		while (low <= high) { 
			
			int mid = low + (high - low) / 2; 

			if (allContainsPrefix(arr, m, arr[0], low, 
												mid)) 
			{ 
				 
				prefix = prefix + arr[0].substring(low,mid + 1); 
				low = mid + 1; 
			} 
			else  
			{ 
				high = mid - 1; 
			} 
		} 

		return prefix; 
	} 

	public static void main(String args[]) 
	{ 
		
		String arr[] = new String[50];
		Scanner sc = new Scanner(System.in);
		int k =sc.nextInt();
		int m=0;
		for(int i=0;i<k;i++)
		{
		    arr[i]=sc.next();
		    n++;
		}
		
        String ans = commonPrefix(arr, m); 
		
		if (ans.length() > 0) 
			System.out.println(ans); 
		else
			System.out.println("There is no common"
									+ " prefix"); 
	} 
} 
