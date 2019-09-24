package controller;

import java.io.File;
import java.io.FileNotFoundException;
import java.io.FileOutputStream;
import java.io.PrintWriter;
import java.util.NoSuchElementException;
import java.util.Scanner;

import model.Cifra;
import view.TelaInicial;

public class TelaInicialController {
	private Cifra cifra;
	private TelaInicial view;

	public TelaInicialController(TelaInicial view) {
		this.view = view;
		cifra = new Cifra();
	}

	/**
	 * Cifra texto
	 * 
	 * @throws Exception
	 */
	public void cifrar() throws Exception {
	}

	/**
	 * Decifra texto
	 * 
	 * @return Texto decifrado
	 * @throws NoSuchElementException
	 */
	public String decifrar() throws NoSuchElementException {
		return null;
	}

	/**
	 * Salva em arquivo o texto cifrado
	 * 
	 * @throws FileNotFoundException
	 */
	public void salvarCifrado() throws FileNotFoundException {
		String filename = cifra.getFilename() + " cifrado.txt";
		PrintWriter out = null;
		out = new PrintWriter(new FileOutputStream(cifra.getDiretorio() + "\\" + filename));
		out.println(cifra.getTextoCifrado());
		if (out != null) {
			out.flush();
			out.close();
		}
	}

	/**
	 * Salva texto decifrado em arquivo
	 * 
	 * @param textoDecifrado Texto decifrado
	 * @throws FileNotFoundException
	 */
	public void salvarDecifrado(String textoDecifrado) throws FileNotFoundException {
		String filename = cifra.getFilename() + " decifrado.txt";
		PrintWriter out = null;
		out = new PrintWriter(new FileOutputStream(cifra.getDiretorio() + "\\" + filename));
		out.println(textoDecifrado);
		if (out != null) {
			out.flush();
			out.close();
		}
	}

	/**
	 * Lê de arquivo o texto claro a ser cifrado
	 * 
	 * @param path Caminho do arquivo
	 */
	public void carregaTextoClaro(String path) {
		Scanner scanner = null;
		try {
			scanner = new Scanner(new File(path), "UTF-8");
			// Usa a expressão regular \A como delimitador
			// Significa que o texto no arquivo será delimitado pelo seu começo
			// e vai tornar o texto inteiro do texto uma só string
			cifra.setTextoClaro(scanner.useDelimiter("\\A").next());
		} catch (FileNotFoundException e) {
			e.printStackTrace();
		} finally {
			if (scanner != null)
				scanner.close();
		}
	}

	public void setChave(String chave) {

	}

	public void reset() {
		cifra = new Cifra();
	}

	public Cifra getCifra() {
		return cifra;
	}
}
