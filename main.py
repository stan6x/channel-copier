import asyncio

from telethon import TelegramClient

import config

client = TelegramClient(config.SESSION_NAME, config.API_ID, config.API_HASH)


async def main():
    for channel in config.CHANNEL1:
        async for message in client.iter_messages(channel, reverse=True):
            await client.send_message(config.CHANNEL2, message)
            await asyncio.sleep(config.INTERVAL)


with client:
    client.loop.run_until_complete(main())
