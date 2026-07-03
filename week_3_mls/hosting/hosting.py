from huggingface_hub import HfApi
import os


os.environ["HF_TOKEN"] = os.getenv("HF_TOKEN")    # please use your token

api = HfApi(token=os.getenv("HF_TOKEN"))
api.upload_folder(
    folder_path="week_3_mls/deployment",     # the local folder containing your files
    # replace with your repoid
    repo_id="rakeshambudkar/Machine-Failure-Prediction",          # the target repo

    repo_type="space",                      # dataset, model, or space
    path_in_repo="",                          # optional: subfolder path inside the repo
)
