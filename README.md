# Seneca
This repository contains code and data for the paper "Morphological Segmentation for Seneca", to appear in AmericasNLP 2021

## Data set construction when evaluating with a development set##
There are two data sources: a grammar book (Bardeau 2007), and words collected from transcribed informal recordings.

To constuct data sets for the grammar book, do:

```python3 code/segmentation_data.py --input resources/all-forms-from-spreadsheet.txt --output OUTPUT_PATH --lang grammar```

The data generated this way in our experiments is in 1/grammar/:
  1. baseline contains data used to train the Naive baseline
  2. tuning contains data used to train the Less naive baseline
  3. domain contains data for a series of cross-domain training experiments
  (1) basic is for transfer learning between the two domains / data sources
  (2) finetine is to fine-tune the model from (1) with in-domain data
  (3) self-training is for using additional words from the Bible (in the resource folder) for training
  (4) multi-task is for multi-task learning; to get the data for this configuration in particular, do:
  
      ```python3 code/augmentation.py --input TARGET_TRAINING_FILE --output OUTPUT_PATH --method b --bible resources/Bible_select.txt```
      
      ```python3 code/prep_task.py --input INPUT_DEVELOPMENT_FILE --output OUTPUT_DEVELOPMENT_FILE```
