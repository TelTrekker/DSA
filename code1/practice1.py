#Variable Assignment
name = 'kristel'
age = 50
bank_balance = 0.1
blood_type = 'Ab'
birthday = 'bukas'
address = 'larlin'
favorite_book = "dora"
todo = ['clean', "laundry"]
gender = ["male", "semi"]
family = {
    "mother" : "alicia",
    "father" : {
        age : 50,
        "mother" : "jhon"
    },
    'siblings': ['jay','thomas']
}

#Local and global variable assignment
def local():
  #name ='ramos'
  name = 'kadyut' #public
  _name = 'chris' #protected
  __name = 'chris' #private
  
  _age = age + 1
  
  #first 
  #bank_balance=+30000 #as if bank_balance = bank_balance + 30000
  _bank_balance = bank_balance
  #_bank_balance = _bank_balance + 30000
  _bank_balance += 30000
  print('first:', _bank_balance)
  
  #second
  _bank_balance = bank_balance
  _bank_balance =+ 30000
  print('second:', _bank_balance)
  
  print(name)
  print(_name)
  print(__name)
  print(age)
  print(_age)
  print('bank_balance', bank_balance)
  print('bank_balance', _bank_balance)

local()

def check_age(age):
  if age >= 18:
    print('Old enough')
  else:
    print('FBI')

check_age(45)

def check_grades(grade):
    if grade >= 95:
       print('with honors')
    elif grade >= 90:
       print('pass')
    elif grade >= 85:
       print('saks lang')
    elif grade >= 80:
       print('fail')
    elif grade >= 75:
       print('drop')
    else:
       print('drop')

check_grades()
check_grades(85)
check_grades(90)
check_grades(93)
check_grades(100)
