package controller;

import java.io.File;
import java.io.FileNotFoundException;
import java.io.FileOutputStream;
import java.io.PrintWriter;
import java.util.ArrayList;
import java.util.HashMap;
import java.util.Iterator;
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

	public void cifrar() throws Exception {

		// Testa se o texto claro foi fornecido pelo usuário
		if (cifra.getTextoClaro().trim().isEmpty()) {
			throw new Exception("Texto Claro Não Foi Definido ou É Vazio");
		}

		// Testa se chave foi fornecida pelo usuário
		if (cifra.getChave().size() == 0) {
			throw new Exception("Chave Não Foi Informada");
		}

		String textoClaroHolder = cifra.getTextoClaro();
		// Tamanho da chave
		int chaveLenght = cifra.getChave().size();
		// Calcula quantos campos faltam no texto claro para completar a cifragem
		int camposRestantes = chaveLenght - (textoClaroHolder.length() % chaveLenght);

		for (int i = 0; i < camposRestantes; i++) {
			// Adiciona aos campos sem texto outras letras começando do "a" minúsculo
			// Código 97 em ASCII igual a letra "a"
			textoClaroHolder += (char) (97 + i);
		}

		// Número de linhas na 'matriz'
		int linhas = textoClaroHolder.length() / cifra.getChave().size();

		String cifrado; // Variável que vai guardar o texto decifrado em cada estágio

		// Três estágios de transposição
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
					index += chaveLenght; // Somando tamanho da chave para ir para o próximo caracter
				}
			}

			textoClaroHolder = cifrado;
		}

		cifra.setTextoCifrado(textoClaroHolder);
	}

	public void salvarCifrado() throws FileNotFoundException {
		String filename = cifra.getFilename() + " cifrado.txt";
		PrintWriter out = null;
		out = new PrintWriter(new FileOutputStream(cifra.getDiretorio() + "\\" + filename));
		out.println(cifra.getTextoCifrado());
		out.flush();
		out.close();
	}

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
		ArrayList<Pair> pair = new ArrayList<Pair>();

		// Converte chave em array de char
		char chaveArray[] = chave.toCharArray();

		// Salva em uma lista de Pair o index da coluna de cada caracter da chave
		for (int i = 0; i < chaveArray.length; i++) {
			pair.add(new Pair(chaveArray[i], i));
		}

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
