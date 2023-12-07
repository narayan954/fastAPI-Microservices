# Project Overview

This project consists of an inventory management system with a frontend built using React and Vite, and two backend services built using FastAPI and Redis. The frontend communicates with the backend services to manage products and orders.

## Frontend

The frontend is a React application that uses Vite for a faster and leaner development experience. It uses the @vitejs/plugin-react-swc plugin for fast refresh. The application is styled using Bootstrap and custom CSS.

The application consists of several components:

- Products: Displays a list of products and allows deleting a product.
- CreateProducts: Provides a form to create a new product.
- Orders: Allows placing an order for a product.

The application uses React Router for navigation between these components.

To run the frontend, use the following commands:


## Backend

The backend consists of two services: inventory and payment. Both services are built using FastAPI and use Redis as a database.

The inventory service manages products. It provides endpoints to create, retrieve, and delete products.

The payment service manages orders. It provides endpoints to create and retrieve orders. When an order is created, it is initially marked as "pending". A background task then marks the order as "completed".

To run each backend service, you need to create a virtual environment, activate it, install the dependencies, and then run the application. The commands are as follows:

## Git Ignore

The .gitignore file is set up to ignore common files and directories that should not be committed to the repository. This includes Python compiled files, virtual environments, logs, and IDE-specific files.

## Linting

The project uses ESLint for linting the JavaScript code. The configuration for ESLint is in the .eslintrc.cjs file.

## Note

Please ensure that you have Node.js, Python, and Redis installed on your machine before running the project. Also, update the .env file with the correct Redis connection details.

