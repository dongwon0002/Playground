## 아두이노 led를 웹캠에 감지한 손모양으로 제어하기
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

'''
python hello.py
'''

-------
## 실제 동작
![Image](https://github.com/user-attachments/assets/aef97cd2-99fb-4b71-a6f4-d5cd459eb353)
