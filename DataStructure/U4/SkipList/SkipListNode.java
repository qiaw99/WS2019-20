package SkipList;

class SkipListNode<T>{
	protected int key;
	protected T value;
	protected SkipListNode<T> up, down, left, right;
	
	public static final int HEAD_KEY = Integer.MIN_VALUE;
	public static final int TAIL_KEY = Integer.MAX_VALUE;
	
	public SkipListNode(int key, T value) {
		this.key = key;
		this.value = value;
	}
	
	public int getKey() {
		return this.key;
	}
	
	public T getValue() {
		return this.value;
	}
	
	public void setKey(int key) {
		this.key = key;
	}
	
	public void setValue(T value) {
		this.value = value;
	}
	
	public boolean equals(Object o) {
		if(this == o) {
			return true;
		}
		if(o == null) {
			return false;
		}
		if(!(o instanceof SkipListNode<?>)) {
			return false;
		}
		
		SkipListNode<T> temp;
		try {
			temp = (SkipListNode<T>) o;
		}catch(ClassCastException e) {
			return false;
		}
		return (temp.getKey() == this.key) && (temp.getValue() == this.value);
	}
	
	@Override
	public String toString() {
		return "key: " + this.key + ", value: " + this.value;
	}
} 
