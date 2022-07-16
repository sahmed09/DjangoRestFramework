## Accounting APIs
```
http://54.251.167.179:8000/api/accounting/
```

### TransactionGraph API:
http://54.251.167.179:8000/api/accounting/transaction_graph_api/?start_date=2021-10-20&end_date=2021-10-28&interval=monthly&transaction_type=debit
<br> Filter Options: start_date, end_date, interval (daily, monthly, yearly), transaction_type (debit, credit)
```
Send GET request:
http://54.251.167.179:8000/api/accounting/transaction_graph_api/?start_date=2021-10-20&end_date=2021-10-28&interval=monthly&transaction_type=debit
{
    "count": 1,
    "next": null,
    "previous": null,
    "results": [
        {
            "date": "2021-10-28",
            "total": 50000.00
        }
    ]
}
```

````
Models:
TransactionUser : Selects the user of a transaction
OrderTransactionTrigger: For a specific shop, creates a transaction trigger based on order status change
    (like from pending to confirmed) and from whom to whom (like seller to delivery agent) and transaction
    type (debit/credit), resolved or not and amount.
Transaction: Creates automatically using signal (order_transaction_trigger) when an 
    OrderTransactionTrigger is created based on order status change.
````
