from django.db import models
from users.models import Student, Staff
from books.models import Book

class Transaction(models.Model):
    """Will hold the transaction details"""

    staff = models.ForeignKey(Staff, on_delete=models.CASCADE)
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    book = models.ForeignKey(Book, on_delete=models.CASCADE)

    issued = models.BooleanField(default=False)
    issue_time = models.DateTimeField()

    returned = models.BooleanField(default=False)
    return_time = models.DateTimeField(blank="True", null="True")

    issue_hash = models.CharField(max_length=200, default="0xasdfg12345")
    return_hash = models.CharField(max_length=200, default="0xasdfg12345")

    def __str__(self):
        """To represent the objects name in the admin panel"""
        return '{} {}'.format(self.student.rollno, self.book.details.name)
