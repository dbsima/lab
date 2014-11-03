import datetime

class CurrentDate(object):
    def __get__(self, instance, owner):
        """
        self - the descriptor object
        instance - the instance object containing the attribute that was
                    referenced (if it's an attribute of a class rather than an
                    instance, this will be None)
        owner - the class where the descriptor was assigned (class object)
        """
        return datetime.date.today()

    def __set__(self, instance, value):
        """
        self - the descriptor object
        instance - the instance object containing the attribute that was
                    referenced (if it's an attribute of a class rather than an
                    instance, this will be None)
        value - the value being assigned
        """
        raise NotImplementedError("Can't change the current date")


class Example(object):
    date = CurrentDate()

e = Example()
print e.date

e.date = datetime.date.today()
