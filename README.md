# Seneca
This repository contains code and data for the paper "Morphological Segmentation for Seneca", to appear in AmericasNLP 2021

## Data set construction when evaluating with a development set ##
There are two data sources: a grammar book ([Bardeau 2007](https://senecalanguage.com/wp-content/uploads/Verb-Book-Vol.1.pdf))), and words collected from transcribed informal recordings.

Transcriptions of informal recordings were performed by [Robbie Jimerson](https://www.linkedin.com/in/robertjimersonjr/) (rcj2772@rit.edu)

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
  
  4. crosslingual contains data for a series of cross-linguistic training experiments
  (1) basic is for transfer learning between Seneca and four Mexican indigenous languages from [Kann et al. (2018)](https://www.aclweb.org/anthology/N18-1005.pdf)
  (2) finetune is to fine-tune the model from (1) with in-domain data
  (3) multi-task is for multi-task learning with the four Mexican indigenous languages from [Kann et al. (2018)](https://www.aclweb.org/anthology/N18-1005.pdf)

Data set construction for the informal sources is similar, except that the code is:

```python3 code/segmentation_data.py --input resources/all-forms-from-spreadsheet.txt --output OUTPUT_PATH --lang robbie```

The output organization (e.g folder names) is the same as that for the grammar book described above.



## Data set construction when evaluating with a development domain ##

For this evaluation scheme, I simply did command-line copy, paste, concatenate, etc. The output data is withn the folder ```2/```, and the sub-folders there are named the same ways as described above for each training setting.

## Training/Applying seq2seq morphological segmentation model ##

It is quite simple and straightforward. ```Hooray.ipynb``` contains a run-through of training and applying one segmentation model

All our models trained under different configurations are within each of the specified folders described above.

## Evaluating the output of a model ##

```python3 code/segmentation_eval.py --gold GOLD_FILE --pred PREDICTED_OUTPUT --ex onmt```

All our evaluation results are within each of the specified folders described above.

## Testing a model ##

The ```experiments/test``` folder contains all models and results during the final testing stage.


