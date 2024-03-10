from fastapi import FastAPI
from starlette.responses import StreamingResponse
from config import Config
import aio_pika

app = FastAPI()

async def get_rabbitmq_connection():
    return await aio_pika.connect_robust(host=Config.RABBITMQ_HOST, port=Config.RABBITMQ_PORT, login=Config.RABBITMQ_USER, password=Config.RABBITMQ_PASSWD)

async def rabbitmq_consumer(queue_name: str):
    connection = await get_rabbitmq_connection()
    async with connection:
        channel = await connection.channel()
        await channel.set_qos(prefetch_count=1)
        queue = await channel.declare_queue(queue_name,)
        async for message in queue:
            async with message.process():
                yield f"data: {message.body.decode()}\n\n"

@app.get("/tasks/{task_id}/stream")
async def stream(task_id: str):
    return StreamingResponse(rabbitmq_consumer(task_id), media_type="text/event-stream")


if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host=Config.HOST, port=Config.PORT)

