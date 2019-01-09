URL=http://images.cocodataset.org/zips
TRAIN=train2014.zip
VAL=val2014.zip
TEST=test2015.zip

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
