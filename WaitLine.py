import time

class WaitLine():
    def __init__(self, LineLength, Speed, LineElement, Progress):
        self.LineLength = LineLength
        self.Speed = Speed
        self.LineElement = LineElement
        self.Progress = Progress
    # set the length of line
    def SetLength(self, LineLength):
        if LineLength == 0:
            print("It has to be bigger than 0 !!")
            return False
        else:
            self.LineLength = LineLength
            return True
    # set the speed of line
    def SetSpeed(self, Speed):
        if Speed == 0:
            print("It has to be bigger than 0 !!")
            return False
        else:
            self.Speed = Speed
            return True
    # print out "=====>====" dynamically
    def WaitLineEffect(self):
        LineElement = self.LineElement
        Progress = self.Progress
        Count = 0
        BlankElement = ' '
        Blank = ''
        while(Count != self.LineLength):
            Line = ''
            for i in range(self.LineLength):
                if i == Count:
                    Line = Line + Progress
                else:
                    Line = Line + LineElement
            print(Line, end = '\r')
            Blank = Blank + BlankElement
            Count += 1
            if Count == self.LineLength:
                print(Blank, end = '\r')
            time.sleep(self.Speed)
            


# print(1 + 2) 
# print("Test")