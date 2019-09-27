package model;

/**
 * Classe que representa um item da engrenagem (cilindro). Cada instância guarda
 * o data, que representa a letra no alfabeto, e uma referência à próxima letra
 * do cilindro
 * 
 * @author jfpsb
 *
 */
public class Node {
	private int data;
	private Node next;

	public Node(int data) {
		this.data = data;
	}

	public int getData() {
		return data;
	}

	public void setData(int data) {
		this.data = data;
	}

	public Node getNext() {
		return next;
	}

	public void setNext(Node next) {
		this.next = next;
	}

}
