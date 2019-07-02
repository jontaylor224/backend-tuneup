#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Tuneup assignment"""

__author__ = "jontaylor224"

import cProfile
import functools
import timeit
import io
import pstats
# from pstats import SortKey


def profile(func):
    """A function that can be used as a decorator to measure performance"""
    # You need to understand how decorators are constructed and used.
    # Be sure to review the lesson material on decorators, they are used
    # extensively in Django and Flask.
    # raise NotImplementedError("Complete this decorator function")
    def wrapper(*args, **kwargs):
        pr = cProfile.Profile()
        pr.enable()
        result = func(*args, **kwargs)
        pr.disable()
        ps = pstats.Stats(pr).strip_dirs().sort_stats('cumulative')
        ps.print_stats(10)
        return result
    return wrapper


def read_movies(src):
    """Returns a list of movie titles"""
    print('Reading file: {}'.format(src))
    with open(src, 'r') as f:
        return f.read().splitlines()


@profile
def find_duplicate_movies(src):
    """Returns a list of duplicate movies from a src list"""
    movies = read_movies(src)
    return [i for i in set(movies) if movies.count(i) > 1]


# def timeit_helper():
#     """Part A:  Obtain some profiling measurements using timeit"""
#     t = timeit.Timer(stmt='main()', setup='')
#     times = t.repeat(repeat=7, number=3)
#     timing_result = min(times) / 3
#     print('Best time across 7 repeats of 3 runs per repeat: ', timing_result)
#     return timing_result


def main():
    """Computes a list of duplicate movie entries"""
    result = find_duplicate_movies('movies.txt')
    print('Found {} duplicate movies:'.format(len(result)))
    print('\n'.join(result))


if __name__ == '__main__':
    main()
