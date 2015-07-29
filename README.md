Python API and Evaluation Code for Beta v0.9 release of the VQA dataset.
===================

This release of the dataset consists of
- 82783 COCO training images and 40504 COCO validation images
- 248349 questions for training and 121512 questions for validation (3 per image)
- 2483490 answers for training and 1215120 answers for validation (10 per question)

There are two types of tasks
- Open-ended task
- Multiple-choice task (18 choices per question)

## Requirements ##
- python 2.7
- scikit-image (visit [this page](http://scikit-image.org/docs/dev/install.html) for installation)
- matplotlib (visit [this page](http://matplotlib.org/users/installing.html) for installation)

## Files ##
./Annotations
- Download annotations files from [here](https://vision.ece.vt.edu/vqa/data/July_Release/Annotations.zip), extract them and place in this folder.
- After download and extraction, this folder should have the following two files  
	- OpenEnded_mscoco_train2014.json
	- OpenEnded_mscoco_val2014.json
	- MultipleChoice_mscoco_train2014.json
	- MultipleChoice_mscoco_val2014.json 
- Annotations files from Beta v0.1 release (10k MSCOCO images, 30k questions, 300k answers) can be found [here](https://vision.ece.vt.edu/vqa/data/teaser_data/annotations.zip).

./Images
- Create a directory with name train2014, download training images from [MSCOCO website](http://mscoco.org/dataset/#download), place training images in train2014 folder after extracting
- Create a directory with name val2014, download validation images from [MSCOCO website](http://mscoco.org/dataset/#download), place validation images in val2014 folder after extracting

./PythonHelperTools
- This directory contains the Python API to read and visualize the VQA dataset
- vqaDemo.py (demo script)
- vqaTools (API to read and visualize data)

./PythonEvaluationTools
- This directory contains the Python evaluation code
- vqaEvalDemo.py (evaluation demo script)
- vqaEvaluation (evaluation code)

./Results
- OpenEnded_mscoco_train2014_fake_results.json (an example of a fake results file to run the demo)
- Visit [VQA evaluation page] (http://visualqa.org/evaluation) for more details.

## References ##
- [VQA: Visual Question Answering](http://visualqa.org/)
- [Microsoft COCO](http://mscoco.org/)

## Developers ##
- Aishwarya Agrawal (Virginia Tech)
- Code for API is based on [MSCOCO API code](https://github.com/pdollar/coco)
- The format of the code for evaluation is based on [MSCOCO evaluation code](https://github.com/tylin/coco-caption)
