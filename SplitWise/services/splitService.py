import sys
sys.path.insert(0,"../models")
from split import Split

class SplitService:
    splitMap = {}
    userBalanceMap = {}

    @staticmethod
    def addSplitEntry(billId, paidBy, sharedBy, sharedPercentage, dueAmount):

        split = Split(billId, paidBy,sharedBy, sharedPercentage, dueAmount)
        SplitService.splitMap[billId] = split

        if paidBy in SplitService.userBalanceMap:
            if sharedBy in SplitService.userBalanceMap[paidBy]:
                dueBalance = SplitService.userBalanceMap[paidBy][sharedBy]
                dueBalance += dueAmount
                SplitService.userBalanceMap[paidBy][sharedBy] = dueBalance
                SplitService.userBalanceMap[sharedBy][paidBy] = dueBalance * -1
            else:
                if sharedBy not in SplitService.userBalanceMap:
                    SplitService.userBalanceMap[sharedBy] = {}
                SplitService.userBalanceMap[paidBy][sharedBy] = dueAmount
                SplitService.userBalanceMap[sharedBy][paidBy] = dueAmount * -1
        else:
            SplitService.userBalanceMap[paidBy] = {}
            if sharedBy not in SplitService.userBalanceMap:
                SplitService.userBalanceMap[sharedBy] = {}
            SplitService.userBalanceMap[paidBy][sharedBy] = dueAmount
            SplitService.userBalanceMap[sharedBy][paidBy] = dueAmount * -1

        # if sharedBy in SplitService.userBalanceMap:
        #     if paidBy in SplitService.userBalanceMap[sharedBy]:
        #         dueBalance = SplitService.userBalanceMap[sharedBy][paidBy]
        #         dueBalance -= dueAmount
        #         SplitService.userBalanceMap[sharedBy][paidBy] = dueBalance
        #     else:
        #         SplitService.userBalanceMap[sharedBy][paidBy] = -dueAmount
        # else:
        #     SplitService.userBalanceMap[sharedBy][paidBy] = -dueAmount

        return split

    @staticmethod
    def fetchDueBalance(myUserId, forUserID):
        if myUserId in SplitService.userBalanceMap:
            return SplitService.userBalanceMap[myUserId].get(forUserID,0.0)

        return 0.0