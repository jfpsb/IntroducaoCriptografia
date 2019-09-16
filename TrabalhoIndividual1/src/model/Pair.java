package model;

import java.util.Comparator;

/**
 * Classe que representa um par de Character e Integer. Cada letra da string
 * informada pelo usu�rio como chave da criptografia representa uma chave no
 * Pair. Imaginando a chave informada pelo usu�rio como um vetor de caracteres,
 * a posi��o da letra no vetor ser� seu Value
 * 
 * @author jfpsb
 *
 */
public class Pair implements Comparator<Pair> {
	private Character key;
	private Integer value;

	public Pair() {
	}

	public Pair(Character key, Integer value) {
		this.key = key;
		this.value = value;
	}

	public Character getKey() {
		return key;
	}

	public void setKey(Character key) {
		this.key = key;
	}

	public Integer getValue() {
		return value;
	}

	public void setValue(Integer value) {
		this.value = value;
	}

	/**
	 * M�todo que compara as keys. Usado para ordena��o crescente da lista de Pairs
	 */
	@Override
	public int compare(Pair o1, Pair o2) {
		if (o1.getKey() == o2.getKey()) {
			return 0;
		} else if (o1.getKey() > o2.getKey()) {
			return 1;
		} else {
			return -1;
		}
	}

}
