# The_maze
Jogo "The Maze", criado inicialmente para a disciplina de POO2

para criação foi utilizado a biblioteca pygame versão 1.9.1
link para download: http://www.pygame.org/download.shtml

para windows a biblioteca possui versão para o python 3.1 32 bits
para Mac O.S somente na versão python 2.7 32 bits

como o jogo foi desenvolvido em um ambiente windows não se sabe se
ocorrerá algum erro quanto a incompatibilidade das versões do python
(3.1 para 2.7)

link python 3.1: https://www.python.org/download/releases/3.1.4/
link python 2.7: https://www.python.org/downloads/release/python-279/

(VERSÃO 32 BITS)

depois de instalado basta configurar as variaveis de ambiente do
sistema (se já houver alguma versão do python instalada, renomeie o
arquivo python.exe baixado, ex.. python31.exe)
e chamar o programa principal (main.py) pelo launcher do python baixado
para facilitar o uso é aconselhado a criação de um shell script para
abertura do programa

Instalar Pygame no linux

sudo apt-get install mercurial python3-dev libjpeg-dev libpng12-dev libportmidi-dev libsdl-image1.2-dev libsdl-mixer1.2-dev libsdl-ttf2.0-dev libsdl1.2-dev libsmpeg-dev libx11-dev ttf-freefont libavformat-dev libswscale-dev
hg clone -u 01b2cb16dc17 https://bitbucket.org/pygame/pygame
cd pygame
python3 config.py
2to3 setup.py -w
python3 setup.py build
sudo python3 setup.py install

Pronto :3
