# Pasos para configurar el entorno virtual Python



### Instalar python 3.9 Windows 
https://www.python.org/ftp/python/3.9.9/python-3.9.9-amd64.exe

### Instalar python en Linux:
```bash
sudo apt install build-essential checkinstall 

sudo apt install libreadline-gplv2-dev libncursesw5-dev libssl-dev \
    libsqlite3-dev tk-dev libgdbm-dev libc6-dev libbz2-dev libffi-dev zlib1g-dev

cd /opt

sudo wget https://www.python.org/ftp/python/3.9.16/Python-3.9.16.tgz

sudo tar xzf Python-3.9.16.tgz

cd Python-3.9.16

sudo ./configure --enable-optimizations

sudo make altinstall

python3.9 -V
```

## Instalar GIT linux
```bash
sudo apt-get install git-core
```

## Crear el entorno virtual Python
```bash
cd udespeak-server
python -m venv .venv
```

## Activar el entorno virtual Python
```bash
# Windows
.venv\Scripts\activate

# Linux
source .venv/bin/activate
```

## Desactivar el entorno virtual Python
```bash
deactivate
```

## Instalar Whisper

Whisper sirve para transformar un audio a texto, modelo creado por OpenIA.

```bash
python3.9 -m pip install --upgrade pip

pip install -U openai-whisper

pip install git+https://github.com/openai/whisper.git

pip install --upgrade --no-deps --force-reinstall git+https://github.com/openai/whisper.git

# Linux
sudo apt update && sudo apt install ffmpeg

# Windows
choco install ffmpeg

pip install setuptools-rust
```

## Instalar gTTS
```bash
pip install gTTS
```

## Instalar Flask
```bash
pip install Flask
```

## Iniciar el servidor 
```bash
flask --app main.py run
```

## Guardar las librerías usadas para crear requirements.txt
```bash
pip3 freeze > requirements.txt
```

# DOCKER

## Crear la imagen
```bash
docker build -t flaskapi:latest .
```

## Crear un contenedor
```bash
docker create --gpus all -p5000:5000 --name udespeak flaskapi
```

## Listar los contenedores creados
```bash
docker ps -a
```

## Ejecutar el contenedor creado
```bash
docker start udespeak
```

## Ver los logs del servidor
```bash
docker logs --follow udespeak
```

## Parar el servidor
```bash
docker stop udespeak
```