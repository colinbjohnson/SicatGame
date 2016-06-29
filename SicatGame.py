#!/usr/bin/env python

from os import system
from sys import exit
import webbrowser


def userAJ():
    system('say Do you like playing Minecraft?')
    minecraft = raw_input('Do you like playing Minecraft (Yes or No):\n')
    if minecraft == 'Yes':
        print 'I love Minecraft, too'
        system('say I love Minecraft, too.')
    else:
        system('say Do not lie to me AJ, I just saw you playing minecraft.')
    system('say How many people are in The Shield')
    the_shield = raw_input('How many people are in The Shield (3 or 5):\n')
    if the_shield == '3':
        print 'A.J.,Jeremy,Julian'
        system('say A.J.,Jeremy,Julian')
    else:
        system('say You Failed!!!')


def userNaomi():
    system('say Do you like playing Runescape?')
    runescape = raw_input('Do you like playing Runescape (Yes or No):\n')
    if runescape == 'Yes':
        system('say I like Runescape, too.')
    else:
        system('say Do not lie to me Naomi, I know that you play Runescape at least 3 hours a day.')
    system('say Do you love me?')
    love_me = raw_input('Do you love me (Yes or No):\n')
    if love_me == 'Yes':
        system('say You are smart.')
    elif love_me == 'No':
        system('say Love Me.Love Me.Love Me.')
    else:
        print 'You need to answer yes or no.'


def userMJ():
    system('say Are you a tiger?')
    tiger = raw_input('Are you a tiger (Yes or No):\n')
    if tiger == 'Yes':
        system('say I have a picture for you.')
        print '                  ___......----:\'"":--....('
        print '            .-\':\'"":   :  :  :   :  :  :.(1\.`-.  '
        print '          .\'`.  `.  :  :  :   :   : : : : : :  .\';'
        print '         :-`. :   .  : :  `.  :   : :.   : :`.`. a;'
        print '         : ;-. `-.-._.  :  :   :  ::. .\' `. `., =  ;'
        print '         :-:.` .-. _-.,  :  :  : ::,.\'.-\' ;-. ,\'\'\'"'
        print '       .\'.\' ;`. .-\' `-.:  :  : : :;.-\'.-.\'   `-\''
        print ':.   .\'.\'.-\' .\'`-.\' -._;..:---\'\'\'"~;._.-;'
        print ':`--\'.\'  : :\'     ;`-.;            :.`.-\'`. '
        print ' `\'"`    : :      ;`.;             :=; `.-\'`.'
        print ' jgs     : \'.    :  ;              :-:   `._-`.'
        print '          `\'"\'    `. `.            `--\'     `._;'
        print '                    `\'"\'    '
    else:
        system('say I know you are a tiger.')

def favoriteChild():
    system('say Who is your favorite child?')
    Favorite_Child = raw_input('Who is your favorite child? (AJ or Naomi)\n')
    if Favorite_Child == 'AJ':
        system('say You are smart.')
    elif Favorite_Child == 'Naomi':
        system('say I do not think so.')
        favoriteChild()
    else:
        print ''


def userGen():
    favoriteChild()


def userCedric():
    system('say Let me play a video for you.')
    webbrowser.open('http://www.python.org/')
    exit(1)


def userJocelyn():
    system('say I heard that you are a talker. What should we talk about?')
    talk_about = raw_input('Enter one of: Sister, Thunder Valley, Music, Work:\n')
    if talk_about == 'Sister':
        system('say I heard that your sister is a tiger.')
    elif talk_about == 'Thunder Valley':
        system('say When are we going to Thunder Valley next?')
        thunder_valley = raw_input('Enter one of: (Monday, Next Week):\n')
        if thunder_valley == 'Monday':
            system('say When are we going to Thunder Valley next?')
        else:
            system('say That is not soon enough. I am going without you.')
    elif talk_about == 'Work':
        system('say I don\'t like Walkgreens, either. They always mess my perscriptions up.')
    else:
        system('say I\'m sorry I don\'t know how to talk about {!s}.'.format(talk_about))
        exit(1)


def getUser():
    "gets a User"
    system('say Hello, who am I speaking with?')
    user = raw_input('Enter your name (AJ, Conrad, Naomi, Mary Jane, Jocelyn, Gen, Cedric) or type Exit to quit:\n')

    if user == 'AJ':
        system('say Hello AJ')
    elif user == 'Naomi':
        system('say Hello Naomi')
    elif user == 'Mary Jane':
        system('say Hello Mary Jane')
    elif user == 'Jocelyn':
        system('say Hello Jocelyn')
    elif user == 'Gen':
        system('say Hello Gen')
    else:
        system('say I\'m sorry that user was not recognized.')
        exit(1)

    return user

game = True
while game is True:
    user = getUser()

    print('Hello, {!s}'.format(user))

    if user == 'AJ':
        userAJ()
    elif user == 'Naomi':
        userNaomi()
    elif user == 'Mary Jane':
        userMJ()
    elif user == 'Jocelyn':
        userJocelyn()
    elif user == 'Cedric':
        userCedric()
    elif user == 'Gen':
        userGen()

    else:
        game = False
