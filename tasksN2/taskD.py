# Реализовать функцию, которая замеряет время на исполнение 100 запросов к адресу:
# http://httpbin.org/delay/3. Запросы должны выполняться асинхронно.
# Допускается написание вспомогательных функций и использование сторонних библиотек.
# Результат замера времени выводит в консоль.
# Ожидаемое время не должно превышать 10 секунд.

import asyncio
import time

import aiohttp
import requests


def get_response_synchronously():
    """Synchronously"""
    url = 'http://httpbin.org/delay/3'
    start = time.time()
    for i in range(1, 5):
        print(i)
        requests.get(url=url)
    end = time.time()
    print(f'Time of function is {end - start}')


get_response_synchronously()


async def get_response_asynchronously():
    url = 'http://httpbin.org/delay/3'

    async with aiohttp.ClientSession() as session:
        response = session.get(url=url)

