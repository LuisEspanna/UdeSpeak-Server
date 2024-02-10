# syntax=docker/dockerfile:1

FROM ubuntu:20.04
WORKDIR /home/app
COPY . /home/app
RUN apt-get -y update
RUN apt-get -y upgrade
RUN apt-get install -y ffmpeg
#
RUN apt-get install -y software-properties-common
RUN add-apt-repository -y ppa:deadsnakes/ppa
# Install py39 from deadsnakes repository
RUN apt-get install -y python3.9
# Install pip from standard ubuntu packages
RUN apt-get install -y python3-pip
#
RUN apt-get install -y git-core
RUN python3.9 -m pip install Flask
RUN python3.9 -m pip install -U flask-cors
RUN python3.9 -m pip install gTTS
RUN python3.9 -m pip install -U openai-whisper
RUN python3.9 -m pip install --upgrade --no-deps --force-reinstall git+https://github.com/openai/whisper.git
RUN python3.9 -m pip install setuptools-rust
RUN python3.9 -m pip install pydub
RUN python3.9 -m pip install ipython
RUN python3.9 -m pip install tensorflow
RUN python3.9 -m pip install tensorflow-io
RUN python3.9 -m pip install librosa
RUN python3.9 -m pip install matplotlib
CMD ["flask", "run", "--host=0.0.0.0"]
EXPOSE 5000