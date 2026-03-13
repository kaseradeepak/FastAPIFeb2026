from fastapi import FastAPI
from fastapi.responses import StreamingResponse
import time

app = FastAPI()

def text_stream():
    for i in range(100):
        yield f"Message {i}\n"
        time.sleep(1)

@app.get("/stream")
async def stream():
    return StreamingResponse(text_stream(), media_type="text/event-stream")
