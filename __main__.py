""" Crabatar CLI
"""
from crabatar import Crabatar
import gizeh

SIZE = 1024
users = {username: Crabatar(username) for username in ('aram', 'ChrisDiFranco',
                                                       'eva', 'jake',
                                                       'mariotocool',
                                                       'yellow_mnm',
                                                       'zucchini',
                                                       'rexstauss',
                                                       'crabber',
                                                       'Callio',
                                                       'TwitterIsForHipsters',
                                                       'HappyHuffman',
                                                       'SpaceX', 'POTUS',
                                                       'matei')}

for crab in users.values():
    print(f'{crab.username + ":":23} DONE')
    crab.write_avatar(f'testout/{crab.username}.png')
