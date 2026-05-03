"""
Test script for bank account fixing and transfer functionality.
"""

from the_bank import Account, Bank


def main() -> None:
    """Run fix and transfer test."""
    bank = Bank()
    bank.add(Account(
        'Smith Jane',
        zip='911-745',
        value=1000.0,
        ref='1044618427ff2782f0bbece0abd05f31'
    ))
    bank.add(Account(
        'William John',
        zip='100-064',
        value=6460.0,
        ref='58ba2b9954cd278eda8a84147ca73c87',
        info=None
    ))

    if not bank.transfer('William John', 'Smith Jane', 1000.0):
        print('Failed - attempting to fix accounts')
        bank.fix_account('William John')
        bank.fix_account('Smith Jane')

    if bank.transfer('William John', 'Smith Jane', 1000.0):
        print('Success')
    else:
        print('Failed')


if __name__ == "__main__":
    main()
