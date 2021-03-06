# EchoRecall 🚀🚀
### Machine Learning API using FastAPI and 🤗 cutting-edge transformer model for question generation

- Capstone project for https://ai.science/

## Goal
>To automate the process of generating test questions and flashcards to help teachers quickly create tests and students to generate flashcards. Our aim to to Accelerate learning through active recall and to use NLP to ask great questions.

## Active Recall and spaced repetition
> "As the name suggests, spaced repetition involves spacing your revision and reviewing topics, ideally by active recall, at specific intervals over a period of time. It can be explained by the 'forgetting curve' – an idea that has been around in the psychology literature for over one hundred years."

## Current Model
> Adapted from https://github.com/patil-suraj/question_generation#results

> valhalla/t5-small-qg-hl

## FastAPI
> Documentation: https://fastapi.tiangolo.com
> Source Code: https://github.com/tiangolo/fastapi

## Source tutorial for FastAPI the modified 
> https://www.youtube.com/watch?v=1zMQBe0l1bM
> 
### Startup
```bash
> $ conda create -n ENV_NAME
> $ conda activate ENV_NAME
> $ pip3 install -r requirements.txt
> $ pip3 install -r dev-requirements.txt
> $ uvicorn main:app --reload
```

