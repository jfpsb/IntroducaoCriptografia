package model;

import java.util.ArrayList;
import java.util.Collections;

/**
 * Lista circular usando {@link Node Nodes} que representa uma engrenagem
 * (cilindro, rotor) da máquina de rotação com 26 campos, cada um representando
 * um caracter do alfabeto
 * 
 * @author jfpsb
 *
 */
public class Engrenagem {
	/**
	 * Primeiro item da lista circular
	 */
	private Node head;
	/**
	 * Último item da lista circular de itens
	 */
	private Node last;
	/**
	 * Próxima engrenagem que será rotacionada quando esta engranagem fizer uma
	 * revolução completa
	 */
	private Engrenagem nextEngrenagem;
	/**
	 * Tamanho da lista circular
	 */
	private int size = 0;
	/**
	 * Guarda quantas vezes essa engrenagem já foi rotacionada
	 */
	private int rotacionado = 0;

	private ArrayList<Integer> numeros;

	/**
	 * Construtor de engrenagem que atribui letras aleatórias
	 */
	public Engrenagem() {
		numeros = new ArrayList<Integer>();

		// Crio uma lista com todas as letras do alfabeto.
		// O número 65 representa o A (maiúsculo) na tabela ASCII.
		// Letras são guardadas de acordo com seus valores na tabela ASCII.
		for (int i = 0; i < 26; i++) {
			numeros.add(i + 65);
		}

		// Embaralha números em lista
		Collections.shuffle(numeros);

		// Adiciono letras embaralhadas na lista circular
		for (int i : numeros) {
			add(i);
		}

	}

	/**
	 * Adiciona item ao final da lista circular
	 * 
	 * @param data Valor do item
	 */
	public void add(int data) {
		if (size < 26) {
			Node n = new Node(data);

			if (size == 0) {
				head = n;
				last = n;
				n.setNext(head);
			} else {
				n.setNext(head);
				last.setNext(n);
				last = n;
			}

			size++;
		} else {
			System.out.println("Engrenagem Já Possui 26 Letras");
		}
	}

	/**
	 * Retorna o elemento da lista circular em relação ao head
	 * 
	 * @param index Posição do item em relação a head da lista circular
	 * @return Node da engrenagem
	 */
	public Node get(int index) {
		Node temp = null;

		if (head != null) {
			temp = head;
			int aux = 65;

			while (aux < index) {
				temp = temp.getNext();
				aux++;
			}
		}

		return temp;
	}

	/**
	 * Limpa itens da lista circular
	 */
	public void clear() {
		head = null;
		last = null;
		size = 0;
		rotacionado = 0;
	}

	/**
	 * Rotaciona o itens do cilindro. Quando houver 26 rotações a próxima engrenagem
	 * é rotacionada uma única vez
	 */
	public void rotacionar() {

		Node antepenultimoNode;

		// Recupero o antepenúltimo Node em relação à head.
		// Número 65 necessário, pois as letras na engrenagem são guardadas de acordo
		// com seus valores na tabela ASCII.
		// 65 representa o A (maiúsculo)
		antepenultimoNode = get(24 + 65);
		// A atribuição já realiza a rotação
		// Rotação no sentido de cima para baixo
		head = last;
		last = antepenultimoNode;

		// Incrementa a quantidade de rotações já efetuadas
		rotacionado++;

		// Se engrenagem tiver rotacionado 26 vezes, a próxima engrenagem será
		// rotacionada uma vez
		if (rotacionado == 26) {
			rotacionado = 0;
			nextEngrenagem.rotacionar();
		}
	}

	/**
	 * Reseta engrenagem às posições iniciais
	 */
	public void reset() {
		clear();

		for (int i = 0; i < 26; i++) {
			add(numeros.get(i));
		}
	}

	public Node getHead() {
		return head;
	}

	public Node getLast() {
		return last;
	}

	public int getSize() {
		return size;
	}

	public Engrenagem getNextEngrenagem() {
		return nextEngrenagem;
	}

	public void setNextEngrenagem(Engrenagem nextEngrenagem) {
		this.nextEngrenagem = nextEngrenagem;
	}
}
