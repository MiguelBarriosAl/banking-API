# Banking-API
To build an internal API for a financial institution using Python.
The task is to build the basic HTTP API for one of those banks! Imagine you are designing a backend API for
bank employees.

# Django Framework
## Model
The database model consists of a transfer table and a user table.
The user table consists of the nexts fields:

 - name = Customer name
 - bank_account = Customer's bank account
 - balance = Amount of money in the user's account
 - created_at = User creation date
 - updated = User update date

The transfers table consists of the nexts fields:

 - receiving_account = Account number to which the bank transfer has been made
 - bank_account = Bank account that made the transfer
 - balance = Amount of money that has been transferred
 - created_at = User creation data transfer
 - updated = User update transfer

# Installation

1. Install python==3.9

    `sudo apt update`
    
    `sudo apt install python3.9`
    
    `python --version`


2. Clone the repository

    `git clone https://github.com/MiguelBarriosAlvarez/Banking-API.git`


4. Install the virtualenv:

    `sudo apt-get install python3-pip`

    `sudo pip3 install virtualenv`
    
    `virtualenv venv `
    
    `source venv/bin/activate`


5. Install requirements

    `pip install -r requirements.txt`

6. Run the API

    `python3 manage.py runserver`

# HTTP requests

- Create new user

   `POST http://127.0.0.1:8000/api/balance/`

  `{
    "name": "Pedro Perez",
    "bank_account": 1244124312312,
    "balance": 9000
   }`

- Show user data

   `GET http://127.0.0.1:8000/api/user/<int:bank_account>`

- Make new transfer
   
   `POST http://127.0.0.1:8000/api/transfer/`

   `{
       "bank_account": "1244124312312",
       "receiving_account": 123446452342,
       "balance": 200
   }`

- Show transfers from a bank account

   `GET http://127.0.0.1:8000/api/user/<int:bank_account>`
