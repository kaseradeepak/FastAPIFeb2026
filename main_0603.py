from fastapi import FastAPI
import time
import asyncio

app = FastAPI()

# Sync API -> Request comes to the endpoint, processing takes 10 seconds time, during this time server can't process any other request.
@app.get("/sync")
def sync_api():
    print("Sync API call starting.")
    # Make a DB call or make an external API call or Write some data to the file.
    time.sleep(10)
    print("Sync API call completed.")
    return {"message" : "This is an example of Sync API."}

# Async API -> request comes to the endpoint, server takes 10 seconds to process the request, meanwhile server can handle other requests as well, that means server is NOT BLOCKED. 
@app.get("/async")
async def sync_api():
    print("Async API call starting.")
    # Make a DB call or make an external API call or Write some data to the file.
    asyncio.sleep(10)
    print("Async API call completed.")
    return {"message" : "This is an example of Async API."}