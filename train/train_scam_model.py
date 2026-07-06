import pandas as pd
import os
os.makedirs('models/scam_model', exist_ok=True)

print("Loading datasets...")
train_df = pd.read_csv('data/scamdetect_train.csv')[['label','text']].dropna()
val_df   = pd.read_csv('data/scamdetect_val.csv')[['label','text']].dropna()
print(f"Train: {len(train_df)} | Val: {len(val_df)}")

from transformers import (DistilBertTokenizer,
    DistilBertForSequenceClassification, Trainer, TrainingArguments)
from datasets import Dataset
from sklearn.metrics import accuracy_score, f1_score

tokenizer = DistilBertTokenizer.from_pretrained('distilbert-base-uncased')

def tokenize(batch):
    return tokenizer(batch['text'], truncation=True,
                     padding='max_length', max_length=128)

print("Tokenizing...")
train_ds = Dataset.from_pandas(train_df).map(tokenize, batched=True)
val_ds   = Dataset.from_pandas(val_df).map(tokenize, batched=True)
train_ds = train_ds.rename_column('label','labels').with_format('torch')
val_ds   = val_ds.rename_column('label','labels').with_format('torch')

print("Loading DistilBERT model...")
model = DistilBertForSequenceClassification.from_pretrained(
    'distilbert-base-uncased', num_labels=2)

def compute_metrics(eval_pred):
    logits, labels = eval_pred
    preds = logits.argmax(-1)
    return {
        'accuracy': accuracy_score(labels, preds),
        'f1': f1_score(labels, preds)
    }

args = TrainingArguments(
    output_dir='models/scam_model',
    num_train_epochs=3,
    per_device_train_batch_size=16,
    per_device_eval_batch_size=32,
    eval_strategy='epoch',
    save_strategy='epoch',
    load_best_model_at_end=True,
    metric_for_best_model='f1',
    logging_steps=50,
    report_to='none'
)

print("Training started... (takes 30-45 min)")
trainer = Trainer(
    model=model,
    args=args,
    train_dataset=train_ds,
    eval_dataset=val_ds,
    compute_metrics=compute_metrics
)
trainer.train()

print("Saving model...")
model.save_pretrained('models/scam_model')
tokenizer.save_pretrained('models/scam_model')
print("DONE! Model saved to models/scam_model/")