import re


def check_valid_email(searchstring):
    """
    Match emails.

    :param searchstring: string
    :return: string
    """
    pass


def extract_author_and_book_names(searchstring):
    """
    Extract author and book.

    :param searchstring: string
    :return: tuple
    """
    pass


def fix_adult_superhero_name(searchstring):
    """
    Replace Boy/Girl or boy/girl with Man/Woman or man/woman respectively.

    :param searchstring: string
    :return: string
    """
    pass


if __name__ == '__main__':

    print("\nProblem 1:")
    testcase11 = 'iamironman.123@starkindustries.com'
    print("Student answer: ",check_valid_email(testcase11),"\tAnswer correct?", check_valid_email(testcase11) == 'valid')

    testcase12 = 'Srogers.250captainA@starkindustries.com'
    print("Student answer: ",check_valid_email(testcase12),"\tAnswer correct?", check_valid_email(testcase12) == 'valid')

    testcase13 = 'nickfury.100@shield.gov'
    print("Student answer: ",check_valid_email(testcase13),"\tAnswer correct?", check_valid_email(testcase13) == 'valid')

    testcase14 = 'venom.144@starkindustries.comasdf'
    print("Student answer: ",check_valid_email(testcase14),"\tAnswer correct?", check_valid_email(testcase14) == 'invalid')

    testcase15 = 'hyperion.942@starkindustries.com'
    print("Student answer: ",check_valid_email(testcase15),"\tAnswer correct?", check_valid_email(testcase15) == 'invalid')

    testcase16 = 'greengoblin.567@shield.gov'
    print("Student answer: ",check_valid_email(testcase16),"\tAnswer correct?", check_valid_email(testcase16) == 'invalid')

    testcase17 = 'drdoom324@starkindustries.com'
    print("Student answer: ",check_valid_email(testcase17),"\tAnswer correct?", check_valid_email(testcase17) == 'invalid')

    testcase18 = 'Hosborn.765*abc@shield.gov'
    print("Student answer: ",check_valid_email(testcase18),"\tAnswer correct?", check_valid_email(testcase18) == 'invalid')

    testcase19 = 'vulture.123@shield.com'
    print("Student answer: ",check_valid_email(testcase19),"\tAnswer correct?", check_valid_email(testcase19) == 'invalid')


    print("\nProblem 2:")
    testcase21 = "George Orwell wrote 1984"
    print("Student answer: ",extract_author_and_book_names(testcase21),"\tAnswer correct?", extract_author_and_book_names(testcase21) == ("George Orwell","1984"))

    testcase22 = "In the 1930s, a Mystery writer wrote Mary Westmacotts. Later it was found that Agatha Christie wrote The Westmacott Novels"
    print("Student answer: ",extract_author_and_book_names(testcase22),"\tAnswer correct?", extract_author_and_book_names(testcase22) == ("Agatha Christie", "The Westmacott Novels"))

    testcase23 = "Roxette wrote books"
    print("Student answer: ", extract_author_and_book_names(testcase23), "\tAnswer correct?", extract_author_and_book_names(testcase23) == ("Roxette", "books"))

    testcase24 = "Erin Morgenstern wrote The Starless Sea Book and The Night Circus"
    print("Student answer: ",extract_author_and_book_names(testcase24),"\tAnswer correct?", extract_author_and_book_names(testcase24) == ("Erin Morgenstern", "The Starless Sea"))

    testcase25 = "Haruki Murakami wrote 1Q84"
    print("Student answer: ",extract_author_and_book_names(testcase25),"\tAnswer correct?", extract_author_and_book_names(testcase25) == ("Haruki Murakami", "1Q84"))

    testcase26 = "Khaled Hosseini wrote sad books"
    print("Student answer: ",extract_author_and_book_names(testcase26),"\tAnswer correct?", extract_author_and_book_names(testcase26) == ("noauthor", "noname"))

    testcase27 = "Haruki Murakami wrote Norwegian Wood"
    print("Student answer: ",extract_author_and_book_names(testcase27),"\tAnswer correct?", extract_author_and_book_names(testcase27) == ("Haruki Murakami", "Norwegian Wood"))


    print("\nProblem 3:")
    testcase31 = 'Spider Boy, I need help!'
    print("Student answer: ",fix_adult_superhero_name(testcase31),"\tAnswer correct?", fix_adult_superhero_name(testcase31) == "Spider Man, I need help!")

    testcase32 = 'There is a boy trapped in a burning building Iron Boy'
    print("Student answer: ",fix_adult_superhero_name(testcase32),"\tAnswer correct?", fix_adult_superhero_name(testcase32) == "There is a boy trapped in a burning building Iron Man")

    testcase33 = 'Spider Girl, I need help!'
    print("Student answer: ",fix_adult_superhero_name(testcase33),"\tAnswer correct?", fix_adult_superhero_name(testcase33) == "Spider Woman, I need help!")

    testcase34 = 'The Invisible girl is a member of the Fantastic Four'
    print("Student answer: ",fix_adult_superhero_name(testcase34),"\tAnswer correct?", fix_adult_superhero_name(testcase34) == "The Invisible woman is a member of the Fantastic Four")

    testcase35 = 'There is a boy that needs to be saved from the alien!'
    print("Student answer: ",fix_adult_superhero_name(testcase35),"\tAnswer correct?", fix_adult_superhero_name(testcase35) == "nomatch")
