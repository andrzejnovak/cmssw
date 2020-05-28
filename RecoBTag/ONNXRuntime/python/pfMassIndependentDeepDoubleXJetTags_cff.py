from __future__ import absolute_import
import FWCore.ParameterSet.Config as cms
from .pfDeepDoubleBvLJetTags_cfi import pfDeepDoubleBvLJetTags
from .pfDeepDoubleCvLJetTags_cfi import pfDeepDoubleCvLJetTags
from .pfDeepDoubleCvBJetTags_cfi import pfDeepDoubleCvBJetTags

pfMassIndependentDeepDoubleBvLJetTags = pfDeepDoubleBvLJetTags.clone(
    model_path = "RecoBTag/Combined/data/DeepDoubleX/94X/V02/BvL_best.onnx")
pfMassIndependentDeepDoubleCvLJetTags = pfDeepDoubleCvLJetTags.clone(
    model_path = "RecoBTag/Combined/data/DeepDoubleX/94X/V02/CvL_best.onnx")
pfMassIndependentDeepDoubleCvBJetTags = pfDeepDoubleCvBJetTags.clone(
    model_path = "RecoBTag/Combined/data/DeepDoubleX/94X/V02/CvB_best.onnx")
