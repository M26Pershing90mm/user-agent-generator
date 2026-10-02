# User-Agent Generator

Windows 11과 Samsung Galaxy Android 환경용 Firefox User-Agent 문자열을 생성하는 Python 도구입니다.

프로그램 실행 시 Mozilla의 공식 Product Details 데이터를 조회하여 최신 Firefox Stable 버전을 자동으로 사용합니다. 인터넷 연결이 없거나 버전 조회에 실패하면 프로그램에 설정된 예비 Firefox 버전을 사용합니다.

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

## 실행 방법

저장소를 다운로드하거나 user agent generator firefox.py 파일을 받은 뒤 터미널 또는 명령 프롬프트에서 실행합니다.

파일명에 공백이 있으므로 실행할 때 파일명을 따옴표로 묶어야 합니다.

    python "user agent generator firefox.py"

Windows에서 python 명령이 동작하지 않는 경우:

    py "user agent generator firefox.py"

## 메뉴

프로그램을 실행하면 다음 메뉴가 표시됩니다.

    ==============================================
    User-Agent Generator
    ==============================================
    1. Windows 11 + Firefox
    2. Samsung Android 13~17 + Firefox
    0. 종료
    ==============================================
    선택:

## 1. Windows 11 + Firefox

메뉴에서 1을 선택합니다.

    선택: 1

프로그램은 Mozilla 서버에서 최신 Firefox Stable 버전을 확인한 뒤 Windows 11 환경용 Firefox User-Agent를 생성합니다.

예:

    최신 Firefox: 157.0

    Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:157.0) Gecko/20100101 Firefox/157.0

Windows 11에서도 Firefox User-Agent의 Windows 플랫폼 토큰은 일반적으로 Windows NT 10.0으로 표시됩니다.

따라서 Windows 11에서 Windows NT 10.0이 표시되는 것은 정상입니다.

생성 후 다음 질문이 표시됩니다.

    파일로 저장할까요? (y/N):

y를 입력하면 다음 파일로 저장됩니다.

    windows_firefox_ua.txt

## 2. Samsung Android 13~17 + Firefox

메뉴에서 2를 선택합니다.

    선택: 2

Android 버전을 선택합니다.

    Android 버전 13~17 (Enter = 랜덤):

다음 버전 중 하나를 입력할 수 있습니다.

    13
    14
    15
    16
    17

아무것도 입력하지 않고 Enter를 누르면 Android 13~17 중 하나를 무작위로 선택합니다.

다음으로 생성할 User-Agent 개수를 입력합니다.

    생성 개수: 5

예:

    최신 Firefox: 157.0

    [1] Android 16 / Galaxy S25 Ultra / SM-S938B
    Mozilla/5.0 (Android 16; Mobile; rv:157.0) Gecko/157.0 Firefox/157.0

생성 후 다음 질문이 표시됩니다.

    파일로 저장할까요? (y/N):

y를 입력하면 다음 파일로 저장됩니다.

    samsung_android_firefox_ua.txt

## Firefox for Android User-Agent 형식

Firefox for Android의 일반적인 스마트폰 User-Agent는 다음과 같은 형태입니다.

    Mozilla/5.0 (Android 16; Mobile; rv:157.0) Gecko/157.0 Firefox/157.0

이 프로그램은 Android용 Chrome에서 사용하는 다음과 같은 형식의 User-Agent를 생성하지 않습니다.

    Mozilla/5.0 (Linux; Android 16; ...) AppleWebKit/... Chrome/... Mobile Safari/...

Android 모드에서도 브라우저 부분은 Firefox 형식으로 생성됩니다.

## Samsung Galaxy 모델 정보

프로그램은 선택된 Android 버전에 맞춰 등록된 Samsung Galaxy 모델 중 하나를 참고 정보로 표시합니다.

예:

    Android 16 / Galaxy S25 Ultra / SM-S938B

하지만 Firefox for Android의 일반적인 User-Agent 문자열에는 SM-S938B 같은 Samsung 모델 코드가 포함되지 않습니다.

따라서 Galaxy 모델명과 모델 코드는 참고용 정보이며 실제 Firefox User-Agent는 다음과 같은 형식으로 생성됩니다.

    Mozilla/5.0 (Android 16; Mobile; rv:157.0) Gecko/157.0 Firefox/157.0

같은 Android 버전과 같은 Firefox 버전을 사용하는 경우 서로 다른 Galaxy 모델이 선택되어도 최종 User-Agent 문자열은 동일할 수 있습니다.

## 최신 Firefox 버전 자동 조회

프로그램은 Mozilla Product Details 데이터를 사용합니다.

    https://product-details.mozilla.org/1.0/firefox_versions.json

응답 데이터의 LATEST_FIREFOX_VERSION 값을 읽어 Windows와 Android Firefox User-Agent 생성에 사용합니다.

인터넷 연결 문제나 Mozilla 서버 응답 오류 등으로 최신 버전을 가져오지 못하면 프로그램에 설정된 예비 Firefox 버전을 사용합니다.

예:

    Firefox 버전 조회 실패 - 예비 버전 사용: 157.0

## 생성 파일

Windows 모드에서 저장:

    windows_firefox_ua.txt

Android 모드에서 저장:

    samsung_android_firefox_ua.txt

Android에서 여러 개를 생성하면 User-Agent 문자열이 한 줄에 하나씩 저장됩니다.

## .gitignore 권장 설정

프로그램 실행으로 생성되는 TXT 파일을 Git 저장소에서 제외하려면 .gitignore 파일에 다음 항목을 추가할 수 있습니다.

    windows_firefox_ua.txt
    samsung_android_firefox_ua.txt

## 참고 사항

User-Agent 문자열을 변경한다고 실제 운영체제, 스마트폰 모델, Firefox 설정 또는 전체 브라우저 환경이 변경되는 것은 아닙니다.

웹사이트는 User-Agent 이외에도 다양한 브라우저 및 장치 정보를 사용할 수 있습니다.

이 프로젝트는 웹 개발, 브라우저 호환성 확인, 테스트 및 연구 목적으로 사용할 수 있습니다.

## License

MIT License

Copyright (c) 2026 Sakai

자세한 내용은 저장소의 LICENSE 파일을 확인하십시오.
