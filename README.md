# Controle de Veículos com Microcontroladores

Este repositório contém projetos de controle e automação de veículos usando microcontroladores, incluindo implementação em **C/C++** e **Python (MicroPython)**. O foco principal é criar um carro seguidor de linha e um carro controlado remotamente via Wi-Fi.

---

## 📁 Estrutura do Repositório

- **`main.cpp`**: Código em C++ para um carro seguidor de linha utilizando sensores e servos.
- **`main.py`**: Controle de um carro via Wi-Fi usando MicroPython. Inclui interface HTML para comandos remotos.

---

## 🔧 Requisitos

### Hardware
- Microcontrolador (ex: Arduino, ESP32, ou ESP8266)
- Sensores (ex: sensores de linha IR para o seguidor de linha)
- Servos ou motores com driver PWM
- Módulo Wi-Fi (para controle remoto via MicroPython)

### Software
- Arduino IDE (para C++)
- MicroPython e ferramentas associadas (ex: Thonny)
- Dependências específicas para cada projeto:
  - `Servo.h` para projetos em C++ com Arduino
  - `MicroPyServer` para MicroPython

---

## 🚀 Guia de Uso

### Seguidor de Linha (C++)
1. Conecte os sensores e os servos ao microcontrolador conforme o esquema de hardware.
2. Carregue o arquivo `main.cpp` no microcontrolador usando o **Arduino IDE**.
3. Ajuste o valor do limiar (`LIMIAR_LINHA`) para calibrar os sensores de linha.
4. Execute e observe o veículo seguir a linha com base nos valores dos sensores.

### Controle via Wi-Fi (MicroPython)
1. Configure os pinos do motor no arquivo `main.py`.
2. Substitua `SSID` e `PASSWORD` pelas credenciais da sua rede Wi-Fi.
3. Carregue o código no microcontrolador com suporte a Wi-Fi (ex: ESP32).
4. Após conexão, acesse a interface no navegador utilizando o IP exibido no terminal.
5. Use os botões na interface para controlar o veículo remotamente.

---

## ⚙️ Arquivos Importantes

1. **`main.cpp`**
   - Utiliza a biblioteca `Servo.h` para controle dos servos.
   - Foco em responsividade sem atrasos para maior velocidade.

2. **`main.py`**
   - Controle remoto via interface web.
   - Implementado com MicroPython, inclui:
     - Conexão Wi-Fi.
     - Interface HTML para controle.
     - Geração de PWM para motores.

---

## 📷 Esquema de Conexões

### Seguidor de Linha
- **Motores/Servos:**
  - Servo esquerdo: Pino 5
  - Servo direito: Pino 6
- **Sensores IR:**
  - Sensor esquerdo: Pino A5
  - Sensor direito: Pino A4

### Controle via Wi-Fi
- **Motores:**
  - Motores conectados aos pinos configurados em `main.py` (ex: 2, 15, 16).
- **Módulo Wi-Fi:**
  - Configuração automática para a rede local com SSID e senha.

---