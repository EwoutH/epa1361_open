import copy
import timeit

from ema_workbench import (Model, Policy, ema_logging, SequentialEvaluator, MultiprocessingEvaluator)
from problem_formulation import get_model_for_problem_formulation

# Setup model
dike_model, planning_steps = get_model_for_problem_formulation(3)

uncertainties = copy.deepcopy(dike_model.uncertainties)
levers = copy.deepcopy(dike_model.levers)


# Define benchmark function
def perf_test(dike_model=dike_model):
    with SequentialEvaluator(dike_model) as evaluator:
        evaluator.perform_experiments(scenarios=10, policies=1)


# Run benchmark with timeit and print results
durations = timeit.Timer(perf_test).repeat(repeat=25, number=1)
print(durations)
