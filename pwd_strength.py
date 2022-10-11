

class PasswordTool:
    """
        Password strength
    """
    def __init__(self, password):
        # Properties
        self.password = password
        self.strength_level = 0

    def process_password(self):
        # Rule 1: Password length greater than 8
        if len(self.password) >= 8:
            self.strength_level += 1
        else:
            print('Password length requires at least 8 digits')

        # Rule 2: Include numbers
        if self.check_number_exist():
            self.strength_level += 1
        else:
            print('Password requires a number')

        # Rule 3: Include letters
        if self.check_letter_exist():
            self.strength_level += 1
        else:
            print('Password requires letters')

    #
    def check_number_exist(self):
        """
            Determine whether a string contains a number
        """
        has_number = False

        for c in self.password:
            if c.isnumeric():
                has_number = True
                break

        return has_number

    def check_letter_exist(self):
        """
            Determine if the string contains letters
        """
        has_letter = False
        for c in self.password:
            if c.isalpha():
                has_letter = True
                break
        return has_letter


class FileTool:
    """
        FileTool
    """
    def __init__(self, filepath):
        self.filepath = filepath

    def write_to_file(self, line):
        f = open(self.filepath, 'a')
        f.write(line)
        f.close()

    def read_from_file(self):
        f = open(self.filepath, 'r')
        lines = f.readlines()
        f.close()
        return lines


def main():
    """
        main
    """

    try_times = 5
    filepath = 'password_6.0.txt'
    file_tool = FileTool(filepath)

    while try_times > 0:

        password = input('Please enter the password')
        password_tool = PasswordTool(password)
        password_tool.process_password()

        line = 'Password：{}, Strength：{}\n'.format(password, password_tool.strength_level)
        file_tool.write_to_file(line)

        if password_tool.strength_level == 3:
            print('Congratulations! Password strength qualified!')
            break
        else:
            print('Password strength unqualified!')
            try_times -= 1

        print()

    if try_times <= 0:
        print('Sorry, there were too many attempts and the password failed to be set!')

    lines = file_tool.read_from_file()
    print(lines)


if __name__ == '__main__':
    main()
