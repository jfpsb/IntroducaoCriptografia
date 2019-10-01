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

		// Neste método não é utilizada uma matriz, mas sim um vetor, entretanto será
		// usada a expressão 'matriz imaginária'

		// Testa se o texto claro foi fornecido pelo usuário
		if (cifra.getTextoClaro().trim().isEmpty()) {
			throw new Exception("Texto Claro Não Foi Definido ou É Vazio");
		}

		// Testa se chave foi fornecida pelo usuário
		if (cifra.getChave().size() == 0) {
			throw new Exception("Chave Não Foi Informada");
		}

		String textoClaroHolder = cifra.getTextoClaro();
		// Tamanho da chave, representa a quantidade de colunas na matriz imaginária
		int chaveLenght = cifra.getChave().size();
		// Calcula quantos campos estão vazios na última linha da matriz imaginária, se
		// houver algum
		int camposVazios = 0;
		if ((textoClaroHolder.length() % chaveLenght) != 0) // Se módulo for zero não há campos em branco
			camposVazios = chaveLenght - (textoClaroHolder.length() % chaveLenght);

		// Para cada campo sem letra na última linha da matriz imaginária
		for (int i = 0; i < camposVazios; i++) {
			// Adiciona aos campos sem texto outras letras começando do "a" minúsculo
			// Código 97 em ASCII igual a letra "a"
			textoClaroHolder += (char) (97 + i);
		}

		// Número de linhas na matriz imaginária
		int linhas = textoClaroHolder.length() / cifra.getChave().size();

		// Variável que vai guardar o texto decifrado em cada estágio
		String cifrado;

		// Três estágios de transposição
		for (int p = 0; p < 3; p++) {
			// Converte texto claro em array de char
			char textoClaroChar[] = textoClaroHolder.toCharArray();

			// Guarda os caracteres do texto cifrado um por um até o final do estágio
			cifrado = "";

			Iterator<Pair> iterator = cifra.getChave().iterator();

			// Itera pelos caracteres da chave em ordem alfabética crescente (previamente
			// ordenada)
			while (iterator.hasNext()) {
				Pair pair = iterator.next();

				// Coluna atribuída à letra do pair atual
				int colunaAtual = pair.getValue();

				// Para cada linha da matriz imaginária, insiro uma letra da coluna atual em
				// cifrado
				for (int j = 0; j < linhas; j++) {
					// Coloco em cifrado os caracteres da coluna da matriz imaginária
					cifrado += textoClaroChar[colunaAtual];
					// Somo o tamanho da chave à coluna atual pra pular pra próxima linha da matriz
					// imaginária mas continuando na mesma coluna
					colunaAtual += chaveLenght;
				}
			}

			// A cada estágio de cifragem o texto cifrado fica salvo em textoClaroHolder
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
		// Número de linhas na matriz imaginária
		int linhas = cifra.getTextoCifrado().length() / cifra.getChave().size();

		// Onde texto decifrado vai ficar guardado em cada estágio.
		// No início guardo o texto cifrado nesta variável
		String decifrado = cifra.getTextoCifrado();

		// Decifragem em 3 estágios
		for (int i = 0; i < 3; i++) {
			// A variável "decifrado" vai de fato guardar o texto cifrado até o término da
			// execução do último estágio da decifragem. Após isso nela estará o texto
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
				 * Se o módulo da posição em que estou no texto cifrado (j) com o número de
				 * linhas da matriz imaginária for zero significa que cheguei ao final da linha
				 * da matriz. Então atribuo a pair a próxima coluna da matriz e atribuo a index
				 * o seu valor.
				 */
				if (j >= linhas && (j % linhas) == 0) {
					pair = iterator.next();
					index = pair.getValue();
				}

				// Populo o array que guarda o texto decifrado
				decifradoArray[index] = textoCifradoArray[j];
				// Somo o tamanho da chave ao index pra pular pra próxima linha da matriz
				// imaginária mas continuando na mesma coluna
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
	 * Lê de arquivo o texto claro a ser cifrado
	 * 
	 * @param path Caminho do arquivo
	 */
	public void carregaTextoClaro(String path) {
		Scanner scanner = null;
		try {
			scanner = new Scanner(new File(path));
			// Usa a expressão regular \A como delimitador
			// Significa que o texto no arquivo será delimitado pelo seu começo
			// e vai tornar o texto inteiro do texto uma só string
			cifra.setTextoClaro(scanner.useDelimiter("\\A").next().toLowerCase());
		} catch (FileNotFoundException e) {
			e.printStackTrace();
		} finally {
			if (scanner != null)
				scanner.close();
		}
	}

	/**
	 * Cria lista de pares usando chave fornecida pelo usuário.
	 * 
	 * @param chave
	 */
	public void setChave(String chave) {
		// Lista de pares
		ArrayList<Pair> pairs = new ArrayList<Pair>();

		// Converte chave em array de char
		char chaveArray[] = chave.toCharArray();

		// Salva em uma lista de Pair.
		// Cada letra da chave é uma key, a posição da letra na string é o value
		for (int i = 0; i < chaveArray.length; i++) {
			pairs.add(new Pair(chaveArray[i], i));
		}

		// Ordena de forma crescente (alfabética) as chaves
		pairs.sort(new Pair());

		cifra.setChave(pairs);
	}

	/**
	 * Reseta o modelo para uma nova execução
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
