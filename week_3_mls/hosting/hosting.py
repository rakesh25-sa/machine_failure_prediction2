from huggingface_hub import HfApi
import os

os.environ["HF_TOKEN"] = "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"
api = HfApi(token=os.getenv("HF_TOKEN"))
api.upload_folder(
    folder_path="week_3_mls/deployment",     # the local folder containing your files
    repo_id="rakeshambudkar/Machine-Failure-Prediction",          # the target repo
    # repo_id="praneeth232/Machine-Failure-Prediction",          # the target repo
    repo_type="space",                      # dataset, model, or space
    path_in_repo="",                          # optional: subfolder path inside the repo
)
