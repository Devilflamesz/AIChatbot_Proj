import pandas as pd
from sklearn.preprocessing import LabelEncoder
from sklearn.model_selection import train_test_split
from transformers import BertTokenizer, BertForSequenceClassification, Trainer, TrainingArguments
from datasets import Dataset, DatasetDict

# Load your dataset
df = pd.read_csv('email_classification_dataset.csv')

# Encode labels into numerical values
label_encoder = LabelEncoder()
df['label'] = label_encoder.fit_transform(df['label'])
print("Encoded classes:", label_encoder.classes_)

# Split into train and validation sets
train_df, val_df = train_test_split(df, test_size=0.3, random_state=42, stratify=df['label'])

# Convert to Huggingface Dataset
train_dataset = Dataset.from_pandas(train_df)
val_dataset = Dataset.from_pandas(val_df)
dataset = DatasetDict({'train': train_dataset, 'validation': val_dataset})

# Load tokenizer and model
model_name = 'bert-base-uncased'
tokenizer = BertTokenizer.from_pretrained(model_name)
model = BertForSequenceClassification.from_pretrained(model_name, num_labels=len(label_encoder.classes_))

def tokenize_function(examples):
    return tokenizer(examples['email_text'], padding='max_length', truncation=True)

# Tokenize datasets
tokenized_datasets = dataset.map(tokenize_function, batched=True)
tokenized_datasets.set_format('torch')

# Training arguments
training_args = TrainingArguments(
    output_dir='./results',
    num_train_epochs=5,
    learning_rate=1e-5,
    per_device_train_batch_size=8,
    per_device_eval_batch_size=8,
    warmup_steps=500,
    weight_decay=0.01,
    logging_dir='./logs',
)

# Trainer
trainer = Trainer(
    model=model,
    args=training_args,
    train_dataset=tokenized_datasets['train'],
    eval_dataset=tokenized_datasets['validation'],
)

try:
    # Train the model
    trainer.train()

    # Save the fine-tuned model
    model.save_pretrained('./my_finetuned_model')
    tokenizer.save_pretrained('./my_finetuned_model')

except Exception as e:
    print(f"Error during training: {str(e)}")
