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