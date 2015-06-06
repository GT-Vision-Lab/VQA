Python API and Evaluation Code for Beta v0.1 sample of the VQA dataset.
===================

This sample of the dataset consists of
- 10k images from COCO training images
- 30k questions (3 per image)
- 300k answers (10 per question)

There are 2 types of tasks
- Open Ended Task (Questions are open ended)
- Multiple Choice Task (Each question has 18 choices to predict the answer from)

## Requirements ##
- python 2.7

## Files ##
./Annotations
- Download annotations file from [here](https://filebox.ece.vt.edu/~cvmlp/vqa//annotations.zip), extract them and place in this folder.
- After download and extraction, this folder should have the following 2 files  
- OpenEnded_mscoco_train2014.json (QA Annotation File for Open Ended Task)
- MultipleChoice_mscoco_train2014.json (QA Annotation File for Multiple Choice Task)

./Images
- Download Training images from [MSCOCO website](http://mscoco.org/dataset/#download) and place here after extracting

./PythonHelperTools
- This directory contains Python API to read and visualize the VQA dataset (We will provide MATLAB API soon)
- vqaDemo.py (demo script)
- vqaTools (API to read and visualize data)

./PythonEvaluationTools
- This directory contains Python evaluation codes (We will provide MATLAB evaluation code soon)
- vqaEvalDemo.py (evaluation demo script)
- vqaEvaluation (evaluation code)

./Results
- OpenEnded_mscoco_train2014_fake_results.json (an example of fake results for running demo)
- Visit [VQA Evaluation Page] (http://visualqa.org/evaluate) page for more details.

## References ##
- [VQA: Visual Question Answering](http://visualqa.org/)
- [Microsoft COCO](http://mscoco.org/dataset/#download)

## Developers ##
- Aishwarya Agrawal (Virginia Tech)
- Code for API is based on [MSCOCO API code](https://github.com/pdollar/coco)
- The format of the code for Evaluation is based on [MSCOCO evaluation code](https://github.com/tylin/coco-caption)

## Acknowledgement ##
- VQA Team
