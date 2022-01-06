
class Series():
    id: int
    name: str

class Run():
    id: int
    series_id: int
    date: datetime.datetime

    def partitioner(self) -> views_partitioning.DataPartitioner:
        # ~~ infer partitioner from date + formula ~~ #
        return partitioner

class Model():
    id:                 int

    name:               str
    level_of_analysis:  str
    outcome:            str

    queryset_name:      str

    train_start:        int
    train_end:          int

    training_date:      datetime.datetime
    author:             str

    retrain:            bool

    constituent_models: Dict[str,"Model"] # str is the name of indep. column

    _model_object:      scikit_learn_model

    def publish(self):
        # ~~ publish to object storage ~~ #

    @property
    def queryset(self) -> viewser.Queryset:
        # ~~ get via viewser ~~ #
        return queryset

    @classmethod
    def from_model_object(
            cls,
            name: str,
            level_of_analysis: str,
            outcome: str,
            train_start: int,
            train_end: int,
            trained_at: datetime.datetime,
            author: str,
            constituent_models: Dict[str, "Model"],
            model_object: scikit_learn_model) -> "Model":
        # ~~ Instantiate new Model from model object ~~ # 
        return instance

    @classmethod
    def fetch(self, name) -> "Model" 
        # ~~ fetch via object storage / database (object + metadata) ~~ #
        return instance 

class RunResult():
    id: int
    run_id: int
    model_id: int

    def publish(self) -> None:
        # ~~ Publish predictions to object storage under name ~~ # 
        name = self.run.series.name + run.series.date + self.model.name

    @classmethod
    def fetch(cls, name: str) -> "RunResult":
        # ~~ Fetch results associated with name ~~ # 
        return instance
