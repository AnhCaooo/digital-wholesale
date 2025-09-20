import azure.functions as func
import logging


def get_stocks(req: func.HttpRequest) -> func.HttpResponse:
    logging.info('Received stocks request.')

    # Check from cache first 
    
    # If user's stock does not exist in cache then get from DB
    
    # Get from DB then update cache to improve performance for next time 
    # (cache should expired after midnight or when the stock data is updated in DB)
    return func.HttpResponse(f"This http triggered function successfully")