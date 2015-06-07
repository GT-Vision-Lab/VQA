Python API and Evaluation Code for Beta v0.1 sample of the VQA dataset.
===================

This sample of the dataset consists of
- 10k images from COCO training images
- 30k questions (3 per image)
- 300k answers (10 per question)

There are two types of tasks
- Open Ended Task (Questions are open ended)
- Multiple Choice Task (Each question has 18 choices from which the correct answer is to be selected)

## Requirements ##
- python 2.7

## Files ##
./Annotations
- Download annotations files from [here](https://filebox.ece.vt.edu/~cvmlp/vqa//annotations.zip), extract them and place in this folder.
- After download and extraction, this folder should have the following two files  
	- OpenEnded_mscoco_train2014.json (VQA Annotation File for the Open Ended Task)
	- MultipleChoice_mscoco_train2014.json (VQA Annotation File for the Multiple Choice Task)

./Images
- Download Training images from the [MSCOCO website](http://mscoco.org/dataset/#download) and place them here after extracting

./PythonHelperTools
- This directory contains the Python API to read and visualize the VQA dataset
- vqaDemo.py (demo script)
- vqaTools (API to read and visualize data)

./PythonEvaluationTools
- This directory contains the Python evaluation codes
- vqaEvalDemo.py (evaluation demo script)
- vqaEvaluation (evaluation code)

./Results
- OpenEnded_mscoco_train2014_fake_results.json (an example of a fake results file to run the demo)
- Visit [VQA evaluation page] (http://visualqa.org/evaluate) page for more details.

## References ##
- [VQA: Visual Question Answering](http://visualqa.org/)
- [Microsoft COCO](http://mscoco.org/dataset/#download)

## Developers ##
- Aishwarya Agrawal (Virginia Tech)
- Code for API is based on [MSCOCO API code](https://github.com/pdollar/coco)
- The format of the code for evaluation is based on [MSCOCO evaluation code](https://github.com/tylin/coco-caption)
