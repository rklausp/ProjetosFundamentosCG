1. GLSL é a linguagem de Shading do OpenGL, baseada em C, é utilizada para auxiliar na manipulação da pipeline de gráficos. Os dois tipos de shader obrigatórios no pipeline programável da versão atual são o vertex shader e o fragment shader. O primeiro é responsável por processar vértices individuais (coordenadas 3d) e seus atributos. O segundo, processa dados relacionados a cor e textura.

2. As primitivas são os comandos e pedidos que fazemos ao OpenGl para que ele saiba como montar aquilo que desejamos. Essas primitivas são processadas pelos shaders (mencionados na questão 1) para assim dar vida a essas imagens que programamos via OpenGl.

3. VBO → Vertex Buffer Objects: buffer é uma região de memória que serve para armazenar dados temporariamente, no caso aqui, estamos falando de uma maneira de enviar os dados acerca do vértice para CPU, alocando-os diretamente na memória da GPU, agilizando a renderização de objetos pela placa gráfica.
VAO → Vertex Array Object: armazena ponteiros que são responsáveis por fazer a ligação aos atributos de um vértice guardado de um VBO, pode-se ter mais de um VAO, e cada VAO pode guardar mais de um atributo dos vértices.
EBO → Element Buffer Objects: está armazendo dentro do VAO e é utilizado para associar a ideia de índices e evitar a especificação de vértices replicados no VBO.

5. Para fazer o triângulo foram adicionados os vértices novos e aumentado o número de vértices em glDrawArrays
![Print de execucao da atividade](/prints/print1.png)
![Print de execucao da atividade](/prints/print2.png)


Na a, para deixar apenas o polígono preenchido foram zerados os valores das variáveis de ponto e linha.
![Print de execucao da atividade](/prints/print3.png)
![Print de execucao da atividade](/prints/print4.png)

Na B, foi trocado GL_TRIANGLES por GL_LINE_LOOP.
![Print de execucao da atividade](/prints/print5.png)
![Print de execucao da atividade](/prints/print6.png)

Da mesma maneira, na C para deixar apenas os pontos se utiliza GL_POINTS.
![Print de execucao da atividade](/prints/print7.png)
![Print de execucao da atividade](/prints/print8.png)


No final, para todos foram chamadas todas as chamadas. 
![Print de execucao da atividade](/prints/print9.png)
![Print de execucao da atividade](/prints/print10.png)



6 - e - Pacman
![Print de execucao da atividade](/prints/print11.png)
![Print de execucao da atividade](/prints/print12.png)
![Print de execucao da atividade](/prints/print13.png)



Para transformar o pacman em círculo é só mudar de 0, nVertices para:
![Print de execucao da atividade](/prints/print14.png)
![Print de execucao da atividade](/prints/print15.png)


Para fazer o octógono é só mudar o número de pontos para 2
![Print de execucao da atividade](/prints/print16.png)
![Print de execucao da atividade](/prints/print17.png)


Para fazer pentágono, o número de pontos é 5.
![Print de execucao da atividade](/prints/print18.png)
![Print de execucao da atividade](/prints/print19.png)


d- Para fatia de pizza primeiro voltamos o glDArrays para como estava antes como Pacman
![Print de execucao da atividade](/prints/print20.png)
E mudar o slice.
![Print de execucao da atividade](/prints/print21.png)



7 - Para fazer a espiral, aumentou-se o número de vértices, colocou-se o raio inicial em 0, e no loop do círculo, adicionou-se um incremento de raio a cada iteração.
![Print de execucao da atividade](/prints/print22.png)
![Print de execucao da atividade](/prints/print23.png)
![Print de execucao da atividade](/prints/print24.png)


8 - a- Nesse caso o VBO armazenaria a posição e cor dos vértices, ou seja seus elementos.O VAO armazenaria as configurações dos VBOs e EBOs, sendo este o que associa as informações de vértices a índices, evitando especificações de vértices replicadas, logo, organizando as informações de cada vértice. O EBO pode ser utilizado para economizar e retulizar vértices, tornando o processo mais ágil.

b - O VBO se nota através da parte em que se passa variável dos vértices e a variável para troca de cor RGB. A parte que envolve o VAO tem seu próprio nome de atributo no código.
