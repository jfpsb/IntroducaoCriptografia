package model;

import java.util.HashMap;

public class Cifra {
	private String textoClaro = "";
	private String textoCifrado = "";
	private String diretorio;
	private String filename;
	private HashMap<Character, Integer> chaveMap = new HashMap<Character, Integer>();

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

	public HashMap<Character, Integer> getChaveMap() {
		return chaveMap;
	}

	public void setChaveMap(HashMap<Character, Integer> chave) {
		this.chaveMap = chave;
	}

	public String getDiretorio() {
		return diretorio;
	}

	public void setDiretorio(String diretorio) {
		this.diretorio = diretorio;
	}

	public String getFilename() {
		return filename;
	}

	public void setFilename(String filename) {
		this.filename = filename;
	}
}
