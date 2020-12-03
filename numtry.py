class Numtry:

    def __init__(self, number):
        self.secretNumber = number
        self.recordNums = []
        self.recordUpdowns = []
        self.isfinished=False
        print(self.secretNumber)

    # Record used numbers and Compare input number with secret number
    def numtry(self, num):
        self.recordNums.append(num)
        if num != self.secretNumber:
            if num < self.secretNumber:
                return 0
            return 1
        self.isfinished=True

        return 2

    # Show recording numbers
    def getRecordNums(self):
        recordNum = ''
        for i in self.recordNums:
            recordNum += (str(i))
        return recordNum

    # Record status, input number with Up and Down
    def updownTry(self, updown):
        self.recordUpdowns.append(updown)

    # Show recording status
    def getRecordUpdown(self):
        recordUpdown = '*** Up & Down Record ***\n'
        for i in self.recordUpdowns:
            recordUpdown += (str(i))
        return recordUpdown


    def finished(self):
        if self.isfinished == True:
            return True
        else:
            return False