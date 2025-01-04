# apa
not the flying bison

## Requirements
- Have Python 3.10 installed;
- Have a Docker engine running;
- Run the script to generate test data:
    `python3 data_script.py`

## Run Greedy Algorithm Test
```
docker image build --tag 'apa:latest' . && docker run --rm --memory=256m apa:latest src/greedy_paradigm.py
```
