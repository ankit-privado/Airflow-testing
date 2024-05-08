from airflow.models import BaseOperator
from airflow.utils.decorators import apply_defaults

class CustomOperator(BaseOperator):
    @apply_defaults
    def __init__(self, my_parameter, *args, **kwargs):
        super(CustomOperator, self).__init__(*args, **kwargs)
        self.parameter = parameter
      
    def execute(self, context):
        s3.upload(context.firstName)
      
class main:
    dag = DAG(
        'dag',
        default_args=default_args,
        description='DAG with CustomOperator'
    )
      
    custom_task = CustomOperator(
        task_id='cutom_task',
        parameter = "something",
        html_content=firstName,
        dag=dag,
    )