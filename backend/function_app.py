import azure.functions as func
from src.api import auth, stock

app = func.FunctionApp(http_auth_level=func.AuthLevel.ANONYMOUS)


@app.route(route="auth/sign-in", methods=[func.HttpMethod.POST])
def sign_in(req: func.HttpRequest) -> func.HttpResponse:
    return auth.handle_sign_in(req)


@app.route(route="stocks", methods=[func.HttpMethod.GET])
def stocks(req: func.HttpRequest) -> func.HttpResponse:
    return stock.get_stocks(req)
