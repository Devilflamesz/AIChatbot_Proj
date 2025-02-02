# -*- coding: utf-8 -*-
"""Textextraction.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1mL_YERLv7R5Iw2UUyymS21JTxz15VPTH
"""

from google.colab import files
upload = files.upload()

# Commented out IPython magic to ensure Python compatibility.
# %%capture
# !pip install git+https://github.com/neuml/txtai#egg=txtai[pipeline]
# 
# # Get test data
# !wget -N https://github.com/neuml/txtai/releases/download/v6.2.0/tests.tar.gz
# !tar -xvzf tests.tar.gz
# 
# # Install NLTK
# import nltk
# nltk.download('punkt')
# 
# 
#

# Commented out IPython magic to ensure Python compatibility.
# %%capture
# 
# from txtai.pipeline import Textractor
# 
# # Create textractor model
# textractor = Textractor()

textractor = Textractor(paragraphs=True)
for paragraph in textractor("FAQ_Chatbot.csv"):
  print(paragraph, "\n----")

textractor = Textractor(paragraphs=True)
for paragraph in textractor("Summary of Right Classification of NYP Systems.docx"):
  print(paragraph, "\n----")

textractor = Textractor(paragraphs=True)
for paragraph in textractor("sgpresident.txt"):
  print(paragraph, "\n----")

textractor = Textractor(paragraphs=True)
for paragraph in textractor("Guide to Right Classification - NYP ppt v190801.pdf"):
  print(paragraph, "\n----")

textractor = Textractor(paragraphs=True)
for paragraph in textractor("Intake 2 LADP Knowledge Transfer 1 Slides.pptx"):
  print(paragraph, "\n----")