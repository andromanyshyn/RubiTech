# Реализовать функцию, которая замеряет время на исполнение 100 запросов к адресу:
# http://httpbin.org/delay/3. Запросы должны выполняться асинхронно.
# Допускается написание вспомогательных функций и использование сторонних библиотек.
# Результат замера времени выводит в консоль.
# Ожидаемое время не должно превышать 10 секунд.

import aiohttp
import asyncio
import time


async def get_request(session):
    async with session.get('http://httpbin.org/delay/3') as response:
        return await response.text()


async def get_multiple_requests():
    async with aiohttp.ClientSession() as session:
        tasks = [get_request(session) for _ in range(100)]
        return await asyncio.gather(*tasks)


async def main():
    responses = await get_multiple_requests()
    for response in responses:
        print(response)


if __name__ == "__main__":
    start = time.time()
    asyncio.run(main())
    end = time.time()
    print("Time taken:", end - start)
