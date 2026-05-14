# 🎮 Party Invite Automation

Projeto de automação desenvolvido em **Python** como primeiro contato com bibliotecas externas. O programa abre um jogo por comando de voz e envia automaticamente convites para amigos via **WhatsApp Desktop**.

---

## 📋 Descrição

Com apenas a sua voz, o programa identifica qual jogo você quer jogar, abre ele no computador e envia uma mensagem de convite para o amigo escolhido no WhatsApp — tudo de forma automática.

---

## 🎮 Funcionalidades

- 🎙️ **Reconhecimento de voz** para identificar o jogo desejado
- 🖥️ **Abertura automática do jogo** via menu Iniciar do Windows
- 💬 **Envio de convite** para amigos pelo WhatsApp Desktop
- 🔁 **Loop contínuo** que limpa o terminal a cada nova rodada

---

## 🛠️ Tecnologias e Bibliotecas

| Biblioteca | Uso |
|---|---|
| `pyautogui` | Automação de teclado e mouse |
| `pyperclip` | Copiar e colar texto via clipboard |
| `speech_recognition` | Reconhecimento de voz |
| `time` | Controle de delays entre ações |
| `os` | Limpeza do terminal |

---

## 🚀 Como Instalar e Executar

### Pré-requisitos

- Python 3.x instalado
- WhatsApp Desktop instalado e logado

### Instalação das dependências

```bash
pip install pyautogui pyperclip SpeechRecognition
```

> O `speech_recognition` também pode exigir o **PyAudio**:
> ```bash
> pip install pyaudio
> ```

### Execução

```bash
python party_automation.py
```

---

## 🕹️ Como Usar

1. Execute o programa
2. **Fale o nome do jogo** que deseja jogar — o programa abrirá automaticamente
3. **Digite o nome do amigo** que deseja convidar
4. O programa abre o WhatsApp, busca o contato e envia a mensagem **"Let's play"**
5. O loop reinicia para uma nova rodada

---

## ⚠️ Observações

- O projeto foi desenvolvido e testado no **Windows**
- As coordenadas de clique (`x`, `y`) no `pyautogui` são fixas e podem precisar de ajuste conforme a resolução do seu monitor
- É necessário ter o **WhatsApp Desktop** aberto para o funcionamento correto

---

## 📁 Estrutura do Projeto

```
party-automation/
├── party_automation.py  # Código-fonte principal
└── README.md            # Documentação do projeto
```

---

## 👨‍🎓 Contexto

Primeiro projeto pessoal utilizando bibliotecas externas em Python, com foco em automação de tarefas do dia a dia usando reconhecimento de voz e controle de interface gráfica.
