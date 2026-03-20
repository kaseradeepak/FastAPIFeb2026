# Background Tasks are used when we want to send the response immediately, but the processing of the request can be done in the background even after sending the response.
# Examples of background tasks - sending email, generating reports/invoices, resolving customer support queries, uploading data to the server ......

# Real_life example -
# 1. We place an order at Amazon
# 2. App shows us the order confirmation.
# 3. In the background: 
#       - Amazon sends notification
#       - Amazon generates invoices
#       - Amazon order delivery process.

from fastapi import FastAPI, BackgroundTasks
import time

app = FastAPI()

def send_notification(message: str):
    print("Sending notification.....")
    time.sleep(1000)
    print("notification sent.")

@app.get("/order")
def place_order(background_tasks: BackgroundTasks):
    print("Place Order started.")
    
    # Payment done -> Order Confirmed.
    
    # Send a confirmation mail to the customer.
    # Send the mail via background tasks.
    background_tasks.add_task(send_notification, "Order placed successfuly.")

    return {"message" : "Order placed"}
