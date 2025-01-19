## 아두이노 led를 웹캠에서 감지한 손모양으로 제어하기
------
### 회로구성 요소
1. arduino UNO
2. 릴레이 모듈
3. led 라이트
### 상태
- arduino uno -> com5연결
- arduino uno -> arduino IDE에서 file/examples/firmata/standardfirmata uploaded
- 릴레이모듈 -> 3번에 연결

### 파일 설명
controller.py >>> pyfirmata2를 이용하여 arduino를 제어
hello.py >>> 실행파일, 웹캠의 화면에서 detector사용

```
python hello.py
```
-----
```
certifi==2024.12.14
charset-normalizer==3.4.1
cvzone==1.6.1
docopt==0.6.2
idna==3.10
joblib==1.4.2
numpy==2.2.1
opencv-python==4.11.0.86
pipreqs==0.4.13
pyFirmata==1.1.0
pyFirmata2==2.5.1
pyserial==3.5
requests==2.32.3
scikit-learn==1.6.1
scipy==1.15.1
threadpoolctl==3.5.0
urllib3==2.3.0
yarg==0.1.10
```

-------
## 실제 동작
![Image](https://github.com/user-attachments/assets/aef97cd2-99fb-4b71-a6f4-d5cd459eb353)
