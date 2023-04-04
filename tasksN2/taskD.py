# Реализовать функцию, которая замеряет время на исполнение 100 запросов к адресу:
# http://httpbin.org/delay/3. Запросы должны выполняться асинхронно.
# Допускается написание вспомогательных функций и использование сторонних библиотек.
# Результат замера времени выводит в консоль.
# Ожидаемое время не должно превышать 10 секунд.

import aiohttp
import asyncio
import time


def get_tasks(session):
    tasks = []  # список запросів
    url = 'http://httpbin.org/delay/3'
    for i in range(1, 100):
        tasks.append(session.get(url=url, ssl=False))  # добавляємо в список запроси (таски)
    return tasks


async def request_asynchronious():  # робимо корутину( тобто асинхронну функцію, задачу)
    async with aiohttp.ClientSession() as session:  # сессія для того щоб відправляти запроси
        tasks = get_tasks(session)  # приймаємо список запросів
        responses = await asyncio.gather(*tasks)  # тут список наших запросів які ми відсилаємо
        for response in responses:
            print(response)


start = time.time()
asyncio.run(request_asynchronious())  # event loop
end = time.time()
print(start - end)


