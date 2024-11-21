import requests
import json 
from urllib.parse import unquote, parse_qs, urlparse
from loguru import logger
import time 
import os
import pyfiglet
from colorama import Fore, Style, init

headers = {
    'accept': '*/*',
    'accept-language': 'en,en-GB;q=0.9,en-US;q=0.8',
    'authorization': '',
    'cache-control': 'no-cache',
    'content-type': 'application/json',
    'origin': 'https://bot.toncircle.org',
    'pragma': 'no-cache',
    'priority': 'u=1, i',
    'referer': 'https://bot.toncircle.org/',
    'x-requested-with': 'org.telegram.messenger',
}

def key_bot():
    try:
        print("\033[96m")
        print("╔════════════════════════════════════════════╗")
        print("║           CIRCLE by Codex Vault            ║")
        print("║                                            ║")
        print("║                  Aphator                   ║")
        print("╚════════════════════════════════════════════╝")
        print("\033[0m")
    except Exception as e:
        print(f"An error occurred: {e}")

def watch(init):
    tgWebAppData = parse_qs(parse_qs(urlparse(init).fragment).get('tgWebAppData', [None])[0])
    user_data = unquote(tgWebAppData['user'][0])
    id = json.loads(user_data)['id']
    chat_instance = tgWebAppData['chat_instance'][0]
    params = {
        'blockId': '3852',
        'tg_id': str(id),
        'tg_platform': 'android',
        'platform': 'Linux arm64',
        'language': 'en',
        'chat_type': 'sender',
        'chat_instance': chat_instance,
    }
    for i in range(1, 100000000000):
        requests.get((requests.get('https://api.adsgram.ai/adv', params=params, headers=headers).json()['banner']['trackings'][-2])['value'])
        logger.info(f'{i} Ad reward claimed')
        time.sleep(60)
        logger.debug('sleeping 1 min for the next Ad')
    # json_data = { 'bet': 1000,'chance': 1}
    # requests.post('https://api.toncircle.org/user/games/upgrade/spin', json=json_data)

init(autoreset=True)
if __name__ == '__main__':
    os.system('cls' if os.name == 'nt' else 'clear')
    key_bot()  # Call the new banner function
    link = input("\nEnter your Circle session link : ")
    watch(link)