# Python testing example

## Install

1) **Create venv**
    ``` 
    python -m venv .venv
    ```
    Enter the env: 
    ``` 
    // Windows
    .venv/Scripts/Activate.ps1

    // Linux / Max
    source .venv/bin/activate
    ```
2) **Install dependencies**
    ``` 
    pip install -r requirements.txt
    ```

## Run Fastapi server
``` 
uvicorn main:app --reload
```

## Run tests
``` 
pytest
```