import requests

api_key = "068aaf864d78486062a0b5e1ffdeca9c"

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
