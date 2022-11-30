import os, sys, glob
from utils import util
from absl import logging

from tfx import v1 as tfx
# from pipeline import configs
from pipeline import local_pipeline

OUTPUT_DIR = "."

# PIPELINE_ROOT = os.path.join(OUTPUT_DIR, "tfx_pipeline_output", configs.PIPELINE_NAME)
# METADATA_PATH = os.path.join(
#     OUTPUT_DIR, "tfx_metadata", configs.PIPELINE_NAME, "metadata.db"
# )
# SERVING_MODEL_DIR = os.path.join(PIPELINE_ROOT, "serving_model")



def run():
    logging.info(f'{util.get_time()}, Process start!!')
    tfx.orchestration.LocalDagRunner().run(
        local_pipeline.create_pipeline(
            
        )
    )

if __name__=="__main__":
    logging.set_verbosity(logging.INFO)
    run()
