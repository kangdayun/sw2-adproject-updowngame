class Updown:

    text_mainDispaly = [
    '''\
    
      □□□□□□□□□□□□
      □□□□□■■□□□□□
      □□□□■■■■□□□□
      □□□■■■■■■□□□
      □□■■■■■■■■□□
      □□□□□■■□□□□□
      □□□□□■■□□□□□
      □□□□□■■□□□□□
      □□□□□■■□□□□□
      □□□□□■■□□□□□\
    ''',

    '''\
    
      □□□□□■■□□□□□
      □□□□□■■□□□□□
      □□□□□■■□□□□□
      □□□□□■■□□□□□
      □□□□□■■□□□□□
      □□■■■■■■■■□□
      □□□■■■■■■□□□
      □□□□■■■■□□□□
      □□□□□■■□□□□□
      □□□□□□□□□□□□\
    ''',

    '''\
    
      □□□□□□□□□□□□
      □□□□□□□□□□□□
      □□□■■□□■■□□□
      □□□■■□□■■□□□
      □□□□□□□□□□□□
      □□■□□□□□□■□□
      □□□■□□□□■□□□
      □□□□■■■■□□□□
      □□□□□□□□□□□□
      □□□□□□□□□□□□\
    ''',

    '''\
    
      □□□□□□□□□□□□
      □□□□□□□□□□□□
      □□□■■□□■■□□□
      □□□■■□□■■□□□
      □□□□□□□□□□□□
      □□□□■■■■□□□□
      □□□■□□□□■□□□
      □□■□□□□□□■□□
      □□□□□□□□□□□□
      □□□□□□□□□□□□\
    '''

    ]

    text_opportunity = [
        '○○○○○○○○○○',
        '○○○○○○○○○●',
        '○○○○○○○○●●',
        '○○○○○○○●●●',
        '○○○○○○●●●●',
        '○○○○○●●●●●',
        '○○○○●●●●●●',
        '○○○●●●●●●●',
        '○○●●●●●●●●',
        '○●●●●●●●●●',
        '●●●●●●●●●●'
    ]


    def __init__(self):
        self.opportunity = len(self.text_opportunity) - 1


    def getOpportunity(self):
        return self.opportunity


    def decreaseOpportunity(self):
        self.opportunity -= 1


    def currentOpportunity(self):
        return self.text_opportunity[self.opportunity]


    def getUpDisplay(self):
        return self.text_mainDispaly[0]


    def getDownDisplay(self):
        return self.text_mainDispaly[1]


    def getSuccessDisplay(self):
        return self.text_mainDispaly[2]


    def getGameoverDisplay(self):
        return self.text_mainDispaly[3]