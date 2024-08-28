# Social Network API

This is a Django-based social networking API that allows users to sign up, search for other users, send and accept friend requests, and view a list of friends.

## Installation

### Prerequisites
- Docker
- Docker Compose

### Steps

1. Clone the repository:
    bash
    git clone https://github.com/your_username/social_network_api.git
    cd social_network_api
    

2. Build and start the services:
    bash
    docker-compose up --build
    

3. The API will be available at http://localhost:8000/.

### Running Tests

To run tests, execute the following command:

```bash
docker-compose run web python manage.py test