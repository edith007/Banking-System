import csv

from django.core.management.base import BaseCommand
from zerver.models import Bank, BankDetail

class Command(BaseCommand):
    help = "Command to import the data dump"

    def handle(self, *args, **kwargs):
        with open('/home/siddharth/Desktop/bank.csv', 'r') as csv_file:
            csv_reader = csv.reader(csv_file, delimiter = ',')
        
            for line in csv_reader:
                Bank.objects.create(id=line[0], name=line[1])

        with open('/home/siddharth/Desktop/bank_branches.csv', 'r') as csv_file:
            csv_reader = csv.reader(csv_file, delimiter = ',')

            for line in csv_reader:
                bank = Bank.objects.get(id=line[1])
                BankDetail.objects.create(ifsc=line[0], bank_id=bank, branch=line[2], address=line[3], city=line[4], district=line[5], state=line[6])
