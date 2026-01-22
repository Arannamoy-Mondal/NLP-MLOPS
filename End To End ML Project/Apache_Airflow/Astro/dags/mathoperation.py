from airflow import DAG
from airflow.operators.python import PythonOperator
from datetime import datetime 


def initial_number():
    print("Initial Number")

def add():
    print("add 5")

def multiply():
    print("multiple 5")

def subtract():
    print("subtract 3")

def compute():
    print("compute")

with DAG("math_operations",start_date=datetime(2025,10,10),schedule="@daily") as dag:
    initial=PythonOperator(task_id="initial_number",python_callable=initial_number)
    ad=PythonOperator(task_id="add",python_callable=add)
    mul=PythonOperator(task_id="multiply",python_callable=multiply)
    sub=PythonOperator(task_id="subtract",python_callable=subtract)
    com=PythonOperator(task_id="compute",python_callable=compute)
    initial>>ad>>mul>>sub>>com