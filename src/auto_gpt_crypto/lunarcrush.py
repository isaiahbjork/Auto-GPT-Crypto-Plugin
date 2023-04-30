import requests
import json


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

    def get_lunarcrush_galaxy_score_cryptos(lunarcrush_api) -> float:

        url = "https://lunarcrush.com/api3/coins?sort=galaxy_score&limit=10"
        headers = {
            'Authorization': f'Bearer {lunarcrush_api}'
        }

        response = requests.request("GET", url, headers=headers)

        if response.status_code == 200:
            # Parse the JSON response into a Python dictionary
            data = json.loads(response.text)

            new_data = []
            for item in data["data"]:
                new_item = {}
                new_item["internal_id"] = item["id"]
                new_item["symbol"] = item["s"]
                new_item["name"] = item["n"]
                new_item["price"] = item["p"]
                new_item["price_btc"] = item["p_btc"]
                new_item["volume_usd"] = item["v"]
                new_item["volatility"] = item["vt"]
                new_item["circulating_supply"] = item["cs"]
                new_item["max_supply"] = item["ms"]
                new_item["percent_change_1h"] = item["pch"]
                new_item["percent_change_24h"] = item["pc"]
                new_item["percent_change_7d"] = item["pc7d"]
                new_item["market_cap"] = item["mc"]
                new_item["galaxy_score"] = item["gs"]
                new_item["galaxy_score_previous_24h"] = item["gs_p"]
                new_item["social_score"] = item["ss"]
                new_item["average_sentiment_1_to_5"] = item["as"]
                new_item["bullish_sentiment"] = item["bl"]
                new_item["bearish_sentiment"] = item["br"]
                new_item["social_spam"] = item["sp"]
                new_item["news_articles"] = item["na"]
                new_item["medium_posts"] = item["md"]
                new_item["tweets_24h"] = item["t"]
                new_item["reddit_activity_24h"] = item["r"]
                new_item["youtube_videos"] = item["yt"]
                new_item["social_volume"] = item["sv"]
                new_item["url_shares"] = item["u"]
                new_item["social_contributors_24h"] = item["c"]
                new_item["social_dominance"] = item["sd"]
                new_item["market_dominance"] = item["d"]
                new_item["confidence_score"] = item["cr"]
                new_item["alt_rank"] = item["acr"]
                new_item["time_created"] = item["tc"]
                new_data.append(new_item)

            tokens = json.dumps(new_data)
            return tokens
        else:
            raise Exception(
                f"Failed data from LunarCrush; status code {response.status_code}")
        
    def get_lunarcrush_alt_rank_cryptos(lunarcrush_api) -> float:

        url = "https://lunarcrush.com/api3/coins?sort=alt_rank&limit=10"
        headers = {
            'Authorization': f'Bearer {lunarcrush_api}'
        }

        response = requests.request("GET", url, headers=headers)

        if response.status_code == 200:
            # Parse the JSON response into a Python dictionary
            data = json.loads(response.text)

            new_data = []
            for item in data["data"]:
                new_item = {}
                new_item["internal_id"] = item["id"]
                new_item["symbol"] = item["s"]
                new_item["name"] = item["n"]
                new_item["price"] = item["p"]
                new_item["price_btc"] = item["p_btc"]
                new_item["volume_usd"] = item["v"]
                new_item["volatility"] = item["vt"]
                new_item["circulating_supply"] = item["cs"]
                new_item["max_supply"] = item["ms"]
                new_item["percent_change_1h"] = item["pch"]
                new_item["percent_change_24h"] = item["pc"]
                new_item["percent_change_7d"] = item["pc7d"]
                new_item["market_cap"] = item["mc"]
                new_item["galaxy_score"] = item["gs"]
                new_item["galaxy_score_previous_24h"] = item["gs_p"]
                new_item["social_score"] = item["ss"]
                new_item["average_sentiment_1_to_5"] = item["as"]
                new_item["bullish_sentiment"] = item["bl"]
                new_item["bearish_sentiment"] = item["br"]
                new_item["social_spam"] = item["sp"]
                new_item["news_articles"] = item["na"]
                new_item["medium_posts"] = item["md"]
                new_item["tweets_24h"] = item["t"]
                new_item["reddit_activity_24h"] = item["r"]
                new_item["youtube_videos"] = item["yt"]
                new_item["social_volume"] = item["sv"]
                new_item["url_shares"] = item["u"]
                new_item["social_contributors_24h"] = item["c"]
                new_item["social_dominance"] = item["sd"]
                new_item["market_dominance"] = item["d"]
                new_item["confidence_score"] = item["cr"]
                new_item["alt_rank"] = item["acr"]
                new_item["time_created"] = item["tc"]
                new_data.append(new_item)

            tokens = json.dumps(new_data)
            return tokens
        else:
            raise Exception(
                f"Failed to get data from LunarCrush; status code {response.status_code}")
        
    def get_recent_crypto_social_feeds(lunarcrush_api) -> float:
        url = "https://lunarcrush.com/api3/feeds?hours=1"
        headers = {
            'Authorization': f'Bearer {lunarcrush_api}'
        }
        response = requests.request("GET", url, headers=headers)
        if response.status_code == 200:
            return response.text
        else:
            raise Exception(
                f"Failed to get data from LunarCrush; status code {response.status_code}")
