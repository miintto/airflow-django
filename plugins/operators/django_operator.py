import os

from airflow.exceptions import AirflowException
from airflow.providers.docker.operators.docker import DockerOperator


class DjangoOperator(DockerOperator):

    DJANGO_DEFAULT_IMAGE = os.getenv("DJANGO_DEFAULT_IMAGE")

    def __init__(
        self, 
        image: str = None,
        django_task: str = None,
        docker_url: str = "unix://var/run/docker.sock",
        network_mode: str = "bridge",
        auto_remove: bool = True,
        *args,
        **kwargs
    ):
        self.django_task = django_task
        super().__init__(
            image=image or self.DJANGO_DEFAULT_IMAGE,
            docker_url=docker_url,
            network_mode=network_mode,
            auto_remove=auto_remove,
            *args,
            **kwargs
        )

    def execute(self, context):
        if not self.image:
            raise AirflowException(
                "Cannot find the docker image in DjangoOperator. You can set "
                "image by `export DJANGO_DEFAULT_IMAGE=django-app:latest` or "
                "`DjangoOperator(image='django-app:latest', ...)`"
            )
        self.command = f"poetry run python manage.py {self.django_task}"
        super().execute(context)
