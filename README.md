# E-Commerce Product API

A REST-based Product API built using Python Flask and Docker.

## Technology Stack

* Python 3.13
* Flask
* Docker
* Git
* GitHub

## Application Architecture

```text
Client
   |
   | HTTP :8080
   v
Docker Container
   |
   v
Flask Product API
```

## API Endpoints

| Method | Endpoint         | Description               |
| ------ | ---------------- | ------------------------- |
| GET    | `/health`        | Application health status |
| GET    | `/products`      | Get all products          |
| GET    | `/products/<id>` | Get a product by ID       |
| POST   | `/products`      | Add a product             |
| PUT    | `/products/<id>` | Update a product          |
| DELETE | `/products/<id>` | Delete a product          |

## Environment Variables

| Variable | Description                                 | Example |
| -------- | ------------------------------------------- | ------- |
| APP_ENV  | Application environment                     | test    |
| DB_HOST  | Database host/future database configuration | test-db |
| APP_PORT | Application port                            | 8080    |

## Build Docker Image

```bash
docker build -t ecommerce-product-api:1.0 .
```

## Run Docker Container

```bash
docker run -d \
  --name ecommerce-product-api-container \
  -p 8080:8080 \
  -e APP_ENV=test \
  -e DB_HOST=test-db \
  -e APP_PORT=8080 \
  ecommerce-product-api:1.0
```

## Health Check

Open:

```text
http://localhost:8080/health
```

## Test Product API

### Add Product

```bash
curl -X POST http://localhost:8080/products \
-H "Content-Type: application/json" \
-d '{"name":"Laptop","price":75000}'
```

### View Products

```bash
curl http://localhost:8080/products
```

### View Product

```bash
curl http://localhost:8080/products/1
```

### Update Product

```bash
curl -X PUT http://localhost:8080/products/1 \
-H "Content-Type: application/json" \
-d '{"name":"Gaming Laptop","price":90000}'
```

### Delete Product

```bash
curl -X DELETE http://localhost:8080/products/1
```

## Stop Container

```bash
docker stop ecommerce-product-api-container
```

## Remove Container

```bash
docker rm ecommerce-product-api-container
```

## Project Flow

```text
Client
  |
  v
Host Port 8080
  |
  v
Docker Container Port 8080
  |
  v
Flask Product API
  |
  +---- /health
  |
  +---- /products
  |
  +---- /products/<id>
```

## Docker Configuration

The application configuration is supplied through environment variables instead of being hard-coded into the application.

The Docker image can be reused to create multiple containers with the same application behavior.
