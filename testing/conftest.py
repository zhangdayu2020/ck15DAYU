import pytest


@pytest.fixture()
def login():
    print( "login" )
    yield ["tom", "28years old"]
    print( "logout" )


@pytest.fixture()
def conn():
    print( "conn" )
