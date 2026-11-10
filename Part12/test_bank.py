import pytest

from bank import BankAccount


@pytest.fixture
def account():
    return BankAccount("Isam", 100)


def test_starting_balance(account):
    assert account.balance == 100


def test_default_balance_is_zero():
    assert BankAccount("Ali").balance == 0


def test_negative_starting_balance():
    with pytest.raises(ValueError):
        BankAccount("Ali", -10)


def test_deposit_increases_balance(account):
    account.deposit(50)
    assert account.balance == 150


@pytest.mark.parametrize("amount", [0, -20])
def test_invalid_deposit(account, amount):
    with pytest.raises(ValueError):
        account.deposit(amount)


def test_withdraw_decreases_balance(account):
    account.withdraw(30)
    assert account.balance == 70


def test_withdraw_entire_balance(account):
    account.withdraw(100)
    assert account.balance == 0


def test_overdraft_not_allowed(account):
    with pytest.raises(ValueError):
        account.withdraw(101)
    assert account.balance == 100  # balance unchanged after failed withdrawal


@pytest.mark.parametrize("amount", [0, -5])
def test_invalid_withdraw(account, amount):
    with pytest.raises(ValueError):
        account.withdraw(amount)


def test_str(account):
    assert str(account) == "Isam: 100"
