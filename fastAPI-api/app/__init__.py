from fastapi import FastAPI

from .settings.db import Model, engine


def create_app():
    """
        Creating and configuring our app
    """

    #Creating Database
    Model.metadata.create_all(bind=engine)

    #Creating the API app
    app = FastAPI()

    from .pessoa.routes import route as pessoa_route

    app.include_router(
        pessoa_route,
        prefix='/pessoa',
        responses={404: {"description": "not found"}}
    )

    return app