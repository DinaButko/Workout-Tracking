import requests
from datetime import datetime

APP_ID = "XXXXXXX"
API_KEY = "XXXXXX"

GENDER = "female"
WEIGHT_KG = "55"
HEIGHT_CM = "165"
AGE = "33"

headers = {
    "x-app-id": APP_ID,
    "x-app-key": API_KEY
}
exercise_endpoint = "https://trackapi.nutritionix.com/v2/natural/exercise"

exercise_text = input("Tell me which exercises you did:")
user_params = {
 "query": exercise_text,
 "gender":GENDER,
 "weight_kg": WEIGHT_KG,
 "height_cm": HEIGHT_CM,
 "age": AGE
}

response = requests.post(url= exercise_endpoint, json =user_params, headers = headers)
result = response.json()
print(result)

post_endpoind = "https://api.sheety.co/7d9c402a50526a1fe9edfda615df26f7/myWorkouts/workouts"


today_date = datetime.now().strftime("%d/%m/%Y")
now_time = datetime.now().strftime("%X")
for exercise in result["exercises"]:
    sheet_inputs = {
"workout": {
"date": today_date,
"time": now_time,
"exercise": exercise["name"].title(),
"duration": exercise["duration_min"],
"calories": exercise["nf_calories"]
        }
    }

sheet_response = requests.post(post_endpoind, json=sheet_inputs)
print(sheet_response.text)