import json
import os
import random
import sqlite3
import string

from django.http import HttpResponse, request
from django.conf import settings

#Constants
ROOT_DIR = settings.BASE_DIR + "/test_app"
# Create your views here.
def hello(request):
    return HttpResponse("Hello")

def gen_password(request):
    length = request.GET.get('length', '10')
    try:
        val = int(length)
        if (val > 0):
            if (8 <= val <= 24):
                return HttpResponse(''.join(
                    [
                        random.choice(string.ascii_lowercase)
                        for _ in range(val)
                    ])
                )
            else:
                return HttpResponse("Length should be in the range from 8 to 24.")
        else:
            return HttpResponse("Length should be bigger than 0.")
    except ValueError:
        return HttpResponse("Length should be a number!")

def get_unique_firstnames(request):
    query = 'SELECT DISTINCT FirstName FROM customers'
    records = execute_query(query)
    return HttpResponse(str(records))

def get_filtered_by_state_and_city(request):
    state = request.GET.get('state', 'AB')
    city = request.GET.get('city', 'Edmonton')
    query = f'SELECT * FROM customers WHERE State = "{state}" AND City = "{city}"'
    records = execute_query(query)
    return HttpResponse(str(records))

def get_revenue(request):
    query = 'SELECT SUM(UnitPrice * Quantity) FROM invoice_items'
    records = execute_query(query)
    return HttpResponse(str(records))

def get_invoices(request):
    country = request.GET.get('country')
    city = request.GET.get('city')
    if country is not None or city is not None:
        query = f'SELECT * FROM invoices WHERE BillingCountry = "{country}" COLLATE NOCASE OR ' \
            f'BillingCity = "{city}" COLLATE NOCASE'
    else:
        query = f'SELECT * FROM invoices'
    records = execute_query(query)
    items = []
    for row in records:
        items.append({'InvoiceDate': row[2], 'BillingAddress': row[3],
                      'BillingCity': row[4], 'BillingCountry': row[5],'Total': row[8]})
    json_records = json.dumps(items)
    return HttpResponse(str(json_records))

def execute_query(query):
    db_path = os.path.join(ROOT_DIR, 'chinook.db')
    print(db_path)
    conn = sqlite3.connect(db_path)
    cur = conn.cursor()
    cur.execute(query)
    records = cur.fetchall()
    return records
