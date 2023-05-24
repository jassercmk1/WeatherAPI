from fastapi import FastAPI
import uvicorn
import httpx


app = FastAPI()
base_url = "http://api.openweathermap.org/data/2.5/weather?"


def get_api_key():
    with open("apikey.txt", "r") as file:
        return file.read().strip()


@app.get("/")
async def welcome_user():
    return {"Welcome to Weather App"}


@app.get("/weather/")
async def get_weather_api(city_name: str) -> dict:
    api_key = get_api_key()
    complete_url = f"{base_url}appid={api_key}&q={city_name}"
    async with httpx.AsyncClient() as client:
        try:
            response = await client.get(complete_url)
            response.raise_for_status()
            data_json = response.json()

            temperature_kelvin = data_json["main"]["temp"]
            temperature_celsius = temperature_kelvin - 273.15

            weather_data = {
                "city_name": data_json["name"],
                "temperature": round(temperature_celsius, 2),
                "description": data_json["weather"][0]["description"],
                "coord": data_json["coord"],
                "weather": data_json["weather"],
                "base": data_json["base"],
                "main": data_json["main"],
                "visibility": data_json["visibility"],
                "wind": data_json["wind"],
                "clouds": data_json["clouds"],
                "dt": data_json["dt"],
                "sys": data_json["sys"],
                "timezone": data_json["timezone"],
                "id": data_json["id"],
                "name": data_json["name"],
                "cod": data_json["cod"],
            }
            return weather_data
        except (httpx.HTTPError, httpx.RequestError, httpx.TimeoutException) as e:
            return {"error": f"An error occurred: {str(e)}"}
        except (KeyError, IndexError) as e:
            return {"error": f"Invalid response format: {str(e)}"}

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
