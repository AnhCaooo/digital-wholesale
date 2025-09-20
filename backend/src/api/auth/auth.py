import azure.functions as func
import logging
import json
from ...models import CLIENT_DB

def handle_sign_in(req: func.HttpRequest) -> func.HttpResponse:
    """Handle when user sends a sign-in request. 
    Due to this is an assignment, not a production app, so does not include any actions with real DB, jwt token generation, etc. 
    Therefore, if client_code is valid (exists in mock db), just return it as access_token to web client.
    
    **For PROD level**: once user sends a sign-in request, we need to handle the client_code by checking salted hash in DB, or use 3rd party such as Auth0, Supabase, Keycloak. 
    And response should contains access_token (JWT_TOKEN) and refresh_token so that web client could use to refresh session when access_token expired

    Args:
        req (func.HttpRequest): An HTTP request object.

    Returns:
        func.HttpResponse: An HTTP request object.
    """
    logging.info('Received sign-in request')
    
    body = req.get_json()
    client_code = body.get("client_code")
    if client_code:
        # Validate the client code if it valid and exists in mock db. If not valid, return 401
        if any(client.code == client_code for client in CLIENT_DB):
            logging.info(f"Client code {client_code} is valid")
            return func.HttpResponse(
                body=json.dumps({
                    "access_token": client_code,
                    }),
                status_code=200
            )
        else:
            logging.warning(f"Client code is invalid: {client_code}")
            return func.HttpResponse(
                body=json.dumps({"message": "Invalid client code"}),
                status_code=401
            )
    else:
        return func.HttpResponse(
            body=json.dumps({"message": "Invalid request"}),
            status_code=400
        )