package Test;

import java.util.Comparator;
import java.util.HashSet;
import java.util.List;
import java.util.PriorityQueue;
import java.util.Set;

class DijkstraPriorityQueue{
	// number of vertices
	private int num;
	// List of distances
	private int dist[];
	
	private Set<Integer> settled;
	private List<List<Node>> adjList;
	private PriorityQueue<Node> priorityQueue;
	
	public DijkstraPriorityQueue(int num) {
		this.num = num;
		dist = new int[num];
		settled = new HashSet<Integer>();
		priorityQueue = new PriorityQueue<Node>(num, new Node());
	}
	
	public void dijkstra(List<List<Node>> adjList, int src) {
		this.adjList = adjList;
		
		// Initialize single source
		for(int i = 0; i < num; i ++) {
			// dist[i] -> ∞
			dist[i] = Integer.MAX_VALUE;
		}
		
		// Add the source node to the priority queue
		priorityQueue.add(new Node(src, 0));
		
		// The distance to source is 0
		dist[src] = 0;
		while(settled.size() != num) {
			// remove the minimum distance node from the priority queue
			int u = priorityQueue.remove().getNode();
			settled.add(u);
			e_Neighbours(u);
		}
	}
	
	private void e_Neighbours(int u) {
		int edgeDistance = -1;
		int newDistance = -1;
		// All the neighbors of v
		for(int i = 0; i < adjList.get(u).size(); i++) {
			Node v = adjList.get(u).get(i);
			// If the current node hasn't be processed
			if(! settled.contains(v.getNode())) {
				edgeDistance = v.getCost();
				newDistance = dist[u] + edgeDistance;
			}
			
			// If the way is better
			if(newDistance < dist[v.getNode()]) {
				dist[v.getNode()] = newDistance;
			}
			
			priorityQueue.add(new Node(v.getNode(), dist[v.getNode()]));
		}
	}
}

class Node implements Comparator<Node>{
	private int node;
	private int cost;
	
	public Node() {}
	
	public Node(int node, int cost) {
		this.node = node;
		this.cost = cost;
	}
	
	public int compare(Node n1, Node n2) {
		if(n1.cost < n2.cost) {
			return -1;
		}else if(n1.cost > n2.cost) {
			return 1;
		}else {
			return 0;
		}
	}
	
	public int getNode() {
		return this.node;
	}
	
	public int getCost() {
		return this.cost;
	}
}

public class Dijkstra {
	public static void main(String[] args) {
		
	}
}
