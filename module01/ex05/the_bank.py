
class Account(object):
    ID_COUNT = 1
    def __init__(self, name, **kwargs):
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
    def transfer(self, amount):
        self.value += amount

class Bank(object):
    """The bank"""
    def __init__(self):
        self.accounts = []
    def add(self, new_account):
        """ Add new_account in the Bank
        @new_account: Account() new account to append
        @return True if success, False if an error occured
        """
        
        # test if new_account is an Account() instance and if
        # it can be appended to the attribute accounts
        if(isinstance(new_account, Account)):
            self.accounts.append(new_account)
            return True
        
        else: return False
    def is_corrupted(self, account):
        """Check if an account is corrupted based on 42 rules."""
        if not isinstance(account, Account):
            return True

        attrs = account.__dict__
        if len(attrs) % 2 == 0:
            return True
        
        if any(attr.startswith("b") for attr in attrs):
            return True
        
        if not any(attr.startswith("zip") or attr.startswith("addr") for attr in attrs):
            return True

        if not all(k in attrs for k in ("name", "id", "value")):
            return True

        if not isinstance(account.name, str):
            return True

        if not isinstance(account.id, int):
            return True

        if not isinstance(account.value, (int, float)):
            return True

        return False
    
    def transfer(self, origin, dest, amount):
        """" Perform the fund transfer
        @origin: str(name) of the first account
        @dest: str(name) of the destination account
        @amount: float(amount) amount to transfer
        @return True if success, False if an error occured
        """
        if not isinstance(amount, (int, float)) or amount < 0:
            return False
        s = None
        r = None
        for acc in self.accounts:
            if acc.id == origin or acc.name == origin:
                s = acc
        for acc in self.accounts:
            if acc.id == dest or acc.name == dest:
                r = acc
        

        if s is None or r is None:
            return False

        if self.is_corrupted(s) or self.is_corrupted(r):
            return False

        if s.value < amount:
            return False

        s.value -= amount
        r.transfer(amount)
        return True
    
    def fix_account(self, name):
        """ fix account associated to name if corrupted
        @name: str(name) of the account
        @return True if success, False if an error occured
        """
        acc = None
        for x in self.accounts:
            if x.id == name or x.name == name:
                acc = x
        if acc is None:
            return False
        if not isinstance(acc, Account):
            return False

        to_remove = [k for k in vars(acc).keys() if k.startswith("b")]
        for k in to_remove:
            try:
                delattr(acc, k)
            except Exception:
                pass

        if not hasattr(acc, "value") or not isinstance(acc.value, (int, float)):
            if hasattr(acc, "value"):
                try:
                    val = float(acc.value)
                    acc.value = int(val) if val.is_integer() else val
                except Exception:
                    acc.value = 0
            else:
                acc.value = 0

        if not any(k.startswith("zip") or k.startswith("addr") for k in vars(acc).keys()):
            acc.addr = ""

        attrs = list(vars(acc).keys())
        if len(attrs) % 2 == 0:
            fix_name = "_fix"
            i = 0
            while fix_name in vars(acc):
                i += 1
                fix_name = f"_fix{i}"
            setattr(acc, fix_name, True)
        return not self.is_corrupted(acc)