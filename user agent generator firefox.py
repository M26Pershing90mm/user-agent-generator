import json
import random
import urllib.request
import urllib.error

FIREFOX_URL = "https://product-details.mozilla.org/1.0/firefox_versions.json"
FIREFOX_FALLBACK = "157.0"

GALAXY_MODELS = {
    "13": [
        ("Galaxy S22","SM-S901B"),
        ("Galaxy S22+","SM-S906B"),
        ("Galaxy S22 Ultra","SM-S908B"),
        ("Galaxy S23","SM-S911B"),
        ("Galaxy S23+","SM-S916B"),
        ("Galaxy S23 Ultra","SM-S918B"),
        ("Galaxy A34 5G","SM-A346B"),
        ("Galaxy A54 5G", SM-A546B"),
        ("Galaxy Z Flip5","SM-F731B"),
        ("Galaxy Z Fold5","SM-F946B"),
    ],

    "14": [
        ("Galaxy S23","SM-S911B"),
        ("Galaxy S23+","SM-S916B"),
        ("Galaxy S23 Ultra","SM-S918B"),
        ("Galaxy S23 FE","SM-S711B"),
        ("Galaxy S24","SM-S921B"),
        ("Galaxy S24+","SM-S926B"),
        ("Galaxy S24 Ultra","SM-S928B"),
        ("Galaxy A35 5G","SM-A356B"),
        ("Galaxy A55 5G","SM-A556B"),
        ("Galaxy Z Flip5","SM-F731B"),
        ("Galaxy Z Fold5","SM-F946B"),
        ("Galaxy Z Flip6","SM-F741B"),
        ("Galaxy Z Fold6","SM-F956B"),
    ],

    "15": [
        ("Galaxy S22","SM-S901B"),
        ("Galaxy S22+","SM-S906B"),
        ("Galaxy S22 Ultra","SM-S908B"),
        ("Galaxy S23","SM-S911B"),
        ("Galaxy S23+","SM-S916B"),
        ("Galaxy S23 Ultra","SM-S918B"),
        ("Galaxy S23 FE","SM-S711B"),
        ("Galaxy S24","SM-S921B"),
        ("Galaxy S24+","SM-S926B"),
        ("Galaxy S24 Ultra""SM-S928B"),
        ("Galaxy S25","SM-S931B"),
        ("Galaxy S25+","SM-S936B"),
        ("Galaxy S25 Ultra","SM-S938B"),
        ("Galaxy S25 Edge","SM-S937B"),
        ("Galaxy A35 5G","SM-A356B"),
        ("Galaxy A55 5G","SM-A556B"),
        ("Galaxy A36 5G","SM-A366B"),
        ("Galaxy A56 5G","SM-A566B"),
        ("Galaxy Z Flip5","SM-F731B"),
        ("Galaxy Z Fold5","SM-F946B"),
        ("Galaxy Z Flip6","SM-F741B"),
        ("Galaxy Z Fold6","SM-F956B"),
    ],

    "16": [
        ("Galaxy S23","SM-S911B"),
        ("Galaxy S23+","SM-S916B"),
        ("Galaxy S23 Ultra","SM-S918B"),
        ("Galaxy S23 FE","SM-S711B"),
        ("Galaxy S24","SM-S921B"),
        ("Galaxy S24+","SM-S926B"),
        ("Galaxy S24 Ultra","SM-S928B"),
        ("Galaxy S25","SM-S931B"),
        ("Galaxy S25+","SM-S936B"),
        ("Galaxy S25 Ultra","SM-S938B"),
        ("Galaxy S25 Edge","SM-S937B"),
        ("Galaxy S26","SM-S942B"),
        ("Galaxy S26+","SM-S947B"),
        ("Galaxy S26 Ultra","SM-S948B"),
        ("Galaxy A34 5G","SM-A346B"),
        ("Galaxy A54 5G","SM-A546B"),
        ("Galaxy A35 5G","SM-A356B"),
        ("Galaxy A55 5G","SM-A556B"),
        ("Galaxy A36 5G","SM-A366B"),
        ("Galaxy A56 5G","SM-A566B"),
        ("Galaxy Z Flip5","SM-F731B"),
        ("Galaxy Z Fold5","SM-F946B"),
        ("Galaxy Z Flip6","SM-F741B"),
        ("Galaxy Z Fold6","SM-F956B"),
        ("Galaxy Z Flip7","SM-F766B"),
        ("Galaxy Z Fold7","SM-F966B"),
    ],

    "17": [
        ("Galaxy S26","SM-S942B"),
        ("Galaxy S26+","SM-S947B"),
        ("Galaxy S26 Ultra","SM-S948B"),
    ],
}


def get_json(url):
    request = urllib.request.Request(
        url,
        headers={
            "User-Agent": "Mozilla/5.0",
            "Accept": "application/json",
        },
    )

    with urllib.request.urlopen(request, timeout=8) as response:
        return json.load(response)


def latest_firefox():
    try:
        data = get_json(FIREFOX_URL)
        version = data.get("LATEST_FIREFOX_VERSION")

        if version:
            return version, True

    except (
        urllib.error.URLError,
        urllib.error.HTTPError,
        TimeoutError,
        json.JSONDecodeError,
        KeyError,
    ):
        pass

    return FIREFOX_FALLBACK, False


def windows_user_agent(version):
    return (
        f"Mozilla/5.0 "
        f"(Windows NT 10.0; Win64; x64; rv:{version}) "
        f"Gecko/20100101 Firefox/{version}"
    )


def android_user_agent(android_version, version):
    return (
        f"Mozilla/5.0 "
        f"(Android {android_version}; Mobile; rv:{version}) "
        f"Gecko/{version} Firefox/{version}"
    )


def ask_count():
    while True:
        value = input("생성 개수: ").strip()

        try:
            count = int(value)

            if 1 <= count <= 10000:
                return count

        except ValueError:
            pass

        print("1~10000 사이 숫자를 입력하세요.")


def ask_android_version():
    while True:
        value = input(
            "Android 버전 13~17 (Enter = 랜덤): "
        ).strip()

        if value == "":
            return None

        if value in GALAXY_MODELS:
            return value

        print("13, 14, 15, 16, 17 중 하나를 입력하세요.")


def save_file(lines, filename):
    try:
        with open(filename, "w", encoding="utf-8") as file:
            file.write("\n".join(lines))
            file.write("\n")

        print(f"저장 완료: {filename}")

    except OSError as error:
        print(f"파일 저장 실패: {error}")


def show_firefox_version(version, online):
    if online:
        print(f"최신 Firefox: {version}")
    else:
        print(
            f"Firefox 버전 조회 실패 - "
            f"예비 버전 사용: {version}"
        )


def run_windows():
    version, online = latest_firefox()

    print()
    show_firefox_version(version, online)
    print()

    ua = windows_user_agent(version)

    print(ua)

    save = input(
        "\n파일로 저장할까요? (y/N): "
    ).strip().lower()

    if save == "y":
        save_file(
            [ua],
            "windows_firefox_ua.txt"
        )


def run_android():
    version, online = latest_firefox()
    selected_version = ask_android_version()
    count = ask_count()

    results = []

    print()
    show_firefox_version(version, online)
    print()

    for number in range(1, count + 1):
        if selected_version:
            android_version = selected_version
        else:
            android_version = random.choice(
                list(GALAXY_MODELS.keys())
            )

        name, model = random.choice(
            GALAXY_MODELS[android_version]
        )

        ua = android_user_agent(
            android_version,
            version
        )

        results.append(ua)

        print(
            f"[{number}] "
            f"Android {android_version} / "
            f"{name} / {model}"
        )

        print(ua)
        print()

    save = input(
        "파일로 저장할까요? (y/N): "
    ).strip().lower()

    if save == "y":
        save_file(
            results,
            "samsung_android_firefox_ua.txt"
        )


def main():
    while True:
        print()
        print("=" * 46)
        print("User-Agent Generator")
        print("=" * 46)
        print("1. Windows 11 + Firefox")
        print("2. Samsung Android 13~17 + Firefox")
        print("0. 종료")
        print("=" * 46)

        choice = input("선택: ").strip()

        if choice == "1":
            run_windows()

        elif choice == "2":
            run_android()

        elif choice == "0":
            print("종료합니다.")
            break

        else:
            print("1, 2, 0 중 하나를 입력하세요.")


if __name__ == "__main__":
    main()
