# Experiments for Crosslingual Test-Time Scaling

We perform crosslingual test-time scaling through budget forcing, which controls the number of thinking tokens generated by s1 models.

### Artifacts
Folder `artifacts/` contains the output artifacts from our experiments for `baselines` models and `s1` models. For `s1`, having `wait` in the folder name indicates extrapolation budget forcing; otherwise, the outputs are from truncation.

Due to the size of the folder, these artifacts are stored on Git LFS system. You can easily download them with the following commands.
```bash
git lfs install # Git LFS initialized.
git lfs pull
```

### Scripts
Folder `eval_scripts/` contains the eval scripts for prompting baselines and s1 models.

```bash
# full eval of s1 models on all languages of MGSM benchmark. 
# you can change the model name and number of thinking tokens in the script.
bash experiments/crosslingual_mgsmeval_scripts/eval_s1.sh
```


### Misc
We also provide several `util` scripts for extracting the average number of tokens and the accuracy results from lm-eval-harness.