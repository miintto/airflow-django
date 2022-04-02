from datetime import datetime

from airflow import DAG
from airflow.operators.bash import BashOperator

from operators.django_operator import DjangoOperator


with DAG(
    dag_id="djnago_operator",
    default_args={"retries": 1},
    schedule_interval=None,
    start_date=datetime(2022, 1, 1),
    catchup=False,
) as dag:
    task_init = BashOperator(
        task_id="initialize",
        bash_command="echo start~!",
        dag=dag
    )
    task_version = DjangoOperator(
        task_id="django_version",
        django_task="--version",
        dag=dag,
    )
    task_migration = DjangoOperator(
        task_id="django_showmigration",
        django_task="showmigrations",
        dag=dag,
    )
    task_fin = BashOperator(
        task_id="finalize",
        bash_command="echo finish~!",
        dag=dag
    )


task_init >> task_version >> task_migration >> task_fin
