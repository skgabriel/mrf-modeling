from transformers import AutoTokenizer, AutoModelForCausalLM,AutoModelForSeq2SeqLM
import torch
import json
import argparse


parser = argparse.ArgumentParser()
parser.add_argument('--model_type',type=str,default="t5")
parser.add_argument('--device', type=str, default='any')
parser.add_argument('--input_file', type=str, default='./example.txt')
parser.add_argument('--output_file', type=str, default='./output.jsonl')
parser.add_argument('--decoding', type=str, default='beam_search')
args = parser.parse_args()
print(args)

model_type = args.model_type

if torch.cuda.is_available() and args.device == "any":
        device = "cuda"
elif args.device == "any":
        device = "cpu"
else:
        device = args.device

def format_output(sequence,model_type):
        if model_type == "t5":
           if "<pad> " in sequence:
              sequence = sequence.replace("<pad> ","")
           return sequence.replace("</s>","")
        else:
           return sequence.split("]")[-1].replace(" <|endoftext|>","")

if model_type == "gpt":
   tokenizer = AutoTokenizer.from_pretrained("petrichorRainbow/mrf-GPT")
   model = AutoModelForCausalLM.from_pretrained("petrichorRainbow/mrf-GPT").to(device)
else:
   tokenizer = AutoTokenizer.from_pretrained("petrichorRainbow/mrf-T5")
   model = AutoModelForSeq2SeqLM.from_pretrained("petrichorRainbow/mrf-T5").to(device)

dims = ["[writer_intent]", "[effect_on_reader]", "[reader_action]","[pred_label]","[gold_label]","[spread]"]
domains = ["[climate]", "[covid]","[cancer]","[Other]"]
tokenizer.add_tokens(dims + domains)
output_file = open(args.output_file,"w")
for headline in open(args.input_file).readlines():
    headline = headline.strip()
    line_ = {"headline":headline}
    for dim in dims:
        input_ = tokenizer.encode(headline + " " + dim, return_tensors="pt").to(device)
        if args.decoding == "beam_search":
           output_ = model.generate(input_ids=input_,num_beams=3,max_length=50)
        else:
           output_ = model.generate(input_ids=input_,top_k=3,max_length=50)
        output_ = format_output(tokenizer.decode(output_[0]),model_type)
        line_[dim] = output_
    output_file.write(str(json.dumps(line_)) + "\n")
