# diagram.py
from diagrams import Cluster, Diagram
from diagrams.gcp.storage import GCS
from diagrams.gcp.devtools import Tasks
from diagrams.gcp.compute import Run

with Diagram("Diagram Cloud Tasks", show=False):
    Storage_Input = GCS("Cloud Storage") 

    with Cluster("App"):
        with Cluster("Event App"):
            Cloud_run = Run("Cloud Run")

        Queue = Tasks("Cloud Tasks")
        Storage_Output = GCS("Cloud Storage")

    Storage_Input >> Cloud_run >> Queue >> Storage_Output