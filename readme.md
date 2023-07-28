``````
``````

<p align="center">
  <img src="https://scontent.fcgh23-1.fna.fbcdn.net/v/t1.15752-9/363814254_271743952142386_4616865015457596016_n.jpg?_nc_cat=111&ccb=1-7&_nc_sid=ae9488&_nc_eui2=AeFKLe5YJkj9LOopxq5Pfwnd-DxLAMtyztL4PEsAy3LO0snmpivCbEN3zQ6DR77e3TOVrSyiK2ZvWkP335LHC-Ev&_nc_ohc=4kezA76ySAsAX-emUEu&_nc_ht=scontent.fcgh23-1.fna&oh=03_AdS-dzsYqahoi23WZnPnJcMy4C3FoDYArptsaTNZWRnC2A&oe=64EAA564" width="300" /><br/>
Contador de pessoas na sala.<br/>
</p>

<br/>

## :pushpin: Descrição

​	O objetivo do nosso dispositivo é muito simples: contar a quantidade de pessoas na sala e exibir em um display. Para isto, fizemos uso de dois sensores, um infravermelho e outro ultrassônico, colocados um do lado do outro. O contador inicializa com o valor 0; se o alguém passar pelo dispositivo, os dois sensores vão detectar movimento. A questão é a ordem em que os dois dispositivos detectam o movimento: se o sensor ultrassônico detectar colisão antes do sensor infravermelho, significa que alguém entrou na sala e o contador é incrementado, sendo atualizado o valor mostrado no display; caso contrário, alguém saiu da sala e o contador é decrementado. Além disso, configuramos um chatbot no telegram, que envia a quantidade de pessoas como mensagem para um usuário.

<br/>

## :robot: Montagem do dispositivo físico

### Lista de materiais

| Quantidade | Nome                                                      | Link para referência                                         |
| ---------- | --------------------------------------------------------- | ------------------------------------------------------------ |
| 1          | ESP32 e cabo USB                                          | https://www.baudaeletronica.com.br/placa-doit-esp32-bluetooth-e-wifi.html |
| 1          | Arduíno UNO                                               | https://www.baudaeletronica.com.br/sensor-touch-capacitivo-ttp223b.html |
| 1          | Modulo Sensor de Distancia Ultrassónico, Chipsce, Hc-Sr04 | https://www.baudaeletronica.com.br/produto/sensor-de-distancia-ultrassonico-hc-sr04.html?utm_source=Site&utm_medium=GoogleMerchant&utm_campaign=GoogleMerchant&gclid=CjwKCAjwq4imBhBQEiwA9Nx1BsPHBXTAy0dByCAjPt1ZsFswPwMLqy45P2mwh-NSNcxOkmcSO3omuhoCjmAQAvD_BwE |
| 1          | Módulo Seguidor de Linha Senhor Óptico TCRT5000           | https://www.baudaeletronica.com.br/produto/modulo-seguidor-de-linha-sensor-optico-tcrt5000.html?utm_source=Site&utm_medium=GoogleMerchant&utm_campaign=GoogleMerchant&gclid=CjwKCAjwq4imBhBQEiwA9Nx1Bj1-7km8xuhM7fwu_9gBFN3RDbfIjgr95E3OQv9alaH0rY6zjh_OsRoCF3gQAvD_BwE |
| X          | Jumpers variados                                          | ---                                                          |
| 1          | Display LCD 16x2 (Azul) com Módulo Adaptador I2C          | https://www.baudaeletronica.com.br/produto/display-lcd-16x2-azul-com-modulo-adaptador-i2c.html?utm_source=Site&utm_medium=GoogleMerchant&utm_campaign=GoogleMerchant&gclid=CjwKCAjwq4imBhBQEiwA9Nx1BvZYqkmxKSxrsbKI3cJEgti6o5lCgIu5pdzjSne04MU8-wU4ewzjVhoC89QQAvD_BwE |

### Lista de conexões

| Componente                      | Pino da placa |
| ------------------------------- | ------------- |
| Sensor Ultrassônico (Trigger)   | 15            |
| Sensor Ultrassônico (Echo)      | 2             |
| Sensor Infravermelho            | 18            |
| Módulo i2c do Display LCD (scl) | 22            |
| Módulo i2c do Display LCD (sda) | 21            |


### Funcionamento dos sensores e atuadores

#### Modulo Sensor de Distancia Ultrassónico, Chipsce, Hc-Sr04

- O **Sensor de Distância Ultrassônico HC-SR04** possui função de medição sem contato de 2cm à 400cm, com precisão de aproximadamente 3mm. O módulo é composto por transmissor, receptor e circuito de controle.

  **PRINCÍPIO DE FUNCIONAMENTO**

  1 - Manter o IO trigger em nível lógico alto por no mínimo 10us, 
  2 - o módulo automatimente envia oito ciclos de uma freqüência de 40 kHz  e detecta se há um pulso de retorno.
  3 - Caso haja sinal de retorno, através de um sinal de nível alto, o tempo de duração deste sinal em nível alto representa a diferença de tempo entre o envio e o retorno.

  **PINAGEM**

  **- VCC** : Alimentação de +5V

  **- TRIG:** Entrada de Pulso

  **- ECHO**: Saída de pulso

  **- GND**: Terminal Terra


#### Módulo Seguidor de Linha Senhor Óptico TCRT5000

Esse módulo é baseado no sensor segue faixa inframervelho TCRT5000 que é composto por dois LEDs, um emissor e um receptor infravermelho. O Emissor emite a luz infravermelha, quando a luz não é refletida ou é refletida de volta, mas a intensidade não é suficientemente forte, o fototransistor não conduz (desligado), dessa forma, a saída do módulo é baixo. Se existir objetos na área de detecção, e a intensidade dos raios infravermelhos refletidos é forte o suficiente para saturar o fototransistor, a saída do módulo é alta. Essa placa será muito útil para confecção de pequenos circuitos em PCB, de forma simples e rápida.

Este Módulo Sensor Óptico conta ainda com um potenciômetro para ajuste da sensibilidade do sensor, o que facilita bastante a construção do protótipo ganhando-se tempo já que não há a necessidade de implementar este ajuste no software do microcontrolador.

Com esse tipo de sensor, podemos detectar se uma superfície é escura ou clara, já que superfícies escuras quase não refletem a luz e as claras refletem quase toda a luz incidente. Assim, pode ser usado em projetos de robótica para detecção de linhas e de obstáculos entre outras aplicações.


### Circuito

<p align="center">
Figura - Diagrama do circuito<br/>
  <img src="https://github.com/Anemaygi/SMAC/blob/master/src/circuitoa.png" width="400" /><br/>
</p>
## :electric_plug: Funcionamento do sistema

- Requisitos do código:
  - Bibliotecas hcsr04, machine, lcd_api e i2c_lcd para configurar o display e network para estabelecer conexão wi-fi.


## :busts_in_silhouette: Contribuir no projeto

### Features implementadas

- [x] Identificação de entrada ou saída de pessoas.


### Features para incrementar no projeto

- [ ] Tivemos uma limitação no projeto, que foi o sensor infravermelho utilizado. Por mais que o dispositivo funcione perfeitamente, o alcance é muito curto (menos de 10 cm). Se quiser incrementar nosso projeto, tente utilizar algum sensor infravermelho com alcance maior, para aumentar a funcionalidade do dispositivo.