# AzFuncPyFastApi
Sample Azure function project in Python using FastApi request and Response API along with Azure OpenAI. 

* HttpExample
* HttpExampleStreamed

local.settings.json
----
```
{
  "IsEncrypted": false,
  "Values": {
    "AzureWebJobsStorage": "UseDevelopmentStorage=true",
    "FUNCTIONS_WORKER_RUNTIME": "python",
    "AzureWebJobsFeatureFlags": "EnableWorkerIndexing",
    "PYTHON_ENABLE_INIT_INDEXING": "1"
  },
  "Host": {
    "LocalHttpPort": 7071,
    "CORS": "*"
  }
}
```

local .env file.
----
```
OPENAI_API_TYPE="azure"
OPENAI_API_BASE="example: https://myendpointname.openai.azure.com/"
OPENAI_API_KEY="your key"
OPENAI_API_VERSION="your api version example: 2023-05-15"

AZURE_OPENAI_CHAT_MODEL_DEPLOYMENT_NAME = "gpt-35-turbo-16k"
```

## For SQLAlchemy model generation
* `pip install sqlalchemy-codegen`
* ``` sqlalchemy-codegen postgresql://dbadmin:dbadminpwd@pgsql.postgres.database.azure.com/chatapp --models_layer --outdir temp```