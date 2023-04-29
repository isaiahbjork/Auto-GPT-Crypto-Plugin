import json
class Telegram():
    async def find_new_eth_tokens(client):
        entity = await client.get_entity('DEXTNewPairsBot')
        messages = await client.get_messages(entity, 20)
        messages_list = []  # Create an empty list to store messages

        for message in messages:
            messages_list.append(str(message.message))

        # Convert the messages_list to a JSON string
        messages_json = json.dumps(messages_list)
        return messages_json

    async def find_telegram_chat_messages(client, chat_name):
        entity = await client.get_entity(chat_name)
        messages = await client.get_messages(entity, 20)
        messages_list = []  # Create an empty list to store messages

        for message in messages:
            messages_list.append(str(message.message))

        # Convert the messages_list to a JSON string
        messages_json = json.dumps(messages_list)
        return messages_json