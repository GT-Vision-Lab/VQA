Python and MATLAB API and Evaluation Code for Beta v0.1 sample of the VQA dataset.
===================

This sample of the dataset consists of
-10k images from COCO training images
-30k questions (3 per image)
-300k answers (10 per question)

There are 2 types of tasks
-Open Ended Task (Questions are open ended)
-Multiple Choice Task (Each question has 18 choices to predict the answer from)

## Requirements ##
- python 2.7

## Files ##
./Annotations
- Download annotations file from [VQA dataset page](http://visualqa.org/dataset) and place the json file in this folder. This  
- OpenEnded_mscoco_train2014.json (QA Annotation File for Open Ended Task)
- MultipleChoice_mscoco_train2014.json (QA Annotation File for Multiple Choice Task)

./Images
- Download Training images from [MSCOCO website](http://mscoco.org/dataset/#download) and place here after extracting

./HelperTools
- This directory contains Python API to read and visualize the VQA dataset (We will provide MATLAB API soon)
- PythonTools/vqaDemo.py (demo script)
- PythonTools/vqaTools (API to read and visualize data)

./EvaluationTools
- This directory contains Python evaluation codes (We will provide MATLAB evaluation code soon)
- PythonTools/vqaEvalDemo.py (evaluation demo script)
- PythonTools/vqaEvaluation (evaluation code)

./Results
- OpenEnded_mscoco_train2014_fake_results.json (an example of fake results for running demo)
- Visit [VQA] (http://visualqa.org/) page for more details.

## References ##
- [VQA: Visual Question Answering](http://visualqa.org/)
- [Microsoft COCO](http://mscoco.org/dataset/#download)

## Developers ##
- Aishwarya Agrawal (Virginia Tech)
Code for API is based on [MSCOCO API code](https://github.com/pdollar/coco)
The format of the code for Evaluation is based on [MSCOCO evaluation code](https://github.com/tylin/coco-caption)

## Acknowledgement ##
- VQA Team
