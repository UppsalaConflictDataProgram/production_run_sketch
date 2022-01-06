# Pseudocode production run using models

from views_runs import Series, Run, Model, RunResult

series = Series.get(series_name)

run = Run.get(series, level_of_analysis, outcome)
# Gets current run, based on current date
# This also retrieves previously trained model objects
# from last month

run.partitioner
# The data partitioner is defined by combining the run date with a formula for how
# to divide the data (ex. percentage train / test / calibrate).

for model in run.models:
    if model.retrain:
        model = retrain_model(model)
        model.publish()

    result = Result.new(model)

    result.publish()
