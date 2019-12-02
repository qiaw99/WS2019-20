package Test;

import java.util.ArrayList;

class AMWGraph{
	private ArrayList vertexList;
	private int[][] edges;
	private int numOfEdges;
	
	public AMWGraph(int n) {
		this.edges = new int [n][n];
		this.vertexList = new ArrayList(n);
		numOfEdges = 0;
	}
	
	public int getNumOfVertex() {
		return this.vertexList.size();
	}
	
	public int getNumOfEdges() {
		return this.numOfEdges;
	}
	
	public Object getValueByIndex(int i) {
		return this.vertexList.get(i);
	}
	
	public int weight(int v1, int v2) {
		return this.edges[v1][v2];
	}
	
	public void insertVertex(Object vertex) {
		this.vertexList.add(vertexList.size(), vertex);
	}
	
	public void insertEdge(int v1, int v2, int weight) {
		this.edges[v1][v2] = weight;
		numOfEdges ++;
	}
	
	public void deleteEdge(int v1, int v2) {
		edges[v1][v2] = 0;
		numOfEdges --;
	}
	
	/**
	 * Get the index of the fist next Vertex
	 * @param index
	 * @return
	 */
	public int getFirstNeighbor(int index) {
		for(int j = 0; j < vertexList.size(); j++) {
			if(edges[index][j] > 0) {
				return j;
			}
		}
		return -1;
	}
	
	public int getNextNeighbor(int v1, int v2) {
		for(int j = v2 + 1; j < vertexList.size(); j++) {
			if(edges[v1][j] > 0) {
				return j;
			}
		}
		return -1;
	}
	
	private void depthFirstSearch(boolean[] isVisited, int i) {
		System.out.println(getValueByIndex(i) + " ");
		isVisited[i] = true;
		
		int v = getFirstNeighbor(i);
		while(v != -1) {
			if(!isVisited[v]) {
				depthFirstSearch(isVisited, v);
			}
			v = getNextNeighbor(i, v);
		}
	}
	
	public void depthFirstSearch(boolean[] isVisited) {
		System.out.println(getNumOfVertex());
		for(int i = 0; i < getNumOfVertex(); i++) {
			if(!isVisited[i]) {
				depthFirstSearch(isVisited, i);
			}
		}
	}
}

public class BFS {
	public static void main(String args[]) {
		int n = 8, e = 9;
        String labels[]={"1","2","3","4","5","6","7","8"};
        AMWGraph graph = new AMWGraph(n);
        for(String label:labels) {
            graph.insertVertex(label);
        }
        
        boolean[] isVisited = new boolean[] {false,false,false,false,false,false,false,false};
        
        graph.insertEdge(0, 1, 1);
        graph.insertEdge(0, 2, 1);
        graph.insertEdge(1, 3, 1);
        graph.insertEdge(1, 4, 1);
        graph.insertEdge(3, 7, 1);
        graph.insertEdge(4, 7, 1);
        graph.insertEdge(2, 5, 1);
        graph.insertEdge(2, 6, 1);
        graph.insertEdge(5, 6, 1);
        graph.insertEdge(1, 0, 1);
        graph.insertEdge(2, 0, 1);
        graph.insertEdge(3, 1, 1);
        graph.insertEdge(4, 1, 1);
        graph.insertEdge(7, 3, 1);
        graph.insertEdge(7, 4, 1);
        graph.insertEdge(6, 2, 1);
        graph.insertEdge(5, 2, 1);
        graph.insertEdge(6, 5, 1);
        
        System.out.println("Depth first search order: ");
        graph.depthFirstSearch(isVisited);
	}
}
