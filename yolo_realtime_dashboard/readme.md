### yolo모델을 이용한 아두이노 릴레이모듈 제어, 이 과정에서 생성된 log에 대해 실시간 대시보드 구성
- streamlit을 통해 db를 읽어와서 시각화하는 방식을 사용
- sqlite3 라이브러리를 통해 log를 수집, 저장
---------------------
수집 log데이터
| index | id   | timestamp           | class_name | confidence | count | x1  | y1  | x2  | y2  |
|-------|------|---------------------|------------|------------|-------|-----|-----|-----|-----|
| 0     | 1430 | 2025-01-22 22:50:33 | dog        | 0.59       | 9     | 161 | 198 | 435 | 421 |
| 1     | 1429 | 2025-01-22 22:50:32 | dog        | 0.54       | 8     | 163 | 200 | 435 | 417 |

------------------------ 
class별 count barplot추가 

<div style="display: flex;">
  <img src="https://github.com/user-attachments/assets/2a374c56-b6ac-4b5a-9740-9f3d50b06984" width="45%" />
  <img src="https://github.com/user-attachments/assets/251cae96-4833-4416-8f3e-f33087bad8ca" width="45%" />
</div>

---------


