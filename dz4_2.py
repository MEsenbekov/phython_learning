class SavingAccaunt:
    pass
class CheckingAccaunt:
    pass
class Stock:
    pass
class Bond:
    pass
class BankAccaunt(SavingAccaunt, CheckingAccaunt):
    pass
class Security(Stock, Bond):
    pass
class RealEstate:
    pass
class Insurableltem(BankAccaunt, RealEstate):
    pass
class Asset(BankAccaunt, Security, RealEstate):
    pass
class InteresBearingltem(Security, BankAccaunt):
    pass