#!/usr/bin/env python3
import os.path
import json
import sys
from librip.ctxmngrs import timer
from librip.decorators import print_result
from librip.gens import field, gen_random
from librip.iterators import Unique as unique

path = os.path.abspath(sys.argv[1])

# Здесь необходимо в переменную path получить
# путь до файла, который был передан при запуске

with open(path) as f:
    data = json.load(f)


# Далее необходимо реализовать все функции по заданию, заменив `raise NotImplemented`
# Важно!
# Функции с 1 по 3 дожны быть реализованы в одну строку
# В реализации функции 4 может быть до 3 строк
# При этом строки должны быть не длиннее 80 символов

def f1(arg):
    return(sorted([i for i in unique([j['job-name'] for j in arg], ignore_case = True)]))


def f2(arg):
	return([x for x in arg if 'программист' in x])


def f3(arg):
    return(["{} {}".format(x, "с опытом Python") for x in arg])


@print_result
def f4(arg):
    return(["{}, {} {} {}".format(x,"зарплата", y, "руб.") for x, y in zip(arg, list(gen_random(100000, 200000, len(arg))))])


with timer():
	f4(f3(f2(f1(data))))