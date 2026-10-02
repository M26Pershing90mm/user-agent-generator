# User-Agent Generator

Windows 11과 Samsung Galaxy Android 환경용 Firefox User-Agent 문자열을 생성하는 Python 도구입니다.

프로그램 실행 시 Mozilla의 공식 Product Details 데이터를 조회하여 최신 Firefox Stable 버전을 자동으로 사용합니다. 인터넷 연결이 없거나 버전 조회에 실패하면 프로그램에 설정된 예비 Firefox 버전을 사용 합니다.

## 기능

- Windows 11 + 최신 Firefox User-Agent 생성
- Samsung Galaxy + Android 13~17 + 최신 Firefox User-Agent 생성
- Mozilla 공식 데이터에서 최신 Firefox Stable 버전 자동 조회
- Android 버전별 Samsung Galaxy 모델을 참고 정보로 표시
- Android User-Agent 여러 개 생성
- 생성 결과 TXT 파일 저장
- 별도 Python 패키지 설치 불필요
- Python 표준 라이브러리만 사용

## 요구 사항

- Python 3.9 이상 권장
- 최신 Firefox 버전 자동 조회를 위한 인터넷 연결

별도의 pip install 과정은 필요하지 않습니다.
