package controller;

import java.io.File;
import java.io.FileNotFoundException;
import java.io.FileOutputStream;
import java.io.PrintWriter;
import java.util.ArrayList;
import java.util.Iterator;
import java.util.NoSuchElementException;
import java.util.Scanner;

import model.Cifra;
import model.Pair;
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

		// Testa se o texto claro foi fornecido pelo usu�rio
		if (cifra.getTextoClaro().trim().isEmpty()) {
			throw new Exception("Texto Claro N�o Foi Definido ou � Vazio");
		}

		// Testa se chave foi fornecida pelo usu�rio
		if (cifra.getChave().size() == 0) {
			throw new Exception("Chave N�o Foi Informada");
		}

		String textoClaroHolder = cifra.getTextoClaro();
		// Tamanho da chave
		int chaveLenght = cifra.getChave().size();
		// Calcula quantos campos faltam no texto claro para completar a cifragem
		int camposRestantes = 0;
		if ((textoClaroHolder.length() % chaveLenght) != 0)
			camposRestantes = chaveLenght - (textoClaroHolder.length() % chaveLenght);

		for (int i = 0; i < camposRestantes; i++) {
			// Adiciona aos campos sem texto outras letras come�ando do "a" min�sculo
			// C�digo 97 em ASCII igual a letra "a"
			textoClaroHolder += (char) (97 + i);
		}

		// N�mero de linhas na 'matriz'
		int linhas = textoClaroHolder.length() / cifra.getChave().size();

		String cifrado; // Vari�vel que vai guardar o texto decifrado em cada est�gio

		// Tr�s est�gios de transposi��o
		for (int p = 0; p < 3; p++) {
			// Converte texto claro em array de char
			char textoClaroChar[] = textoClaroHolder.toCharArray();

			cifrado = "";

			Iterator<Pair> iterator = cifra.getChave().iterator();

			while (iterator.hasNext()) {
				Pair pair = iterator.next();

				int index = pair.getValue();

				for (int j = 0; j < linhas; j++) {
					cifrado += textoClaroChar[index];
					// Somo o tamanho da chave ao index pra pular pra pr�xima linha da matriz
					// imagin�ria mas continuando na mesma coluna
					index += chaveLenght;
				}
			}

			textoClaroHolder = cifrado;
		}

		cifra.setTextoCifrado(textoClaroHolder);
	}

	/**
	 * Decifra texto
	 * 
	 * @return Texto decifrado
	 * @throws NoSuchElementException
	 */
	public void decifrar() throws NoSuchElementException {
		// Tamanho da chave
		int chaveLenght = cifra.getChave().size();
		// Vetor de char que vai guardar cada caracter do texto decifrado
		char decifradoArray[] = new char[cifra.getTextoCifrado().length()];
		// N�mero de linhas na 'matriz imagin�ria'
		int linhas = cifra.getTextoCifrado().length() / cifra.getChave().size();

		// Onde texto decifrado vai ficar guardado em cada est�gio.
		// No in�cio guardo o texto cifrado nesta vari�vel
		String decifrado = cifra.getTextoCifrado();

		for (int i = 0; i < 3; i++) {
			// A vari�vel "decifrado" vai de fato guardar o texto cifrado at� o t�rmino da
			// execu��o do �ltimo est�gio da decifragem. Ap�s isso nela estar� o texto
			// decifrado.
			// Guardo texto cifrado em vetor de char.
			char textoCifradoArray[] = decifrado.toCharArray();

			// Iterator dos pares formados pela chave
			Iterator<Pair> iterator = cifra.getChave().iterator();
			// Pego o primeiro par
			Pair pair = iterator.next();
			// Se imaginarmos o texto decifrado em uma matriz, index representa uma coluna.
			// Index do primeiro par
			int index = pair.getValue();

			// Percorro todo o texto cifrado, caracter por caracter
			for (int j = 0; j < decifrado.length(); j++) {
				/**
				 * Se o m�dulo da posi��o em que estou no texto cifrado (j) com o n�mero de
				 * linhas da matriz imagin�ria for zero significa que cheguei ao final da linha
				 * da matriz. Ent�o atribuo a pair a pr�xima coluna da matriz e atribuo a index
				 * o seu valor.
				 */
				if (j >= linhas && (j % linhas) == 0) {
					pair = iterator.next();
					index = pair.getValue();
				}

				// Populo o array que guarda o texto decifrado
				decifradoArray[index] = textoCifradoArray[j];
				// Somo o tamanho da chave ao index pra pular pra pr�xima linha da matriz
				// imagin�ria mas continuando na mesma coluna
				index += chaveLenght;
			}

			// Guardando texto decifrado
			decifrado = new String(decifradoArray);
		}
		
		cifra.setTextoDecifrado(decifrado);
	}

	/**
	 * Salva em arquivo o texto cifrado
	 * 
	 * @throws FileNotFoundException
	 */
	public void salvarCifrado() throws FileNotFoundException {
		String filename = "Trabalho Indiv. 1 - " + cifra.getFilename() + " cifrado.txt";
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
		String filename = "Trabalho Indiv. 1 - " + cifra.getFilename() + " decifrado.txt";
		PrintWriter out = null;
		out = new PrintWriter(new FileOutputStream(cifra.getDiretorio() + File.separator + filename));
		out.println(cifra.getTextoDecifrado());
		if (out != null) {
			out.flush();
			out.close();
		}
	}

	/**
	 * L� de arquivo o texto claro a ser cifrado
	 * 
	 * @param path Caminho do arquivo
	 */
	public void carregaTextoClaro(String path) {
		Scanner scanner = null;
		try {
			scanner = new Scanner(new File(path), "UTF-8");
			// Usa a express�o regular \A como delimitador
			// Significa que o texto no arquivo ser� delimitado pelo seu come�o
			// e vai tornar o texto inteiro do texto uma s� string
			cifra.setTextoClaro(scanner.useDelimiter("\\A").next());
		} catch (FileNotFoundException e) {
			e.printStackTrace();
		} finally {
			if (scanner != null)
				scanner.close();
		}
	}

	/**
	 * Cria lista de pares usando chave fornecida pelo usu�rio.
	 * 
	 * @param chave
	 */
	public void setChave(String chave) {
		// Lista de pares
		ArrayList<Pair> pair = new ArrayList<Pair>();

		// Converte chave em array de char
		char chaveArray[] = chave.toCharArray();

		// Salva em uma lista de Pair.
		// Cada letra da chave � uma key, a posi��o da letra na string � o value
		for (int i = 0; i < chaveArray.length; i++) {
			pair.add(new Pair(chaveArray[i], i));
		}

		// Ordena de forma crescente (alfab�tica) as chaves
		pair.sort(new Pair());

		cifra.setChave(pair);
	}

	public void reset() {
		cifra = new Cifra();
	}

	public Cifra getCifra() {
		return cifra;
	}
}
