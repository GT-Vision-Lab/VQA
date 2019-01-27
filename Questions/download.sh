URL=https://s3.amazonaws.com/cvmlp/vqa/mscoco/vqa
TRAIN=v2_Questions_Train_mscoco.zip
VAL=v2_Questions_Val_mscoco.zip
TEST=v2_Questions_Test_mscoco.zip

if [ ! -f $TRAIN ]; then
    wget $URL/$TRAIN
fi
if [ ! -f $VAL ]; then
    wget $URL/$VAL
fi
if [ ! -f $TEST ]; then
    wget $URL/$TEST
fi

unzip $TRAIN
unzip $VAL
unzip $TEST
