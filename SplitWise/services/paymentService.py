import sys
sys.path.insert(0, "../models")
from payment import Payment

class PaymentService:
    paymentMap = {}
    userPaymentMap = {}

    @staticmethod
    def addPayment(amount, paidBy, paidTo):
        payment = Payment(amount, paidBy, paidTo)
        PaymentService.paymentMap[payment.id] = payment

        if paidBy in PaymentService.userPaymentMap:
            if paidTo in PaymentService.userPaymentMap[paidBy]:
                netPaidAmount = PaymentService.userPaymentMap[paidBy][paidTo]
                netPaidAmount += amount
                PaymentService.userPaymentMap[paidBy][paidTo] = netPaidAmount
                PaymentService.userPaymentMap[paidTo][paidBy] = netPaidAmount * -1
            else:
                if paidTo not in PaymentService.userPaymentMap:
                    PaymentService.userPaymentMap[paidTo] = {}
                PaymentService.userPaymentMap[paidBy][paidTo] = amount
                PaymentService.userPaymentMap[paidTo][paidBy] = amount * -1
        else:
            if paidTo not in PaymentService.userPaymentMap:
                PaymentService.userPaymentMap[paidTo] = {}
            PaymentService.userPaymentMap[paidBy] = {}
            PaymentService.userPaymentMap[paidBy][paidTo] = amount
            PaymentService.userPaymentMap[paidTo][paidBy] = amount * -1
        
        return payment

    @staticmethod
    def fetchPaymentBalance(myUserId, forUserID):
        if myUserId in PaymentService.userPaymentMap:
            return PaymentService.userPaymentMap[myUserId].get(forUserID,0.0)
        return 0.0