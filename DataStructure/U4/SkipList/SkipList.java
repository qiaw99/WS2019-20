package SkipList;

import java.util.Random;

public class SkipList<T> {
	private SkipListNode<T> head, tail;
	private int nodes;
	private int listLevel;
	private Random random;
	private static final double PROBABILITY = 0.5;
	
	public SkipList() {
		this.random= new Random();
		clear();
	}
	
	public void clear() {
		head = new SkipListNode<T>(SkipListNode.HEAD_KEY, null);
		tail = new SkipListNode<T>(SkipListNode.TAIL_KEY, null);
		this.nodes = 0;
		this.listLevel = 0;
		horizontalLink(head, tail);
	}
	
	public boolean isEmpty() {
		return this.nodes == 0;
	}
	
	public int size() {
		return this.nodes;
	}	
	
	/**
	 * Find the position before where key should be inserted in the last level 
	 * @param key
	 * @return	temp
	 */
	protected SkipListNode<T> findNode(int key){
		SkipListNode<T> temp = head;
		while(true) {
			while(temp.right.key != SkipListNode.TAIL_KEY && temp.right.key < key) {
				temp = temp.right;
			}
			if(temp.down != null) {
				temp = temp.down;
			}else {
				break;
			}
		}
		return temp;
	}
	
	protected SkipListNode<T> search(int key){
		SkipListNode<T> temp = findNode(key);
		if(key == temp.getKey())
			return temp;
		else
			return null;
	}
		
	protected void insert(int key, T value) {
		SkipListNode<T> temp = findNode(key);
		if(key == temp.getKey()) {
			temp.value = value;
		}
		
		SkipListNode<T> newNode = new SkipListNode(key, value);
		int currentLevel = 0;
		backLink(temp, newNode);
		while(random.nextDouble() < PROBABILITY) {
			if(currentLevel >= this.listLevel) {
				this.listLevel ++;
				SkipListNode<T> n1 = new SkipListNode<T>(SkipListNode.HEAD_KEY, null);
				SkipListNode<T> n2 = new SkipListNode<T>(SkipListNode.TAIL_KEY, null);
				horizontalLink(n1, n2);
				verticalLink(n1, head);
				verticalLink(n2, tail);
				this.head = n1;
				this.tail = n2;
			}
			while(temp.up == null) {
				temp = temp.left;
			}
			temp = temp.up;
			
			SkipListNode<T> n3 = new SkipListNode<T>(key, null);
			backLink(temp, n3);		// Insert n3 behind temp
			verticalLink(n3, newNode);
			newNode = n3;
			currentLevel ++;
		}
		this.nodes ++;
	}	
		
	private void backLink(SkipListNode<T> node1, SkipListNode<T> node2) {
		node2.left = node1;
		node2.right = node1.right;
		node1.right.left = node2;
		node1.right = node2;
	}	
		
	private void verticalLink(SkipListNode<T> node1, SkipListNode<T> node2) {
		node1.down = node2;
		node2.up = node1;
	}	
		
	private void horizontalLink(SkipListNode<T> node1, SkipListNode<T> node2){
		node1.right = node2;
		node2.left = node1;
	}		
	
	public String toString() {
		if(isEmpty()) {
			return "The SkipList is empty!";
		}
		StringBuilder builder = new StringBuilder();
		SkipListNode<T> temp = this.head;
		while(temp.down != null) {
			temp = temp.down;
		}
		while(temp.left != null) {
			temp = temp.left;
		}
		if(temp.right != null) {
			temp = temp.right;
		}
		while(temp.right != null) {
			builder.append(temp);
			builder.append("\n");
			temp = temp.right;
		}
		return builder.toString();
	}
}
