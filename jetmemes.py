#!/usr/bin/env python3

import itertools
from random import shuffle

l = ['jet', 'fuel', 'melt', 'steel', 'beams', 'meme']


def jet_melt():
    perm = list(itertools.permutations(l))
    shuffle(perm)
    return perm


def steel_fuel(a):
    return "{}can't{}".format("{} " * 2, " {}" * 3).format(a[0][0].upper() + a[0][1:], *a[1:len(l)])


def beam_memes():
    perm = jet_melt()
    print("\n".join([steel_fuel(a) for a in perm]))


def jet_beams():
    perm = jet_melt()[0]
    return steel_fuel(perm)


# A helpful alias
def create_commit_message():
    return jet_beams()


if __name__ == "__main__":
    beam_memes()
