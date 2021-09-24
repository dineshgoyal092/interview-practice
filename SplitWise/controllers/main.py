import sys
sys.path.insert(0,"../services")
sys.path.insert(0,"../models")

from billService import BillService
from paymentService import PaymentService
from splitService import SplitService
from userService import UserService
# from bill import Bill


def addUser(name):
    return UserService.addUser(name)


def addBill(amount, paidBy, createdBy, sharedBy, sharedPercentage, dueAmount=None):
    bill = BillService.addBill(amount, paidBy, createdBy)
    if sharedPercentage:
        dueAmount = bill.getAmount() * sharedPercentage / 100
    print(dueAmount)
    SplitService.addSplitEntry(bill.id, paidBy, sharedBy, sharedPercentage, dueAmount)
    return bill

def addPayment(paidBy, paidTo, amount=None):
    if not amount:
        amount = getBalance(paidBy, paidTo) * -1
    if amount > 0.0:
        payment = PaymentService.addPayment(amount, paidBy, paidTo)
        return payment

def getBalance(myUserId, forUserID):
    netDueBalnce = SplitService.fetchDueBalance(myUserId, forUserID)
    netPaidBalance = PaymentService.fetchPaymentBalance(myUserId, forUserID)
    return netPaidBalance + netDueBalnce


u1= addUser("Dinesh")
u2 = addUser("Ramesh")
u3 = addUser("Somesh")
print(u1,u2,u3)

bill1 = addBill(1000.0,u1.id,u1.id,u2.id,50)
print(bill1.__dict__)

bill2 = addBill(2000.0,u1.id,u1.id,u3.id,None, 500)
print(bill2.__dict__)

bill3 = addBill(4000.0,u3.id,u3.id,u1.id,None, 1500)
print(bill3.__dict__)


print(getBalance(u1.id, u2.id))
print(getBalance(u2.id, u1.id))

print(getBalance(u1.id, u3.id))
print(getBalance(u3.id, u1.id))

addPayment(u1.id,u3.id)
addPayment(u2.id,u1.id, 200.0)


print(getBalance(u1.id, u2.id))
print(getBalance(u2.id, u1.id))

print(getBalance(u1.id, u3.id))
print(getBalance(u3.id, u1.id))

    
    
