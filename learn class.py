class Staff():
    def __init__(self, dig):
        self.dig = dig
    def hired(self):
        print('is hired')
'''
class PC():
    def __init__(self, nm, sexx):
        if (sexx>18):
            self.nm = nm
            self.sex = sexx

    def run(self):
        print('run')
    def words(self):
        print(f'words here {self.nm}, and more {self.sex} thats all.')
'''
class Cook(Staff):
     def __init__(self, who, what, dig):
         super().__init__(dig)
         self.nm = who
         self.tool = what
     def job(self):
        print(f'me {self.nm} and I use {self.tool} to do my tasks.')

class Tender(Staff):
    def __init__(self, who, what,dig):
        super().__init__(dig)
        self.nm = who
        self.drink = what
    def job(self):
        print(f'i stand around playing with my {self.drink} and yah.')

    @classmethod
    def dothis(cls, arg1, arg2):
        return arg1 + arg2

linecook=Cook("joe","knife", 123)
playa=Tender('chic', "booby", 456)
'''
class Testy:
    def __init__(self):
'''
def worker_work(staffer):
    staffer.job()

worker_work(linecook)
playa.job()
linecook.job()
playa.dig()