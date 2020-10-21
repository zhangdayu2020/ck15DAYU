import time


def test_case1(login):
    print( "test_case1" )
    print( login )


def test_case2(conn):
    print( "test_case2" )
    print( conn )


import pytest


@pytest.mark.usefixtures( "login" )
def test_case3():
    sleep( 3 )
    print( "test_case3" )
    # print(login)
