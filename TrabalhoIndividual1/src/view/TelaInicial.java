package view;

import java.awt.BorderLayout;
import java.awt.Dimension;
import java.awt.FlowLayout;
import java.awt.Font;
import java.awt.GridLayout;
import java.awt.Toolkit;
import java.awt.event.ActionEvent;
import java.awt.event.ActionListener;
import java.awt.event.KeyAdapter;
import java.awt.event.KeyEvent;
import java.io.File;
import java.io.FileFilter;
import java.nio.file.DirectoryStream.Filter;
import java.util.Arrays;

import javax.swing.JButton;
import javax.swing.JFileChooser;
import javax.swing.JFrame;
import javax.swing.JLabel;
import javax.swing.JPanel;
import javax.swing.JTextField;
import javax.swing.SwingConstants;
import javax.swing.filechooser.FileNameExtensionFilter;

public class TelaInicial extends JFrame {

	private static final int width = 600; // Largura da tela
	private static final int height = 130; // Altura da tela

	// Labels
	private JLabel lblChave;
	private JLabel lblAbrirArquivo;

	// Panels
	private JPanel wrapperPanel; // Panel do Jframe
	private JPanel camposPanel; // Panel com o campo de chave e bot�o para abrir arquivo com texto claro
	private JPanel botaoPanel; // Panel com o bot�o de cifrar

	// Bot�es
	private JButton btnCifrar;
	private JButton btnAbrirArquivo;

	// Campo de texto
	private JTextField txtChave;

	// Selecionador de arquivo
	private JFileChooser chooser;

	public TelaInicial() {
		// Configura��es do formul�rio
		super("Atividade Individual 1");

		setDefaultCloseOperation(EXIT_ON_CLOSE); // Encerra aplica��o ao fechar tela
		setSize(width, height); // Configura tamanho da tela
		setMinimumSize(getSize()); // Configura tamanho m�nimo da tela igual ao tamanho inicial

		// Configura para que tela abra no centro da tela
		Dimension screenSize = Toolkit.getDefaultToolkit().getScreenSize(); // Pega as dimens�es do monitor
		int x = (screenSize.width - width) / 2; // Calcula coordenada x para que tela fique centrada horizontalmente
		int y = (screenSize.height - height) / 2; // Calculada coordenada y para que tela fique centra verticalmente
		setLocation(x, y);

		// Inicializando componentes de interface
		lblAbrirArquivo = new JLabel("Selecione o Arquivo");
		lblChave = new JLabel("Chave:");

		wrapperPanel = new JPanel();
		camposPanel = new JPanel();
		botaoPanel = new JPanel();

		btnCifrar = new JButton("Cifrar");
		btnAbrirArquivo = new JButton("Abrir Arquivo");

		txtChave = new JTextField();

		chooser = new JFileChooser();

		// Configurando atributos de componentes
		lblAbrirArquivo.setHorizontalAlignment(SwingConstants.CENTER); // Centra texto horizontalmente
		lblChave.setHorizontalAlignment(SwingConstants.CENTER); // Centra texto horizontalmente

		// Configura o panel principal com um BorderLayout
		wrapperPanel.setLayout(new BorderLayout());
		// Configura com GridLayout panel que conter� o campo de chave e bot�o de abrir
		// arquivo
		// Duas colunas, duas linhas. Espa�amento de 2 entre cada linha e coluna
		camposPanel.setLayout(new GridLayout(2, 2, 2, 2));
		// Panel que conter� o bot�o configurado com FlowLayout
		botaoPanel.setLayout(new FlowLayout());

		// Configura tamanho de letra de bot�o de cifrar
		btnCifrar.setFont(new Font("Arial", Font.BOLD, 18));
		
		btnCifrar.addActionListener(new ActionListener() {
			@Override
			public void actionPerformed(ActionEvent e) {
				char c[] = txtChave.getText().toCharArray();
				Arrays.sort(c);
				System.out.println(new String(c));
			}
		});

		// Configura evento de clique do bot�o de abrir selecionador de arquivo
		btnAbrirArquivo.addActionListener(new ActionListener() {
			@Override
			public void actionPerformed(ActionEvent e) {
				int result = chooser.showOpenDialog(wrapperPanel);

				if (result == JFileChooser.APPROVE_OPTION) {
					// Coloca caminho do arquivo escolhido na label de arquivo
					lblAbrirArquivo.setText(chooser.getSelectedFile().getAbsolutePath());
					char c[] = txtChave.getText().toCharArray();
					Arrays.sort(c);
					System.out.println(new String(c));
				}
			}
		});

		// Limita tamanho da chave a 7 caracteres
		txtChave.addKeyListener(new KeyAdapter() {
			public void keyTyped(KeyEvent e) {
				if (txtChave.getText().length() >= 7)
					e.consume();
			}
		});

		// Configura pasta inicial do selecionador de arquivo
		chooser.setCurrentDirectory(new File(System.getProperty("user.home")));
		// Configura filtro para arquivos txt
		FileNameExtensionFilter filtro = new FileNameExtensionFilter("Arquivo de Texto (*.txt)", "txt");
		chooser.addChoosableFileFilter(filtro);
		// Configura que somente a extens�o txt estar� dispon�vel ao escolher arquivos
		chooser.setAcceptAllFileFilterUsed(false);

		// Adicionando componentes aos panels
		camposPanel.add(lblChave);
		camposPanel.add(txtChave);
		camposPanel.add(lblAbrirArquivo);
		camposPanel.add(btnAbrirArquivo);
		botaoPanel.add(btnCifrar);

		// Adicionando panels ao panel principal
		wrapperPanel.add(camposPanel, BorderLayout.CENTER); // Panel com campo e bot�o de arquivo no centro do
															// formul�rio
		wrapperPanel.add(btnCifrar, BorderLayout.SOUTH); // Bot�o de cifrar na borda sul do formul�rio

		// Adicionando o panel principal ao formul�rio
		add(wrapperPanel);
	}
}
