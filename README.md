User Agent Generator
Windows 11과 Samsung Galaxy Android 환경용 Firefox User-Agent를 생성하는 Python 도구입니다.
프로그램 실행 시 Mozilla의 공식 Product Details 데이터를 조회해 최신 Firefox Stable 버전을 자동으로 사용합니다.
인터넷 연결이 없거나 조회에 실패하면 프로그램에 지정된 예비 버전을 사용합니다.
기능
Windows 11+최신 Firefox User-Agent 생성
Samsung Galaxy+Android 13~17+최신 Firefox User-Agent 생성
Mozilla 공식 데이터에서 최신 Firefox Stable 버전 자동 조회
Android 버전별 Galaxy 모델을 참고 프로필로 표시
여러 개 생성 및 TXT 저장
외부 패키지 설치 불필요
요구 사항
Python 3.9 이상 권장
최신 Firefox 버전 자동 조회를 위한 인터넷 연결
pip install 은 필요하지 않습니다.
실행 방법
저장소를 다운로드하거나 user agent generator.py 를 받은 뒤 터미널에서 실행
python user_agent_generator.py
Windows에서 python 명령이 동작하지 않으면:
py user_agent_generator.py
메뉴
User-Agent Generator
1.Windows 11 + Firefox
2.Samsung Android 13~17 + Firefox
0.종료
선택:
1.Windows 11 + Firefox
메뉴에서 1 을 입력합니다.
선택: 1
최신 Firefox Stable 버전을 조회한 뒤 Windows 11용 Firefox UA를 출력
예:Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:157.0) Gecko/20100101 Firefox/157.0
Windows 11의 Firefox UA에서도 Windows 플랫폼 토큰은 Windows NT 10.0으로 표시
저장 질문에서 y를 입력하면:windows_firefox_ua.txt
파일로 저장
2. Samsung Android 13~17 + Firefox
메뉴에서 2를 입력
선택:2
Android 버전을 선택
Android 버전 13~17 (Enter = 랜덤):
13, 14, 15, 16, 17 중 하나를 입력하거나 Enter를 눌러 랜덤으로 선택할 수 있음
생성 개수를 입력합니다.
생성 개수: 5
예:[1] Android 16/Galaxy S25 Ultra / SM-S938B
Mozilla/5.0 (Android 16; Mobile; rv:157.0) Gecko/157.0 Firefox/157.0
저장을 선택하면:samsung_android_firefox_ua.txt
파일로 저장
Android Firefox UA 형식
Firefox for Android는 일반적으로 다음 형식을 사용
Mozilla/5.0 (Android 16; Mobile; rv:157.0) Gecko/157.0 Firefox/157.0
Android용 Chrome의 다음과 같은 형식은 이 프로그램에서 생성하지 않음
Mozilla/5.0 (Linux; Android 16; ...) AppleWebKit/... Chrome/... Mobile Safari/...
Firefox Android UA에는 SM-S938B 같은 삼성 모델명이 일반적으로 포함되지 않습니다.
프로그램에서 Galaxy 모델명과 모델 코드는 Android 버전별 참고 프로필로만 표시
따라서 같은 Android 버전과 같은 Firefox 버전을 사용하면 서로 다른 Galaxy 모델도 실제 Firefox UA 문자열은 동일할 수 있음
최신 Firefox 버전 조회
다음 Mozilla Product Details 데이터를 사용합니다.
https://product-details.mozilla.org/1.0/firefox_versions.json
LATEST_FIREFOX_VERSION 값을 사용해 Windows와 Android Firefox UA를 생성
참고
User-Agent 문자열만 변경한다고 실제 운영체제,스마트폰 모델,브라우저 설정 또는 전체 브라우저 핑거프린트가 변경되는 것은 아님
웹 개발, 호환성 확인, 테스트 및 연구 용도로 사용할 수 있습니다.
