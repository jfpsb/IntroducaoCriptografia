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

/**
 * Controller para TelaInicial
 * 
 * @author jfpsb
 *
 */
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

		// Neste m�todo n�o � utilizada uma matriz, mas sim um vetor, entretanto ser�
		// usada a express�o 'matriz imagin�ria'

		// Testa se o texto claro foi fornecido pelo usu�rio
		if (cifra.getTextoClaro().trim().isEmpty()) {
			throw new Exception("Texto Claro N�o Foi Definido ou � Vazio");
		}

		// Testa se chave foi fornecida pelo usu�rio
		if (cifra.getChave().size() == 0) {
			throw new Exception("Chave N�o Foi Informada");
		}

		String textoClaroHolder = cifra.getTextoClaro();
		// Tamanho da chave, representa a quantidade de colunas na matriz imagin�ria
		int chaveLenght = cifra.getChave().size();
		// Calcula quantos campos est�o vazios na �ltima linha da matriz imagin�ria, se
		// houver algum
		int camposVazios = 0;
		if ((textoClaroHolder.length() % chaveLenght) != 0) // Se m�dulo for zero n�o h� campos em branco
			camposVazios = chaveLenght - (textoClaroHolder.length() % chaveLenght);

		// Para cada campo sem letra na �ltima linha da matriz imagin�ria
		for (int i = 0; i < camposVazios; i++) {
			// Adiciona aos campos sem texto outras letras come�ando do "a" min�sculo
			// C�digo 97 em ASCII igual a letra "a"
			textoClaroHolder += (char) (97 + i);
		}

		// N�mero de linhas na matriz imagin�ria
		int linhas = textoClaroHolder.length() / cifra.getChave().size();

		// Vari�vel que vai guardar o texto decifrado em cada est�gio
		String cifrado;

		// Tr�s est�gios de transposi��o
		for (int p = 0; p < 3; p++) {
			// Converte texto claro em array de char
			char textoClaroChar[] = textoClaroHolder.toCharArray();

			// Guarda os caracteres do texto cifrado um por um at� o final do est�gio
			cifrado = "";

			Iterator<Pair> iterator = cifra.getChave().iterator();

			// Itera pelos caracteres da chave em ordem alfab�tica crescente (previamente
			// ordenada)
			while (iterator.hasNext()) {
				Pair pair = iterator.next();

				// Coluna atribu�da � letra do pair atual
				int colunaAtual = pair.getValue();

				// Para cada linha da matriz imagin�ria, insiro uma letra da coluna atual em
				// cifrado
				for (int j = 0; j < linhas; j++) {
					// Coloco em cifrado os caracteres da coluna da matriz imagin�ria
					cifrado += textoClaroChar[colunaAtual];
					// Somo o tamanho da chave � coluna atual pra pular pra pr�xima linha da matriz
					// imagin�ria mas continuando na mesma coluna
					colunaAtual += chaveLenght;
				}
			}

			// A cada est�gio de cifragem o texto cifrado fica salvo em textoClaroHolder
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
		// N�mero de linhas na matriz imagin�ria
		int linhas = cifra.getTextoCifrado().length() / cifra.getChave().size();

		// Onde texto decifrado vai ficar guardado em cada est�gio.
		// No in�cio guardo o texto cifrado nesta vari�vel
		String decifrado = cifra.getTextoCifrado();

		// Decifragem em 3 est�gios
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
				/*
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
			scanner = new Scanner(new File(path));
			// Usa a express�o regular \A como delimitador
			// Significa que o texto no arquivo ser� delimitado pelo seu come�o
			// e vai tornar o texto inteiro do texto uma s� string
			cifra.setTextoClaro(scanner.useDelimiter("\\A").next().toLowerCase());
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
		ArrayList<Pair> pairs = new ArrayList<Pair>();

		// Converte chave em array de char
		char chaveArray[] = chave.toCharArray();

		// Salva em uma lista de Pair.
		// Cada letra da chave � uma key, a posi��o da letra na string � o value
		for (int i = 0; i < chaveArray.length; i++) {
			pairs.add(new Pair(chaveArray[i], i));
		}

		// Ordena de forma crescente (alfab�tica) as chaves
		pairs.sort(new Pair());

		cifra.setChave(pairs);
	}

	/**
	 * Reseta o modelo para uma nova execu��o
	 */
	public void reset() {
		cifra = new Cifra();
	}

	/**
	 * Retorna cifra para acesso na view
	 * 
	 * @return Cifra
	 */
	public Cifra getCifra() {
		return cifra;
	}
}
