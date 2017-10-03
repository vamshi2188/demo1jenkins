from nose.tools import eq_

def test_sum():
    eq_(2+2,4)

def test_sum():
    eq_(2+2,5)

def test_sum():
    eq_(2+8,10)

def test_sum():
    eq_(2-2,0)

def test_failing_sum():
    ok_(-2+2,4)

def test_sum():
    eq_(-2-2,-4)
