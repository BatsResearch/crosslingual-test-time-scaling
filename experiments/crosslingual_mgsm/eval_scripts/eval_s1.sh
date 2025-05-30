# eval on s1 with truncation budget forcing strategy using 4 GPUs

cd lm-evaluation-harness/

LANGS=(bn de en es fr ja ru sw te th zh)
OUTPUT_DIR=../outputs
MODEL=s1.1-3B
THINKING=500 # truncation: max thinking token

mkdir -p $OUTPUT_DIR
for LANG in "${LANGS[@]}"; do
    OUTPUT_FP=${OUTPUT_DIR}/${MODEL}-mgsm_direct_${LANG}_${THINKING}
    lm_eval --model vllm --model_args pretrained=simplescaling/${MODEL},dtype=bfloat16,tensor_parallel_size=4 --tasks mgsm_direct_${LANG} --batch_size auto --apply_chat_template --output_path ${OUTPUT_FP} --log_samples --gen_kwargs "max_gen_toks=32768,max_tokens_thinking=${THINKING}"
done