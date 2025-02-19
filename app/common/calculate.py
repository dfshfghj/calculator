from sympy import *
from multiprocessing import Process, Queue, freeze_support
from functools import lru_cache

freeze_support()

@lru_cache(maxsize=4096)
def _calculate(expression: str, mode: str):
    expression = sympify(expression, rational=True)
    if mode == '=':
        if isinstance(expression, (Sum, Product, Integral)):
            raw_result = simplify(expression.doit())
        else:
            raw_result = simplify(expression)
        return raw_result
    else:
        result = expression.evalf()
        return result
    
def calculate(expression: str, mode: str, queue: Queue):
        queue.put(_calculate(expression, mode))

def start_process(expression: str, mode: str, queue: Queue):
    process = Process(target=calculate, args=(expression, mode, queue))
    process.daemon = True
    process.start()
    return process

