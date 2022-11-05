# rasp_DL


## 1) 프로젝트에 대한 소개

마스크 미착용자와 기침한 사람을 자동으로 판별해서 알람을 실시간 보내는 프로젝트

##### <프로그램 흐름도>

![2](https://user-images.githubusercontent.com/62248763/101849955-18af2300-3b9c-11eb-846b-7fcea3bc151f.JPG)

##### <windows server part / raspberry pi part>

1. pi/raspberry/file-server.py 를 실행시킬 때 포트를 지정하여 실행

라즈베리파이에 연결된 마이크 모듈에서 녹음한 음성부분을 socket 이용해서 전송하기 위한 코드

2. server/file-client.py를 실행 (이때 포트번호 지정과 라즈베리파이의 IP 주소 포함되어야 함) 

음성을 받기 위한 코드

3.	server/ftp-windows.py 실행

영상을 받기 위한 코드 (ftplib)

4.	pi/raspberry/app-cap.py 실행

영상을 캡처 및 보내기, 음성 캡처

5.	server/covid19.py 실행

프로젝트의 주 웹서버 코드


## 2) Reference

#### 데이터
- https://research.google.com/audioset/
- https://freesound.org/
- https://catalog.ldc.upenn.edu/LDC93S1
- https://urbansounddataset.weebly.com/
- https://urbansounddataset.weebly.com/urbansound8k.html

#### 참조 프로젝트
- 소리 특징 추출과 분류

https://github.com/mikesmales/Udacity-ML-Capstone

- customized yolo weights 얻기

https://www.youtube.com/watch?v=10joRJt39Ns&t=1224s

https://www.youtube.com/watch?v=EGQyDla8JNU

- 라즈베리파이 카메라 캡처

https://github.com/miguelgrinberg/flask-video-streaming


## 3) License

MIT License
