# apa
not the flying bison

## Requirements
- Have a Docker engine running;
- Run the script to generate test data:
    ```
    docker image build --tag 'apa:latest' . && docker run --rm --memory=256m -v ./data:/app/data apa:latest src/data_script.py
    ```

## Run Greedy Algorithm Test
```
docker image build --tag 'apa:latest' . && docker run --rm --memory=256m -v ./data:/app/data apa:latest src/greedy_paradigm.py uniform_tasks.csv
```
