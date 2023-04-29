import requests
class LunarCrush():
    def get_coin_of_the_day(lunarcrush_api) -> float:

            url = "https://lunarcrush.com/api3/coinoftheday"
            headers = {
                'Authorization': f'Bearer {lunarcrush_api}'
            }

            response = requests.request("GET", url, headers=headers)

            if response.status_code == 200:
                return response.text.encode('utf8')
            else:
                raise Exception(
                    f"Failed to get coin of the day from LunarCrush; status code {response.status_code}")