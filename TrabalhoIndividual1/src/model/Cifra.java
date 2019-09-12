package model;

import java.util.HashMap;

public class Cifra {
	private String textoClaro = "";
	private String textoCifrado = "";
	private String chave;
	private HashMap<Character, Integer> chaveMap = new HashMap<Character, Integer>();

	public void cifrar() {
		int chaveLenght = chave.length();
		int leftover = textoClaro.length() % chaveLenght;
		
		for(int i = 0; i < leftover; i++) {
			textoClaro += (char) (97 + i);
		}
		
		char textoClaroChar[] = textoClaro.toCharArray();
		
		for(int i : chaveMap.values()) {
			int aux = i;
			
			while(aux < textoClaroChar.length) {
				System.out.print(textoClaroChar[aux]);
				aux += chaveLenght;				
			}
		}
	}

	public String getTextoClaro() {
		return textoClaro;
	}

	public void setTextoClaro(String textoClaro) {
		this.textoClaro = textoClaro;
	}

	public String getTextoCifrado() {
		return textoCifrado;
	}

	public void setTextoCifrado(String textoCifrado) {
		this.textoCifrado = textoCifrado;
	}

	public void setChave(String chave) {
		this.chave = chave;
	}

	public HashMap<Character, Integer> getChaveMap() {
		return chaveMap;
	}

	public void setChaveMap(HashMap<Character, Integer> chave) {
		this.chaveMap = chave;
	}
}
