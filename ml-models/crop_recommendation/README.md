# crop_recommendation

> A scalable and production-ready **ml_pipeline** project template built with modern MLOps and AI engineering best practices.

## Author

**Siddharth Ganguli**

---

## Overview

This project template is designed to accelerate the development of machine learning and AI applications by providing a clean, modular, and extensible architecture. It supports optional integrations such as APIs, experiment tracking, data versioning, containerization, and CI/CD workflows.

---

## Tech Stack

- **Python 3.10**

- **FastAPI** for REST API development



- **MLflow** for experiment tracking and model management


- **DVC** for dataset and pipeline versioning


- **Docker** for containerized deployment


- **GitHub Actions** for CI/CD automation


---

## Features


- REST API support using FastAPI



- Experiment tracking and model registry


- Data and pipeline version control


- Dockerized environment setup


- Automated testing and deployment workflows

- Modular and scalable folder structure
- Easy customization and extension
- Production-ready project organization

---

## Cloud Configuration

**Selected Cloud Provider:** `aws`


### AWS Services
- Amazon S3
- Amazon EC2
- Amazon SageMaker






---

## Installation

Clone the repository and install dependencies:

```bash
git clone <your-repository-url>
cd crop_recommendation

pip install -r requirements.txt
```

---

## Running the Project

### Run Main Application

```bash
python main.py
```


### Run FastAPI Server

```bash
uvicorn src.crop_recommendation.api.app:app --reload
```





### Run with Docker

```bash
docker-compose up --build
```


---

## Project Structure

```text
crop_recommendation/
│
├── artifacts/         # Generated outputs and artifacts
├── configs/           # Configuration files
├── data/              # Raw and processed datasets
├── deployments/       # Deployment-related scripts and configs
├── docs/              # Project documentation
├── logs/              # Log files
├── models/            # Saved models and checkpoints
├── notebooks/         # Jupyter notebooks
├── reports/           # Reports and analysis outputs
├── src/               # Source code
├── tests/             # Unit and integration tests
│
├── main.py            # Project entry point
├── requirements.txt   # Python dependencies
└── README.md          # Project documentation
```

---

## Development Workflow

1. Create and activate a virtual environment
2. Install dependencies
3. Configure environment variables
4. Start development
5. Run tests before deployment

---

## Testing

Run tests using:

```bash
pytest tests/
```

---

## Best Practices Included

- Clean project architecture
- Environment-based configuration
- Scalable ML engineering workflow
- Reproducible experiments
- Deployment-ready setup
- CI/CD friendly structure

---

## License

This project is licensed under the **MIT License**.

---

## Contributing

Contributions, issues, and feature requests are welcome.

1. Fork the repository
2. Create a feature branch
3. Commit your changes
4. Open a pull request

---

## Contact

**Siddhartha Ganguli**

For questions or collaboration opportunities, feel free to connect.
siddharthaganguli0093@gmail.com 
