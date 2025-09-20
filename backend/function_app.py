import azure.functions as func
import datetime
import json
import logging

app = func.FunctionApp(http_auth_level=func.AuthLevel.ANONYMOUS)

@app.route(route="auth/sign-in", methods=[func.HttpMethod.POST])
def sign_in(req: func.HttpRequest) -> func.HttpResponse:
    logging.info('Received sign-in request')

    client_code = req.params.get('client-code')

    if client_code:
        # Validate the client code if it valid and exists in mock db. If not valid, return 401
        
        # If valid, generate user a jwt token and return it to them
        return func.HttpResponse(f"Get token for client code: {client_code}")
    else:
        return func.HTTP(
             "Invalid request",
             status_code=400
        )

@app.route(route="stocks", methods=[func.HttpMethod.GET])
def stocks(req: func.HttpRequest) -> func.HttpResponse:
    logging.info('Received stocks request.')

    # Check from cache first 
    
    # If user's stock does not exist in cache then get from DB
    
    # Get from DB then update cache to improve performance for next time 
    # (cache should expired after midnight or when the stock data is updated in DB)
    return func.HttpResponse(f"This http triggered function successfully")