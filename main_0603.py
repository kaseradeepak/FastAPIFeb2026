from fastapi import FastAPI, Request
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

# This middleware will get triggered for every HTTP API request coming to our fastAPI server.
@app.middleware("http")
async def first_middleware_function(request: Request, call_next):
    # Phase-1 : get the request (Before processing)
    print("First Middleware - Before processing")

    # Phase-2 : Send the request to the server (Send for processing)
    response = await call_next(request) # await - make a non blocking call to the request.

    # Phase-3 : Get the response (After processing)
    print("First Middleware - After processing")

    return response

@app.middleware("http")
async def second_middleware_function(request: Request, call_next):
    # Phase-1 : get the request (Before processing)
    print("Second Middleware - Before processing")

    # Phase-2 : Send the request to the server (Send for processing)
    response = await call_next(request) # await - make a non blocking call to the request.

    # Phase-3 : Get the response (After processing)
    print("Second Middleware - After processing")

    return response

@app.get("/sample")
async def sample():
    asyncio.sleep(10)
    return {"message" : "This is the sample API."}
