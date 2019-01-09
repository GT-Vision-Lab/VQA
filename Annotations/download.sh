URL=https://s3.amazonaws.com/cvmlp/vqa/mscoco/vqa
TRAIN=v2_Annotations_Train_mscoco.zip
VAL=v2_Annotations_Val_mscoco.zip

if [ ! -f $TRAIN ]; then
    wget $URL/$TRAIN
fi
if [ ! -f $VAL ]; then
    wget $URL/$VAL
fi

unzip $TRAIN
unzip $VAL
