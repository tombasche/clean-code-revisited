"""
Meaningful names
"""

# TODO - pull apart some of the examples in the book and how they can be improved through types
# When is it ok to use a,b,i,x etc.?
# noise words - this is still relevant. Take a few minutes to think of the intent of the data. data or information is always tempting - but everything is information! Maybe instead of UserInformation, UserDetails, UserBankAccounts etc.
# Names that you have to read out

# Rip apart the meaningful context example (side effects, stupid function names)


# This is the kind of rubbish the book promotes:
class GuessStatisticsMessage:

    def __init__(self):
        self.number = ""
        self.verb = ""
        self.plural_modifier = ""

    def make(self, candidate, count):
        self.create_plural_dependent_message_parts(count)
        return f"There {self.verb} {self.number} {candidate}{self.plural_modifier} "

    def create_plural_dependent_message_parts(self, count):
        if count == 0:
            self.there_are_no_letters()
        elif count == 1:
            self.there_is_one_letter()
        else:
            self.there_are_many_letters(count)

    def there_are_many_letters(self, count):
        self.number = str(count)
        self.verb = "are"
        self.plural_modifier = "s"

    def there_is_one_letter(self):
        self.number = "1"
        self.verb = "is"
        self.plural_modifier = ""

    def there_are_no_letters(self):
        self.number = "no"
        self.verb = "are"
        self.plural_modifier = "s"
