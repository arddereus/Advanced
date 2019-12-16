class Mytime:

    def __init__(self, hrs=0, mins =0, secs = 0):
        self.hours = hrs
        self.minutes = mins
        self.seconds = secs

    def __str__(self):
        return ("{0}:{1}:{2}".format(self.hours, self.minutes, self.seconds))

    def increment(self, seconds):
        self.seconds += seconds

        while self.seconds >= 60:
            self.seconds -= 60
            self.minutes +=1

        while self.minutes >= 60:
            self.minutes -= 60
            self.hours += 1

    def to_seconds(self):
        hsec = self.hours * 3600
        msec = self.minutes * 60
        secs = self.seconds
        totalsecs = hsec + msec + secs
        return totalsecs

t1 = Mytime(5, 5, 5)
t2 = (5, 5, 10)

newtime = t1.to_seconds
print(newtime())




