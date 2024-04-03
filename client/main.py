import uvicorn
import asyncio
import aiohttp
import random
from loguru import logger
from fastapi import FastAPI
from datetime import datetime
from config import settings

HOST=settings.HOST
PORT=settings.PORT
servise_url = settings.SERVICE_URL

app = FastAPI()
logger.add('parser.log', format='%(asctime)s - [%(threadName)s] - %(message)s', level='DEBUG', retention="2 days")


async def send_request(request_id, delay, semaphore : asyncio.Semaphore):
    current_thread = asyncio.current_task()
    current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    
    try:
        async with semaphore:
            
            data = {
                "id": request_id,
                "delay": delay
            }
            async with aiohttp.ClientSession() as session:
                async with session.post(servise_url, json=data) as response:
                    logger.info(f"Request {request_id}, Thread: {current_thread} Delay: {delay} seconds. Time: {current_time}")
            await asyncio.sleep(1)
    except Exception as e:
        logger.error('', exc_info=e)

# Обработчик POST запросов
@app.post("/send_requests/")
async def send_requests(connection_count: int, connection_value: int, delay_range: int):
    tasks = []
    semaphore = asyncio.Semaphore(connection_count)
    try:
        for i in range(connection_value):
            delay = random.randint(1, delay_range)
            id = random.randint(1, 1000000)
            task = asyncio.create_task(send_request(id, delay, semaphore))
            tasks.append(task)
        
        # Ожидаем завершения всех задач
        await asyncio.gather(*tasks)

        return {"message": "Requests sent successfully"}
    except Exception as exc:
        return {"asyncAnswer": exc}


if __name__ == "__main__":
    uvicorn.run(app="main:app", reload=True, host=HOST, port=PORT)
