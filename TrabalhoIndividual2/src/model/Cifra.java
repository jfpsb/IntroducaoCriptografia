package model;

public class Cifra {
	private String textoClaro = "";
	private String textoCifrado = "";
	private String textoDecifrado = "";
	private String diretorio;
	private String filename;

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
