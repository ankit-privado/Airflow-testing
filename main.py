from airflow import DAG
from airflow.operators import EmailOperator
from datetime import datetime

class main:
    default_args = {
        'owner': 'airflow',
        'start_date': datetime(2024, 4, 1)
    }
    
    dag = DAG(
        'email_dag',
         default_args=default_args,
         description='DAG with EmailOperator',
         schedule_interval='@once'
    )
      
    email_content = "Hello"
      
    email_task = MySqlOperator(
        task_id='send_email',
        to='recipient@example.com',
        subject='Email Notification',
        html_content=email_content,
        dag=dag
    )