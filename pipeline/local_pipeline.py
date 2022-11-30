from typing import Dict, Optional, Text

import tensorflow_model_analysis as tfma
from ml_metadata.proto import metadata_store_pb2
from tfx import v1 as tfx

from tfx.components import ImportExampleGen
from tfx.components import StatisticsGen
from tfx.v1.components import ImportSchemaGen
from tfx.components import ExampleValidator
from tfx.components import Transform
from tfx.components import Tuner
from tfx.components import Trainer
from tfx.components import Evaluator
from tfx.components import Pusher

from tfx.types import Channel
from tfx.types.standard_artifacts import Model
from tfx.types.standard_artifacts import ModelBlessing
from tfx.dsl.components.common import resolver

def creat_pipeline(
    pipeline
)

