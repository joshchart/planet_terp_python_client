# coding: utf-8

# flake8: noqa

# import all models into this package
# if you have many models here with many references from one model to another this may
# raise a RecursionError
# to avoid this, import only the models that you directly need like:
# from planet_terp.model.pet import Pet
# or import this package, but before doing it, use:
# import sys
# sys.setrecursionlimit(n)

from planet_terp.model.course import Course
from planet_terp.model.grades import Grades
from planet_terp.model.professor import Professor
from planet_terp.model.search_result import SearchResult
