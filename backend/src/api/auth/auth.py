import azure.functions as func
import logging

def handle_sign_in(req: func.HttpRequest) -> func.HttpResponse:
    logging.info('Received sign-in request')

    client_code = req.params.get('client-code')

    if client_code:
        # Validate the client code if it valid and exists in mock db. If not valid, return 401
        
        # If valid, generate user a jwt token and return it to them
        return func.HttpResponse(f"Get token for client code: {client_code}")
    else:
        return func.HttpResponse(
             "Invalid request",
             status_code=400
        )