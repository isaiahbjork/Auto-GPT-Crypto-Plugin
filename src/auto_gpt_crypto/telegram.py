from telethon import TelegramClient
import os
import asyncio

telegram_api_id = os.getenv('TELEGRAM_API_ID')
telegram_api_hash = os.getenv('TELEGRAM_API_HASH')


class Telegram():

    def __init__(self, api_key: str = None, hash: str = None):
        self.api_key = api_key
        self.hash = hash
        self.client = TelegramClient(
            'Auto-GPT Crypto', api_key, hash)
        

    async def get_new_eth_tokens_async(self):

        entity = await self.client.get_entity('DEXTNewPairsBot')
        messages = await self.client.get_messages(entity, 20)
        print(entity)
        print(messages)
        messages_list = []  # Create an empty list to store messages

        for message in messages:
            messages_list.append(message.text)
        return messages_list

    def get_new_eth_tokens(self):
        loop = asyncio.new_event_loop()
        asyncio.set_event_loop(loop)
        result = loop.run_until_complete(self.get_new_eth_tokens_async())
        loop.close()
        return result
    
    

