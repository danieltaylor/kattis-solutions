import java.util.HashMap;
import java.util.Map;
import java.util.Scanner;

public class Metaprogramming {
	public static void main(String[] args) {
		Scanner s = new Scanner(System.in);
		Map<String, Integer> definitions = new HashMap<String, Integer>();

		while (s.hasNext()) {
			String command = s.next();
			switch (command) {
				case "define":
					int val = s.nextInt();
					String var = s.next();
					definitions.put(var, val);
					break;
				case "eval":
					String var1 = s.next();
					String operator = s.next();
					String var2 = s.next();
					if (definitions.containsKey(var1) && definitions.containsKey(var2)) {
						int val1 = definitions.get(var1);
						int val2 = definitions.get(var2);
						switch (operator) {
							case "<":
								System.out.println(val1 < val2);
								break;
							case ">":
								System.out.println(val1 > val2);
								break;
							case "=":
								System.out.println(val1 == val2);
								break;
						}
					} else {
						System.out.println("undefined");
					}
					break;
			}
		}
	}
}
