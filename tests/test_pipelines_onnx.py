import unittest

import torch
from onnx_transformers import pipeline
from onnxruntime import InferenceSession


class OnnxExportTestCase(unittest.TestCase):
    MODEL_TO_TEST = ["bert-base-cased", "gpt2", "roberta-base"]

    def test_onnx_graph_creation(self):
        try:
            nlp = pipeline("feature-extraction", onnx=True)
            assert isinstance(nlp.onnx_model, InferenceSession)
        except Exception as e:
            self.fail(e)

    def test_feature_extraction_forward(self):
        self._test_pipeline_forward("feature-extraction", "My name is Bert")

    def test_sentiment_analysis_forward(self):
        self._test_pipeline_forward("sentiment-analysis", "This is a positive text.")

    def test_ner_forward(self):
        self._test_pipeline_forward("ner", "My name is Bert")

    def test_question_answering_forward(self):
        self._test_pipeline_forward(
            "question-answering", {"question": "Who is Jim Henson ?", "context": "Jim Henson was a nice puppet"}
        )

    def test_zero_shot_classification_forward(self):
        sequence = "Who are you voting for in 2020?"
        candidate_labels = ["economics", "politics", "public health"]

        try:
            # test onnx forward
            nlp = pipeline("zero-shot-classification", onnx=True)
            nlp(sequence, candidate_labels)

            # test torch forward
            nlp = pipeline("zero-shot-classification", onnx=False)
            assert isinstance(nlp.model, torch.nn.Module)
            nlp(sequence, candidate_labels)
        except Exception as e:
            self.fail(e)

    def _test_pipeline_forward(self, task, example):
        try:
            # test onnx forward
            nlp = pipeline(task, onnx=True)
            nlp(example)

            # test torch forward
            nlp = pipeline(task, onnx=False)
            assert isinstance(nlp.model, torch.nn.Module)
            nlp(example)
        except Exception as e:
            self.fail(e)
