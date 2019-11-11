package SkipList;

public class Main {
	public static void main(String args[]) {
		SkipList<String> list = new SkipList<String>();
		System.out.println(list);
		list.insert(2, "1");
		list.insert(1, "2");
		list.insert(3, "3");
		list.insert(5, "4");
		list.insert(4, "5");
		list.insert(7, "6");
		list.insert(2, "7");
		System.out.println(list);
		System.out.println(list.size());
	}
}
