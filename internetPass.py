import string

underscore = "_"


class UsernameContainsIllegalCharacter(Exception):
    def __init__(self, arg, index):
        self._arg = arg
        self._index = index

    def get_index(self):
        return self._arg.index(self._index)

    def get_arg(self):
        return self._arg

    def __str__(self):
        return "Username %s contains illegal character at index %s " % (self._arg, self._index)


class UsernameTooShort(Exception):
    def __init__(self, arg):
        self._arg = arg

    def get_arg(self):
        return self._arg

    def __str__(self):
        return "Username %s too short" % self._arg


class UsernameTooLong(Exception):
    def __init__(self, arg):
        self._arg = arg

    def get_arg(self):
        return self._arg

    def __str__(self):
        return "Username %s too long" % self._arg


class PasswordTooLong(Exception):
    def __init__(self, arg):
        self._arg = arg

    def __str__(self):
        return "Password too long: %s" % self._arg

    def get_arg(self):
        return self._arg


class PasswordTooShort(Exception):
    def __init__(self, arg):
        self._arg = arg

    def __str__(self):
        return "Password Too short: %s" % self._arg

    def get_arg(self):
        return self._arg


class PasswordMissingCharacter(Exception):
    def __init__(self, arg):
        self._arg = arg

    def get_arg(self):
        return self._arg

    def __str__(self):
        return "Password Missing Character " % self._arg


class PasswordMissingUppercase(PasswordMissingCharacter):
    def __init__(self, arg):
        super(PasswordMissingUppercase, self).__init__(arg)
        self._arg = arg

    def get_arg(self):
        return self._arg

    def __str__(self):
        return "Password %s is missing a character (Uppercase)" % self._arg


class PasswordMissingLowercase(PasswordMissingCharacter):
    def __init__(self, arg):
        super(PasswordMissingLowercase, self).__init__(arg)
        self._arg = arg

    def get_arg(self):
        return self._arg

    def __str__(self):
        return "Password %s is missing a character (Lowercase) " % self._arg


class PasswordMissingDigit(PasswordMissingCharacter):
    def __init__(self, arg):
        super(PasswordMissingDigit, self).__init__(arg)
        self._arg = arg

    def get_arg(self):
        return self._arg

    def __str__(self):
        return "Password %s is missing a character (Digit) " % self._arg


class PasswordMissingSpecialChar(PasswordMissingCharacter):
    def __init__(self, arg):
        super(PasswordMissingSpecialChar, self).__init__(arg)
        self._arg = arg

    def get_arg(self):
        return self._arg

    def __str__(self):
        return "Password %s missing special character " % self._arg


def count_punctuations(password):
    SpecialCharCounter = 0

    for i in password:
        if i in string.punctuation:
            SpecialCharCounter += 1

    return SpecialCharCounter


def check_input(username, password):
    try:
        for i in username:
            if i != underscore and not i.isalnum():
                raise UsernameContainsIllegalCharacter(username, i)

        if len(username) < 3:
            raise UsernameTooShort(username)
        elif len(username) > 16:
            raise UsernameTooLong(username)

        if len(password) < 8:
            raise PasswordTooShort(password)
        elif len(password) > 40:
            raise PasswordTooLong(password)
        elif password.islower():
            raise PasswordMissingUppercase(password)
        elif not any(char.isdigit() for char in password):
            raise PasswordMissingDigit(password)
        elif count_punctuations(password) != 1:
            raise PasswordMissingSpecialChar(password)

    except UsernameContainsIllegalCharacter as eIllegalCharacter:
        print(eIllegalCharacter)
    except UsernameTooShort as eUsernameTooShort:
        print(eUsernameTooShort)
    except UsernameTooLong as eUsernameTooLong:
        print(eUsernameTooLong)
    except PasswordTooShort as ePasswordTooShort:
        print(ePasswordTooShort)
    except PasswordTooLong as ePasswordTooLong:
        print(ePasswordTooLong)
    except PasswordMissingDigit as ePasswordMissingDigit:
        print(ePasswordMissingDigit)
    except PasswordMissingSpecialChar as ePasswordMissingSpecialChar:
        print(ePasswordMissingSpecialChar)
    except PasswordMissingCharacter as ePasswordMissingCharacter:
        print(ePasswordMissingCharacter)
    else:
        print("username %s and password %s are OK" % (username, password))


def main():
    check_input("1", "2")
    check_input("0123456789ABCDEFG", "2")
    check_input("A_a1222.2", "12345678")
    check_input("A_1", "2")
    check_input("A_1", "ThisIsAQuiteLongPasswordAndHonestlyUnnecessary")
    check_input("A_1", "abcdefghijklmnop")
    check_input("A_1", "ABCDEFGHIJLKMNOP")
    check_input("A_1", "ABCDEFGhijklmnop")
    check_input("A_1", "4BCD3F6h1jk1mn0p")
    check_input("A_1", "4BCD3F6.1jk1mn0p")


main()
