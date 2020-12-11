# Growth05

## 1) 시연 영상 유튜브 주소

https://www.youtube.com/watch?v=ru0xJEwz4Uc&t=3s

## 2) 프로젝트에 대한 소개

감염병이 대유행하는 시대에 마스크 착용은 자신의 생명을 지키기 위해 당연히 착용해야하는 것이 되었으며, 조금이라도 누군가 기침을 하거나 발열과 같은 증상을 보이게 되면 의심을 하거나 불안하게 된다. 그러나 방역수칙을 준수하는 것이 그 어느때보다 중요한 시기에, 종종 버스나 지하철과 같은 대중교통을 탈 때 마스크를 착용하지 않는 이들을 보고 마스크를 쓰라고 요구하는 버스 기사나 승객을 폭행하는 사건을 볼 수 있었다. 그래서 우리 조는 공공장소에서 마스크를 착용하지 않는 사람들을 실시간으로 '관리자'에게 알려주는 시스템이 있다면 확산 예방 효과가 있을 것이라고 생각했고, 또한 누군가가 기침을 했을 때 관리자가 기침을 한 사람을 예의주시하게 되면 코로나의 확산을 조금이나마 막을 수 있을 것이라고 생각했다. 따라서 우리 조의 프로젝트 내용은 공공 실내 장소에서 기침을 하거나 마스크 미착용자를 자동으로 판별하여 관리자에게 알려주는 시스템이다.

![1](https://user-images.githubusercontent.com/62248763/101849804-cbcb4c80-3b9b-11eb-9801-a142068b3267.JPG)

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


## 3) Reference

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


## 4) 기술 블로그

- https://m.blog.naver.com/jiao0126/222146583690 : 데이터 수집에 관한 내용
- https://hyoyoung9710.tistory.com/31 : 기침 소리 인식과 마스크 착용/미착용 인식 관한 딥러닝 모델, 라즈베리파이에 관한 내용
- https://blog.naver.com/bigyellow67/222146705478 : 데이터 수집 및 위의 블로그 보고 개인적으로 공부한 내용



## 5) License

MIT License
