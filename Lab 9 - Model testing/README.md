
# MLOps Lab: Model Testing and Deployment

## Introduction
This lab focuses on the practical aspects of model testing and deployment in the field of Machine Learning Operations (MLOps). It covers various techniques and tools used for effectively deploying and monitoring machine learning models.

## Contents
- `main.py` - Main script for model training and evaluation.
- `saved_model.ipynb` - Jupyter notebook detailing the model saving process.
- `locust_file.py` - Load testing script using Locust.
- `MLOps - Model Testing.pdf` - Documentation and guidelines for the lab.

## Installation and Setup
Follow these steps to set up your environment for running the lab:
1. Clone the repository.
2. Install required dependencies: `pip install -r requirements.txt`
3. Set up your environment variables as needed.

## Usage
To run the main script, use the following command:
```bash
python main.py
```
For the Jupyter notebook, ensure you have Jupyter Lab or Notebook installed and run it from your local server.

## Screenshots
- Screenshot 1: ![View Screenshot](https://cdn.discordapp.com/attachments/1191490101247758479/1193692594161582130/image.png)
- Screenshot 2: ![View Screenshot](https://cdn.discordapp.com/attachments/1191490101247758479/1193732911137050634/Screenshot_from_2024-01-08_02-46-03.png)
- Screenshot 3: ![View Screenshot](https://cdn.discordapp.com/attachments/1191490101247758479/1193733299143725146/Screenshot_from_2024-01-08_02-49-31.png)





## Performance Metrics of FastAPI Service

| Metric                      | Value                      |
|-----------------------------|----------------------------|
| Endpoint                    | /question_answering (POST) |
| Number of Requests          | 4843                       |
| Failure Rate                | 0.00%                      |
| Average Response Time       | 2253 ms (2.25 s)           |
| Min Response Time           | 24 ms                      |
| Max Response Time           | 7738 ms (7.74 s)           |
| Median Response Time        | 2300 ms                    |
| Throughput                  | 30.17 requests/sec         |
| **Response Time Percentiles** |                            |
| 50% (Median)                | 2300 ms                    |
| 66%                         | 3000 ms                    |
| 75%                         | 3200 ms                    |
| 80%                         | 3300 ms                    |
| 90%                         | 3400 ms                    |
| 95%                         | 3800 ms                    |
| 98%                         | 4300 ms                    |
| 99%                         | 4600 ms                    |
| 99.9%                       | 6400 ms                    |
| 99.99%                      | 7700 ms                    |
| 100%                        | 7700 ms                    |

### Interpretation
- **Consistency:** Most of the requests (99.99%) were served within 7700 milliseconds (approximately 7.7 seconds), indicating that the service is consistent for almost all requests.
- **Performance:** The median response time is 2300 milliseconds (approximately 2.3 seconds), suggesting that half of the requests were processed within this time. However, the 99.9th percentile indicates that a small fraction of requests (0.1%) took up to 6400 milliseconds (approximately 6.4 seconds), which might be a concern depending on the application's requirements.
- **Throughput:** The service handled a throughput of 30.17 requests per second without any failures, indicating that it can handle a moderate load effectively.

In conclusion, the FastAPI service appears to be performing well with consistent response times and a decent throughput rate. However, monitoring and optimization might be needed if faster response times are required for all percentiles or if higher throughputs are expected.
