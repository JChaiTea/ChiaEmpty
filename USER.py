import csv


class users(object):
    """Class designed to organize active users on the program"""

    def __init__(self):
        """Constructor"""
        while True:
            cUser = input('Hello! Welcome to Chia, please enter your username: ')
            if len(cUser) != 0:
                self.cUser = cUser
                break
            else:
                print('Please enter a valid username!')
        users.welcome(self)

    def welcome(self):
        """Check the User and diplay welcome"""
        user_status = users.checkUser(self)
        if user_status:
            print(f'Welcome, {self.cUser}, thanks for using Chia')
        else:
            entries = []
            while True:
                acctnum = input('Please enter an account number:')
                if len(acctnum) > 0:
                    entries.append(True)
                email = input('Please enter a valid email: ')
                if len(email) > 0:
                    entries.append(True)
                phone = input('Please enter a valid phone number')
                if len(phone) > 0:
                    entries.append(True)
                if sum(entries) == 3:
                    createdUser = users.creatUser(self, name=self.cUser, account=acctnum, email=email, phone=phone)
                    if createdUser == 'user created':
                        print(f'Welcome {self.cUser}, thanks for using Chia')
                    break
                else:
                    print('Please enter inputs for all fields')


    def checkUser(self):
        """Check the status of the given user"""
        with open('userBase.csv', 'r') as infile:
            reader = csv.reader(infile)
            for line in reader:
                if self.cUser in line:
                    return True
            return False

    def creatUser(self, name, account, email, phone):
        """Create a new user into the system"""
        try:
            with open('userBase.csv', 'a') as outfile:
                writer = csv.writer(outfile)
                writer.writerow([name, account, email, phone])
                writer.writerow([])
            return 'user created'
        except:
            return 'unable to create user'

    def getEmail(self):
        """Return the users email address"""
        with open('userBase.csv', 'r') as infile:
            reader = csv.reader(infile)
            for row in reader:
                if self.cUser in row:
                    email = row[2]
        return email
