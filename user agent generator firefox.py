import json
import random
import urllib.request

FIREFOX_URL = "https://product-details.mozilla.org/1.0/firefox_versions.json"
FIREFOX_FALLBACK = "157.0"

GALAXY_MODELS = {
    "13": [
        ("Galaxy S22", "SM-S901B"),
        ("Galaxy S22+", "SM-S906B"),
        ("Galaxy S22 Ultra", "SM-S908B"),
        ("Galaxy S23", "SM-S911B"),
        ("Galaxy S23+", "SM-S916B"),
        ("Galaxy S23 Ultra", "SM-S918B"),
        ("Galaxy A34 5G", "SM-A346B"),
        ("Galaxy A54 5G", "SM-A546B"),
        ("Galaxy Z Flip5", "SM-F731B"),
        ("Galaxy Z Fold5", "SM-F946B"),
    ],
    "14": [
        ("Galaxy S23", "SM-S911B"),
        ("Galaxy S23+", "SM-S916B"),
        ("Galaxy S23 Ultra", "SM-S918B"),
        ("Galaxy S23 FE", "SM-S711B"),
        ("Galaxy S24", "SM-S921B"),
        ("Galaxy S24+", "SM-S926B"),
        ("Galaxy S24 Ultra", "SM-S928B"),
        ("Galaxy A35 5G", "SM-A356B"),
        ("Galaxy A55 5G", "SM-A556B"),
        ("Galaxy Z Flip6", "SM-F741B"),
        ("Galaxy Z Fold6", "SM-F956B"),
    ],
    "15": [
        ("Galaxy S24", "SM-S921B"),
        ("Galaxy S24+", "SM-S926B"),
        ("Galaxy S24 Ultra", "SM-S928B"),
        ("Galaxy S25", "SM-S931B"),
        ("Galaxy S25+", "SM-S936B"),
        ("Galaxy S25 Ultra", "SM-S938B"),
        ("Galaxy S25 Edge", "SM-S937B"),
        ("Galaxy A36 5G", "SM-A366B"),
        ("Galaxy A56 5G", "SM-A566B"),
        ("Galaxy Z Flip7", "SM-F766B"),
        ("Galaxy Z Fold7", "SM-F966B"),
    ],
    "16": [
        ("Galaxy S24", "SM-S921B"),
        ("Galaxy S24+", "SM-S926B"),
        ("Galaxy S24 Ultra", "SM-S928B"),
        ("Galaxy S25", "SM-S931B"),
        ("Galaxy S25+", "SM-S936B"),
        ("Galaxy S25 Ultra", "SM-S938B"),
        ("Galaxy S25 Edge", "SM-S937B"),
        ("Galaxy S26", "SM-S942B"),
        ("Galaxy S26+", "SM-S947B"),
        ("Galaxy S26 Ultra", "SM-S948B"),
        ("Galaxy A36 5G", "SM-A366B"),
        ("Galaxy A56 5G", "SM-A566B"),
        ("Galaxy Z Flip7", "SM-F766B"),
        ("Galaxy Z Fold7", "SM-F966B"),
    ],
    "17": [
        ("Galaxy S26", "SM-S942B"),
        ("Galaxy S26+", "SM-S947B"),
        ("Galaxy S26 Ultra", "SM-S948B"),
    ],
}


def get_json(url):
    request = urllib.request.Request(url, headers={"User-Agent": "Mozilla/5.0"})
    with urllib.request.urlopen(request, timeout=6) as response:
        return json.load(response)


def latest_firefox():
    try:
        return get_json(FIREFOX_URL)["LATEST_FIREFOX_VERSION"]
    except Exception:
        return FIREFOX_FALLBACK


def windows_user_agent(version):
    return (
        f"Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:{version}) "
        f"Gecko/20100101 Firefox/{version}"
    )


def android_user_agent(android_version, version):
    return (
        f"Mozilla/5.0 (Android {android_version}; Mobile; rv:{version}) "
        f"Gecko/{version} Firefox/{version}"
    )


def ask_count():
    while True:
        try:
            count = int(input("생성 개수: ").strip())
            if 1 <= count <= 10000:
                return count
        except ValueError:
            pass
        print("1~10000 사이 숫자를 입력하세요.")


def ask_android_version():
    while True:
        value = input("Android 버전 13~17 (Enter = 랜덤): ").strip()
        if not value:
            return None
        if value in GALAXY_MODELS:
            return value
        print("13, 14, 15, 16, 17 중 하나를 입력하세요.")


def save_file(lines, filename):
    with open(filename, "w", encoding="utf-8") as file:
        file.write("\n".join(lines) + "\n")
    print(f"저장: {filename}")


def run_windows():
    version = latest_firefox()
    ua = windows_user_agent(version)

    print()
    print(f"Firefox {version}")
    print(ua)

    if input("\n파일로 저장할까요? (y/N): ").strip().lower() == "y":
        save_file([ua], "windows_firefox_ua.txt")


def run_android():
    version = latest_firefox()
    selected_version = ask_android_version()
    count = ask_count()
    results = []

    print()
    print(f"Firefox for Android {version}")

    for number in range(1, count + 1):
        android_version = selected_version or random.choice(list(GALAXY_MODELS))
        name, model = random.choice(GALAXY_MODELS[android_version])
        ua = android_user_agent(android_version, version)
        results.append(ua)

        print()
        print(f"[{number}] Android {android_version} / {name} / {model}")
        print(ua)

    if input("\n파일로 저장할까요? (y/N): ").strip().lower() == "y":
        save_file(results, "samsung_android_firefox_ua.txt")


def main():
    while True:
        print()
        print("User-Agent Generator")
        print("1. Windows 11 + Firefox")
        print("2. Samsung Android 13~17 + Firefox")
        print("0. 종료")

        choice = input("선택: ").strip()

        if choice == "1":
            run_windows()
        elif choice == "2":
            run_android()
        elif choice == "0":
            break
        else:
            print("1, 2, 0 중 하나를 입력하세요.")


if __name__ == "__main__":
    main()
