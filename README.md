# apa
not the flying bison

## Experiment Setup

### Build the Docker Image
```
docker image build --tag 'apa:latest' .
```

### Generate the Test data
```
docker run --rm --memory=256m -v ./data:/app/data apa:latest src/data_script.py
```


## Run the Greedy Algorithm
```
docker run --rm --memory=256m -v ./data:/app/data apa:latest src/greedy_paradigm.py uniform_tasks.csv
```

```
docker run --rm --memory=256m -v ./data:/app/data apa:latest src/greedy_paradigm.py normal_distribution_tasks.csv
```
