# 날씨 조회 콘솔 앱 (Python)

## 프로젝트 소개
사용자가 도시 이름을 입력하면, 해당 도시의 날씨, 기온, 습도를 알려주는 간단한 콘솔 프로그램입니다.  
OpenWeather API를 사용하여 실시간 데이터를 불러옵니다.

## 사용기술
- Python
- requests 라이브러리
- OpenWeather API

## 실행 방법
1. `weather.py` 실행
2. 도시 이름 입력 (예: seoul)
3. 날씨 정보 출력

## 📄 주요 코드

```python
import requests

api_key = "여기에_본인의_API_KEY_입력"

city = input("도시를 입력하세요 (영문): ").strip()

url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric&lang=kr"

response = requests.get(url)
data = response.json()

if response.status_code == 200:
    weather = data['weather'][0]['description']
    temp = data['main']['temp']
    humidity = data['main']['humidity']
    
    print("="*40)
    print(f" {city.title()}의 날씨 정보")
    print(f" 상태 : {weather}")
    print(f" 온도 : {temp}°C")
    print(f" 습도 : {humidity}%")
    print("="*40)

else:
    print("! 도시 이름을 다시 확인해주세요.")
    print(f"(에러 코드: {response.status_code})")
```
![Seoul 날씨 실행화면](screenshots/seoul_weather.png)
## 👤 만든 사람
김제완