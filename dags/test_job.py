from datetime import datetime
from airflow.decorators import dag, task
from airflow.operators.bash import BashOperator


@task()
def start(*args, **kwargs) -> bool:
    t = BashOperator(
        task_id='test_start',
        bash_command='echo start',
    )
    return True


@task()
def echo(*args, **kwargs) -> bool:
    t = BashOperator(
        task_id='test_echo',
        bash_command='echo hello world',
    )
    return True


@task()
def finalize(result: bool, *args, **kwargs) -> bool:
    if result:
        t = BashOperator(
            task_id='test_finalize',
            bash_command='echo finich',
        )
    return True


@dag(
    start_date=datetime(2022, 3, 27),
    schedule_interval=None,
    catchup=False,
    tags=['taskflow api']
)
def test_job():
    args = start()
    result = echo(args)
    a = finalize(result)


test_dag = test_job()
