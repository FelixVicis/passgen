#!/usr/bin/python
from os import path
from random import SystemRandom as seed


def get_path_from_home(*path_parts):
    from os import path

    home = path.expanduser('~')

    return path.join(home, *path_parts)


def get_dictionary(path):
    with open(path) as f:
        return f.read().splitlines()


def generate_word_password(dictionary=None, n=4, **kwargs):
    rand = seed()

    if (not dictionary):
        dictionary = get_path_from_home('dictionary.dic')

    dictionary = get_dictionary(dictionary)

    words = [
        rand.choice(dictionary)
        for _ in range(n)
    ]

    return ' '.join(words)


def get_character_set(set_id='a'):
    def get_alphanumeric():
        return range(0x0030, 0x0039) + range(0x0041, 0x005A) + range(0x0061, 0x007A)

    def get_whitespace():
        return get_alphanumeric() + [0x20, 0xA0, 0x9]

    def get_special():
        return get_whitespace() + range(0x0021, 0x002F) + range(0x003A, 0x0040) + \
            range(0x005B, 0x0060) + range(0x007B, 0x007E)

    def get_unicode():
        return get_special() + range(0x00A1, 0x10FFFF)

    case = {
        'a': get_alphanumeric,
        'w': get_whitespace,
        's': get_special,
        'u': get_unicode,
    }

    return map(unichr, case[set_id]())


def generate_character_password(state='a', n=20, **kwargs):
    rand = seed()

    character_set = get_character_set(state)

    characters = [
        rand.choice(character_set)
        for _ in range(n)
    ]

    return ''.join(characters)


def generate_password(**kwargs):
    if (kwargs['state'] is 'd'):
        return generate_word_password(**kwargs)

    return generate_character_password(**kwargs)


if __name__ == "__main__":
    from argparse import ArgumentParser as console
    from argparse import ArgumentDefaultsHelpFormatter as formatter

    parser = console(
        description='Password Generator',
        formatter_class=formatter)

    parser.add_argument('--dictionary', '-d',
                        type=str,
                        metavar="path_to_file",
                        default=None,
                        help="Overrides the dictionary file used.")

    parser.add_argument('-n',
                        default=20,
                        type=int,
                        metavar="length",
                        help="Length of the output password.")

    parser.add_argument('--state', '-s', default='a',
                        choices=[
                            'a',
                            'w',
                            's',
                            'u',
                            'd',
                        ],
                        help="""Defines the character set used to create the password.
                                Sets are:
                                    alphanumeric,
                                    whitespace,
                                    special-characters,
                                    unicode,
                                    or dictionary.""")

    arguments = parser.parse_args()

    try:
        print generate_password(**vars(arguments))
    except Exception as e:
        print e
