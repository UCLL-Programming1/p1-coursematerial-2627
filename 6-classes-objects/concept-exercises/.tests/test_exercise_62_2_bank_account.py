from p1_util.tests.test_util import call_function, run_script

import pytest

def test_function(pytestconfig):
    account = call_function(__file__, "BankAccount", ["James"])
    assert account.owner == "James", f"Expected owner 'James', got {account.owner!r}"
    assert account.balance == 0, f"A new account should start with balance 0, got {account.balance!r}"

def test_function_deposit(pytestconfig):
    account = call_function(__file__, "BankAccount", ["Alice"])
    account.deposit(100)
    assert account.balance == 100, f"Expected balance 100 after depositing 100, got {account.balance!r}"
    account.deposit(50)
    assert account.balance == 150, f"Expected balance 150 after depositing 50 more, got {account.balance!r}"

def test_function_withdraw(pytestconfig, capsys):
    account = call_function(__file__, "BankAccount", ["Alice"])
    account.deposit(100)

    account.withdraw(30)
    assert account.balance == 70, f"Expected balance 70 after withdrawing 30, got {account.balance!r}"
    output = capsys.readouterr().out
    assert output == "", f"A successful withdrawal should not print anything, got {output!r}"

    # withdrawing exactly the remaining balance should be allowed
    account.withdraw(70)
    assert account.balance == 0, f"Expected balance 0 after withdrawing the full balance, got {account.balance!r}"

def test_function_insufficient_funds(pytestconfig, capsys):
    account = call_function(__file__, "BankAccount", ["Bob"])
    account.deposit(50)

    account.withdraw(51)
    output = capsys.readouterr().out
    assert output == "Insufficient funds\n", f"Expected 'Insufficient funds' to be printed, got {output!r}"
    assert account.balance == 50, f"The balance should stay unchanged after a failed withdrawal, got {account.balance!r}"
