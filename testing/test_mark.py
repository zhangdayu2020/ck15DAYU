import pytest


@pytest.mark.login
def test_login1():
    print( "login1" )


@pytest.mark.login
def test_login2():
    print( "login2" )


@pytest.mark.search
def test_search1():
    print( "test_search1" )


@pytest.mark.search
def test_search2():
    print( "test_search2" )
