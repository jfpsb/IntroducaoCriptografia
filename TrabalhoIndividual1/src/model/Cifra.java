package model;

import java.util.ArrayList;
import java.util.HashMap;

public class Cifra {
	private String textoClaro = "";
	private String textoCifrado = "";
	private String textoDecifrado = "";
	private String diretorio;
	private String filename;
	private ArrayList<Pair> chave = new ArrayList<Pair>();

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

	public ArrayList<Pair> getChave() {
		return chave;
	}

	public void setChave(ArrayList<Pair> chave) {
		this.chave = chave;
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
	
	public String getTextoDecifrado() {
		return textoDecifrado;
	}

	public void setTextoDecifrado(String textoDecifrado) {
		this.textoDecifrado = textoDecifrado;
	}
}
