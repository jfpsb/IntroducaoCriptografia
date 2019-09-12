package controller;

import java.io.File;
import java.io.FileNotFoundException;
import java.util.Arrays;
import java.util.HashMap;
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

	public Boolean cifrar() throws Exception {

		if (cifra.getTextoClaro().trim().isEmpty()) {
			throw new Exception("Texto Claro Não Foi Definido ou É Vazio");
		}

		if (cifra.getChaveMap().size() == 0) {
			throw new Exception("Chave Não Foi Informada");
		}

		cifra.cifrar();

		return true;
	}

	public void carregaTextoClaro(String path) {
		Scanner scanner = null;
		try {
			scanner = new Scanner(new File(path));
			cifra.setTextoClaro(scanner.useDelimiter("\\A").next());
			System.out.println(cifra.getTextoClaro());
		} catch (FileNotFoundException e) {
			e.printStackTrace();
		} finally {
			if (scanner != null)
				scanner.close();
		}
	}

	public void setChave(String chave) {
		cifra.setChave(chave);
		
		HashMap<Character, Integer> map = new HashMap<Character, Integer>();

		char chaveArray[] = chave.toCharArray();
		//Arrays.sort(chaveArray);

		for (int i = 0; i < chaveArray.length; i++) {
			map.put(chaveArray[i], i);
		}

		cifra.setChaveMap(map);
		
		System.out.println(map);
	}

	public Cifra getCifra() {
		return cifra;
	}

	public void setCifra(Cifra cifra) {
		this.cifra = cifra;
	}
}
