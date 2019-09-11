package view;

import java.awt.BorderLayout;
import java.awt.Dimension;
import java.awt.FlowLayout;
import java.awt.GridLayout;
import java.awt.Toolkit;
import java.awt.event.KeyAdapter;
import java.awt.event.KeyEvent;

import javax.swing.Box;
import javax.swing.BoxLayout;
import javax.swing.JButton;
import javax.swing.JFrame;
import javax.swing.JLabel;
import javax.swing.JPanel;
import javax.swing.JTextField;

public class TelaInicial extends JFrame {
	/**
	 * 
	 */
	private static final long serialVersionUID = 1L;
	private static final int width = 600;
	private static final int height = 130;

	private JPanel wrapperPanel; // Panel do Jframe
	private JPanel camposPanel; // Panel com os campos
	private JPanel botaoPanel; // Panel com o botão de cifrar

	private JButton btnCifrar;
	private JButton btnAbrirArquivo;

	private JLabel lblChave;
	private JLabel lblAbrirArquivo;

	private JTextField txtChave;

	public TelaInicial() {
		super("Atividade Individual 1");

		setDefaultCloseOperation(EXIT_ON_CLOSE);
		setSize(width, height);
		setMinimumSize(getSize());

		// Tela abre centrada
		Dimension screenSize = Toolkit.getDefaultToolkit().getScreenSize();
		int x = (screenSize.width - width) / 2;
		int y = (screenSize.height - height) / 2;
		setLocation(x, y);

		wrapperPanel = new JPanel();
		camposPanel = new JPanel();
		botaoPanel = new JPanel();

		lblAbrirArquivo = new JLabel("Selecione o Arquivo");
		lblChave = new JLabel("Chave: ");

		txtChave = new JTextField();
		// Limita tamanho da chave a 7 caracteres
		txtChave.addKeyListener(new KeyAdapter() {
			public void keyTyped(KeyEvent e) {
				if (txtChave.getText().length() >= 7)
					e.consume();
			}
		});

		wrapperPanel.setLayout(new BorderLayout());
		camposPanel.setLayout(new GridLayout(2, 2, 2, 2));
		botaoPanel.setLayout(new FlowLayout());

		btnCifrar = new JButton("Cifrar");
		btnAbrirArquivo = new JButton("Abrir Arquivo");

		camposPanel.add(lblChave);
		camposPanel.add(txtChave);
		camposPanel.add(lblAbrirArquivo);
		camposPanel.add(btnAbrirArquivo);
		botaoPanel.add(btnCifrar);

		wrapperPanel.add(camposPanel, BorderLayout.CENTER);
		wrapperPanel.add(btnCifrar, BorderLayout.SOUTH);

		add(wrapperPanel);
	}
}
