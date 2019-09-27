package controller;

import java.io.File;
import java.io.FileNotFoundException;
import java.io.FileOutputStream;
import java.io.PrintWriter;
import java.util.NoSuchElementException;
import java.util.Scanner;

import model.Cifra;
import model.Engrenagem;
import model.Node;
import view.TelaInicial;

public class TelaInicialController {
	private Cifra cifra;
	private TelaInicial view;

	private Engrenagem engrenagem1;
	private Engrenagem engrenagem2;
	private Engrenagem engrenagem3;

	public TelaInicialController(TelaInicial view) {
		this.view = view;
		cifra = new Cifra();

		engrenagem1 = new Engrenagem();
		engrenagem2 = new Engrenagem();
		engrenagem3 = new Engrenagem();

		engrenagem1.setNextEngrenagem(engrenagem2);
		engrenagem2.setNextEngrenagem(engrenagem3);
		engrenagem3.setNextEngrenagem(engrenagem1);
	}

	/**
	 * Cifra texto
	 * 
	 * @throws Exception
	 */
	public void cifrar() throws Exception {
		char textoClaroArray[] = cifra.getTextoClaro().toCharArray();

		for (int i = 0; i < textoClaroArray.length; i++) {

			Node nodeEng1 = engrenagem1.get(textoClaroArray[i]);
			Node nodeEng2 = engrenagem2.get(nodeEng1.getData());
			Node nodeEng3 = engrenagem3.get(nodeEng2.getData());

			engrenagem1.rotacionar();

			System.out.print((char) nodeEng3.getData());
		}
		
		System.out.println();
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
			// Significa que o texto no arquivo será inicialmente delimitado pelo seu começo
			// e vai tornar o texto inteiro do texto uma só string.
			// Coloca o texto inteiro em caracteres maiúsculos.
			// Substitui todos os espaços no texto pela letra X.
			cifra.setTextoClaro(scanner.useDelimiter("\\A").next().toUpperCase().replace(' ', 'X'));
		} catch (FileNotFoundException e) {
			e.printStackTrace();
		} finally {
			if (scanner != null)
				scanner.close();
		}
	}

	public void reset() {
		cifra = new Cifra();
	}

	public Cifra getCifra() {
		return cifra;
	}
}
