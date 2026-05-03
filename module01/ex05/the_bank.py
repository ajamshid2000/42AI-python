
"""
Bank and Account classes for managing bank accounts and transfers.
"""

from typing import List, Union, Any


class Account:
    """
    A bank account class.

    Attributes:
        id: Unique account ID.
        name: Account name.
        value: Account balance.
    """
    ID_COUNT = 1

    def __init__(self, name: str, **kwargs: Any) -> None:
        """
        Initialize an Account.

        Args:
            name: Account name.
            **kwargs: Additional attributes.

        Raises:
            AttributeError: If name is not str or value is negative.
        """
        self.__dict__.update(kwargs)
        self.id = self.ID_COUNT
        Account.ID_COUNT += 1
        self.name = name
        if not hasattr(self, 'value'):
            self.value = 0
        if self.value < 0:
            raise AttributeError("Attribute value cannot be negative.")
        if not isinstance(self.name, str):
            raise AttributeError("Attribute name must be a str object.")

    def transfer(self, amount: Union[int, float]) -> None:
        """
        Transfer amount to this account.

        Args:
            amount: Amount to add.
        """
        self.value += amount


class Bank:
    """
    A bank class managing accounts and transfers.
    """

    def __init__(self) -> None:
        """Initialize the bank."""
        self.accounts: List[Account] = []

    def add(self, new_account: Account) -> bool:
        """
        Add a new account to the bank.

        Args:
            new_account: The account to add.

        Returns:
            True if added successfully, False otherwise.
        """
        if isinstance(new_account, Account):
            self.accounts.append(new_account)
            return True
        return False

    def is_corrupted(self, account: Account) -> bool:
        """
        Check if an account is corrupted based on specific rules.

        Args:
            account: The account to check.

        Returns:
            True if corrupted, False otherwise.
        """
        if not isinstance(account, Account):
            return True

        attrs = account.__dict__
        if len(attrs) % 2 == 0:
            return True

        if any(attr.startswith("b") for attr in attrs):
            return True

        if not any(attr.startswith("zip") or attr.startswith("addr") for attr in attrs):
            return True

        required = {"name", "id", "value"}
        if not required.issubset(attrs):
            return True

        if not isinstance(account.name, str):
            return True

        if not isinstance(account.id, int):
            return True

        if not isinstance(account.value, (int, float)):
            return True

        return False

    def transfer(self, origin: Union[str, int], dest: Union[str, int], amount: Union[int, float]) -> bool:
        """
        Perform a fund transfer between accounts.

        Args:
            origin: Origin account name or ID.
            dest: Destination account name or ID.
            amount: Amount to transfer.

        Returns:
            True if successful, False otherwise.
        """
        if not isinstance(amount, (int, float)) or amount < 0:
            return False

        sender = None
        receiver = None
        for acc in self.accounts:
            if acc.id == origin or acc.name == origin:
                sender = acc
            if acc.id == dest or acc.name == dest:
                receiver = acc

        if sender is None or receiver is None:
            return False

        if self.is_corrupted(sender) or self.is_corrupted(receiver):
            return False

        if sender.value < amount:
            return False

        sender.value -= amount
        receiver.transfer(amount)
        return True

    def fix_account(self, name: Union[str, int]) -> bool:
        """
        Fix a corrupted account.

        Args:
            name: Account name or ID.

        Returns:
            True if fixed successfully, False otherwise.
        """
        acc = None
        for x in self.accounts:
            if x.id == name or x.name == name:
                acc = x
        if acc is None:
            return False
        if not isinstance(acc, Account):
            return False

        # Remove attributes starting with 'b'
        to_remove = [k for k in vars(acc).keys() if k.startswith("b")]
        for k in to_remove:
            try:
                delattr(acc, k)
            except Exception:
                pass

        # Fix value
        if not hasattr(acc, "value") or not isinstance(acc.value, (int, float)):
            if hasattr(acc, "value"):
                try:
                    val = float(acc.value)
                    acc.value = int(val) if val.is_integer() else val
                except Exception:
                    acc.value = 0
            else:
                acc.value = 0

        # Add addr if missing
        if not any(k.startswith("zip") or k.startswith("addr") for k in vars(acc).keys()):
            acc.addr = ""

        # Ensure odd number of attributes
        attrs = list(vars(acc).keys())
        if len(attrs) % 2 == 0:
            fix_name = "_fix"
            i = 0
            while hasattr(acc, fix_name):
                i += 1
                fix_name = f"_fix{i}"
            setattr(acc, fix_name, True)

        return not self.is_corrupted(acc)