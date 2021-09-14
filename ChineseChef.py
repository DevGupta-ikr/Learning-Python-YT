from Chef import Chef

class ChineseChef(Chef):

    def make_special(self):  # Override
        print("The chef makes a special dish Also")

    def make_fried_rice(self):
        print("The chef makes a fried rice")