# onnx_transformers

![onnx_transformers](https://github.com/patil-suraj/onnx_transformers/blob/master/data/social_preview.jpeg?raw=True)

Accelerated NLP pipelines for fast inference 🚀 on CPU. Built with 🤗Transformers and ONNX runtime. +Plus quantize option 😊

## Installation:

```bash
pip install git+https://github.com/patil-suraj/onnx_transformers
```

## Usage:

> *NOTE* : This is an experimental project and only tested with PyTorch

The pipeline API is similar to transformers [pipeline](https://huggingface.co/transformers/main_classes/pipelines.html) with just a few differences which are explained below.

Just provide the path/url to the model and it'll download the model if needed from the [hub](https://huggingface.co/models) and automatically create onnx graph and run inference.

```python
from onnx_transformers import pipeline

# Initialize a pipeline by passing the task name and 
# set onnx to True (default value is also True)
>>> nlp = pipeline("sentiment-analysis", onnx=True)
>>> nlp("Transformers and onnx runtime is an awesome combo!")
[{'label': 'POSITIVE', 'score': 0.999721109867096}]  
```

Or provide a different model using the `model` argument.

```python
from onnx_transformers import pipeline

>>> nlp = pipeline("question-answering", model="deepset/roberta-base-squad2", onnx=True)
>>> nlp({
  "question": "What is ONNX Runtime ?", 
  "context": "ONNX Runtime is a highly performant single inference engine for multiple platforms and hardware"
})
{'answer': 'highly performant single inference engine for multiple platforms and hardware', 'end': 94, 'score': 0.751201868057251, 'start': 18}
```

```python
from onnx_transformers import pipeline

>>> nlp = pipeline("ner", model="mys/electra-base-turkish-cased-ner", onnx=True, quantized=True, grouped_entities=True)
>>> nlp("adana kebap ülkemizin önemli lezzetlerinden biridir.")
[{'entity_group': 'B-food', 'score': 0.869149774312973, 'word': 'adana kebap'}]
```

Set `onnx` to `False` for standard torch inference.
Set `quantized` to `True` for quantize with Onnx. ( set `onnx` to True)

You can create `Pipeline` objects for the following down-stream tasks:

 - `feature-extraction`: Generates a tensor representation for the input sequence
 - `ner`: Generates named entity mapping for each word in the input sequence.
 - `sentiment-analysis`: Gives the polarity (positive / negative) of the whole input sequence. Can be used for any text classification model.
 - `question-answering`: Provided some context and a question referring to the context, it will extract the answer to the question in the context.
 - `zero-shot-classification`:
  

Calling the pipeline for the first time loads the model, creates the onnx graph, and caches it for future use. Due to this, the first load will take some time. Subsequent calls to the same model will load the onnx graph automatically from the cache.

The key difference between HF pipeline and onnx_transformers is that the `model` parameter should always be a `string` (path or url to the saved model). Also, the `zero-shot-classification` pipeline here uses `roberta-large-mnli` as default model instead of `facebook/bart-large-mnli` as BART is not yet tested with onnx runtime.


## Benchmarks

> Note: For some reason, onnx is slow on colab notebook so you won't notice any speed-up there. Benchmark it on your own hardware.

For detailed benchmarks and other information refer to this blog post and notebook.
- [Accelerate your NLP pipelines using Hugging Face Transformers and ONNX Runtime](https://medium.com/microsoftazure/accelerate-your-nlp-pipelines-using-hugging-face-transformers-and-onnx-runtime-2443578f4333)
- [Exporting 🤗 transformers model to ONNX](https://github.com/huggingface/transformers/blob/master/notebooks/04-onnx-export.ipynb)

To benchmark the pipelines in this repo, see the [benchmark_pipelines](https://github.com/patil-suraj/onnx_transformers/blob/master/notebooks/benchmark_pipelines.ipynb) notebook. 
>(Note: These are not yet comprehensive benchmarks.)

**Benchmark `feature-extraction` pipeline** 

![](https://github.com/patil-suraj/onnx_transformers/blob/master/data/feature_extraction_pipeline_benchmark.png?raw=True)


**Benchmark `question-answering` pipeline**

![](https://github.com/patil-suraj/onnx_transformers/blob/master/data/qa_pipeline_benchmark.png?raw=True)
