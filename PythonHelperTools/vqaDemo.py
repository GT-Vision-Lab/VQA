# coding: utf-8

from vqaTools.vqa import VQA
#import numpy as np
import random
import skimage.io as io
import matplotlib.pyplot as plt

dataDir='../../VQA'
taskType='OpenEnded'
dataType='mscoco'
dataSubType='train2014'
annFile='%s/Annotations/%s_%s_%s.json'%(dataDir, taskType, dataType, dataSubType)
imgDir = '%s/Images/' %(dataDir)

# initialize VQA api for QA annotations
vqa=VQA(annFile)

# load and display QA annotations for given question types
"""
quesTypes can be one of the following
what color 
what kind 
what are 
what type 
is the 
is this
how many 
are 
does 
where 
is there 
why 
which 
do 
what does 
what time 
who 
what sport 
what animal 
what brand
"""
annIds = vqa.getQuesIds(quesTypes='how many');   
anns = vqa.loadQA(annIds)
randomAnn = random.choice(anns)
vqa.showQA([randomAnn])
imgId = randomAnn['image_id']
imgFilename = 'COCO_train2014_'+ str(imgId).zfill(12) + '.jpg'
I = io.imread(imgDir + imgFilename)
plt.imshow(I)
plt.axis('off')
plt.show()

# load and display QA annotations for given answer types
"""
ansTypes can be one of the following
yes/no
number
other
"""
annIds = vqa.getQuesIds(ansTypes='yes/no');   
anns = vqa.loadQA(annIds)
randomAnn = random.choice(anns)
vqa.showQA([randomAnn])
imgId = randomAnn['image_id']
imgFilename = 'COCO_train2014_'+ str(imgId).zfill(12) + '.jpg'
I = io.imread(imgDir + imgFilename)
plt.imshow(I)
plt.axis('off')
plt.show()

# load and display QA annotations for given images
"""
Usage: vqa.getImgIds(quesIds=[], quesTypes=[], ansTypes=[])
Above method can be used to retrieve imageIds for given question Ids or given question types or given answer types.
"""
ids = vqa.getImgIds()
annIds = vqa.getQuesIds(imgIds=random.sample(ids,5));  
anns = vqa.loadQA(annIds)
randomAnn = random.choice(anns)
vqa.showQA([randomAnn])  
imgId = randomAnn['image_id']
imgFilename = 'COCO_train2014_'+ str(imgId).zfill(12) + '.jpg'
I = io.imread(imgDir + imgFilename)
plt.imshow(I)
plt.axis('off')
plt.show()

