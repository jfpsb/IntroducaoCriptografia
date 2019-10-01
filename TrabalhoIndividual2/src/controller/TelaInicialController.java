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

		inicializaEngrenagem();
	}

	/**
	 * Cifra texto
	 * 
	 * @throws Exception
	 */
	public void cifrar() throws Exception {
		// Variável que vai guardar texto cifrado
		String textoCifradoHolder = "";
		// Array de caracteres do texto claro
		char textoClaroArray[] = cifra.getTextoClaro().toCharArray();

		// Iterando sobre cada caracter do texto claro
		for (int i = 0; i < textoClaroArray.length; i++) {
			// Alimento cada caracter para a primeira engrenagem e o resultado desta para a
			// próxima até chegar na última
			Node nodeEng1 = engrenagem1.get(textoClaroArray[i]);
			Node nodeEng2 = engrenagem2.get(nodeEng1.getData());
			Node nodeEng3 = engrenagem3.get(nodeEng2.getData());

			// Rotaciona a engrenagem a cada caracter criptografado
			engrenagem1.rotacionar();

			// Adiciono o caracter cifrado na variável temporária de texto cifrado
			textoCifradoHolder += (char) nodeEng3.getData();
		}

		// Adiciono texto cifrado no model
		cifra.setTextoCifrado(textoCifradoHolder);
	}

	/**
	 * Decifra texto
	 * 
	 * @return Texto decifrado
	 * @throws NoSuchElementException
	 */
	public void decifrar() throws NoSuchElementException {
		String textoCifradoHolder = cifra.getTextoCifrado();
		char textoCifradoArray[] = textoCifradoHolder.toCharArray();
		String textoDecifradoHolder = "";

		// Coloco cada engrenagem em sua configuração inicial
		engrenagem1.reset();
		engrenagem2.reset();
		engrenagem3.reset();

		// Iterando por cada caracter do texto cifrado
		for (int i = 0; i < textoCifradoArray.length; i++) {
			// Para cada letra do alfabeto vou testar nos cilindros se o resultado é igual
			// ao do texto cifrado.
			// Em ASCII: 65 = A; 90 = Z;
			for (int letra = 65; letra <= 90; letra++) {
				Node nodeEng1 = engrenagem1.get(letra);
				Node nodeEng2 = engrenagem2.get(nodeEng1.getData());
				Node nodeEng3 = engrenagem3.get(nodeEng2.getData());

				// Se consulta nos cilindros der igual ao caractere presente no texto cifrado
				if (nodeEng3.getData() == textoCifradoArray[i]) {
					// Rotaciono engrenagem 1
					engrenagem1.rotacionar();

					// Adiciono o caracter encontrado à variável atualmente salvando texto decifrado
					textoDecifradoHolder += (char) letra;

					break;
				}
			}
		}

		// Salvo texto decifrado no model
		cifra.setTextoDecifrado(textoDecifradoHolder);
	}

	/**
	 * Salva em arquivo o texto cifrado
	 * 
	 * @throws FileNotFoundException
	 */
	public void salvarCifrado() throws FileNotFoundException {
		String filename = "Trabalho Indiv. 2 - " + cifra.getFilename() + " cifrado.txt";
		PrintWriter out = null;
		out = new PrintWriter(new FileOutputStream(cifra.getDiretorio() + File.separator + filename));
		out.println(cifra.getTextoCifrado());
		if (out != null) {
			out.flush();
			out.close();
		}
	}

	/**
	 * Salva texto decifrado em arquivo
	 * 
	 * @throws FileNotFoundException
	 */
	public void salvarDecifrado() throws FileNotFoundException {
		String filename = "Trabalho Indiv. 2 - " + cifra.getFilename() + " decifrado.txt";
		PrintWriter out = null;
		out = new PrintWriter(new FileOutputStream(cifra.getDiretorio() + File.separator + filename));
		out.println(cifra.getTextoDecifrado());
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

	/**
	 * Reseta o modelo para uma nova execução e atribui novos valores nas
	 * engrenagens
	 */
	public void reset() {
		cifra = new Cifra();
		inicializaEngrenagem();
	}

	/**
	 * Retorna cifra para acesso na view
	 * 
	 * @return Cifra
	 */
	public Cifra getCifra() {
		return cifra;
	}

	/**
	 * Inicializa engrenagens e configura as referências de engrenagem
	 */
	private void inicializaEngrenagem() {
		engrenagem1 = new Engrenagem();
		engrenagem2 = new Engrenagem();
		engrenagem3 = new Engrenagem();

		engrenagem1.setNextEngrenagem(engrenagem2);
		engrenagem2.setNextEngrenagem(engrenagem3);
		engrenagem3.setNextEngrenagem(engrenagem1);
	}
}
