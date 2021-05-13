# payment_api
## Installation of packages(Flask is used for making REST API calls so you need to have)
### 1) virtualenv (pip3 install virtualenv)
### 2) Then you have to activate virtualenv at the desired location (. venv/bin/activate)
### 3) Flask (pip3 install Flask)
### 4) sqlite3 database for maintaining the account balances and the transaction logs (sudo apt install sqlite3)
### 5) Run the application using (python3 app.py)


## The implemented functions include:
### 1) `Signup` url: http://127.0.0.1:7000/signup
       You need to give phone number(which is unique) along with a password and an initial balance(minimum 5000)
       
       The case where user does not maintain the minimum balance of Rs 5000
   ![Screenshot from 2021-05-12 19-18-01](https://user-images.githubusercontent.com/70585990/117988927-7ddc8f80-b359-11eb-9816-d2b216c35f31.png)
   
       The case where user does maintain the minimum balance of Rs 5000 and the account is successfully created
       
   ![Screenshot from 2021-05-12 19-18-11](https://user-images.githubusercontent.com/70585990/117989652-212da480-b35a-11eb-848c-170818131e8d.png)
   
       The case where an account linked with the given phone number alreday exist
    
   ![Screenshot from 2021-05-12 19-18-18](https://user-images.githubusercontent.com/70585990/117990094-749ff280-b35a-11eb-9b5e-a952175a9ce9.png)

### 2) `Credit` url: http://127.0.0.1:7000/credit
       You need to give your phone number along with the correct password and the amount to be added.
       
       The case where the given phone number does not have a wallet account yet
       
  ![Screenshot from 2021-05-12 19-19-01](https://user-images.githubusercontent.com/70585990/117990446-cd6f8b00-b35a-11eb-9d5e-e350837401d1.png)

       The case where the password of the given phone number is not correct
      
  ![Screenshot from 2021-05-12 19-19-18](https://user-images.githubusercontent.com/70585990/117990955-3fe06b00-b35b-11eb-9db4-4f6b8312cccc.png)
  
       The case where the phone number and password are valid and the specified amount is credited.
       
   ![Screenshot from 2021-05-12 19-53-59](https://user-images.githubusercontent.com/70585990/117991586-d319a080-b35b-11eb-938c-32c5ab64042e.png)
   
### 3) `Debit` url: http://127.0.0.1:7000/debit
       You need to give your phone number along with the correct password and the amount to be debited. The balance after deduction should be greater than or equal to 5000 otherwise the transaction wouldn't be performed.
       
       The case where the balance after transcation becomes less than 5000 so the transaction is not performed.
     
  ![Screenshot from 2021-05-12 19-20-08](https://user-images.githubusercontent.com/70585990/117992042-3c99af00-b35c-11eb-85bf-860a621fc27f.png)
  
       The case where the balance after the transaction is greater than 5000 so the transaction is performed.
    
  ![Screenshot from 2021-05-12 19-20-19](https://user-images.githubusercontent.com/70585990/117992318-779be280-b35c-11eb-9871-dfe45cf8152d.png)
### 4) `Check Balance` url: http://127.0.0.1:7000/checkb
       You need to give the phone number nad the corresponding valid password.
       
   ![Screenshot from 2021-05-12 19-20-38](https://user-images.githubusercontent.com/70585990/117992436-8e423980-b35c-11eb-8882-09b1e89eaa15.png)

## A log table is also created in the project.db database which contains all the transactions which have taken place in the order in which they have taken place. It includes the following  columns (phone number,transaction type(credit/debit),amount,balance before transaction, balance after transaction)

## temp.py could be used to see all the transactions that have taken place.

![Screenshot from 2021-05-13 12-45-04](https://user-images.githubusercontent.com/70585990/118092301-8aa8c400-b3e9-11eb-976d-369eaad8e845.png)





