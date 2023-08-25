# Django CRUD API Star Wars Planets

This project was developed as a response to a code challenge focused on building a CRUD API using Django. The challenge involved retrieving data from an external GraphQL API, storing it in a database, and creating RESTful endpoints for CRUD operations.

## Challenge Description

The goal of the challenge was to:

1. Retrieve data from an external GraphQL API.
2. Store the data in an appropriate database structure.
3. Create RESTful Create, Read, Update, and Delete endpoints to interact with the database.

## Solution

To address the challenge, the following steps were taken:

1. **Fetching Data from GraphQL API:** I created a custom Django management command that fetches data from the specified GraphQL endpoint. This command can be executed to populate the database with external data. <br><br> In case the GraphQL API is not available, I have included a JSON file with the API's output.
You can find in `graphql_api_output_example.json` file at the root of the project.
<br><br> To run the command, use `python manage.py fetch_data`.

2. **Models:** I created 3 models. Planet, Terrain, and Climate. The Planet model has a many-to-many relationship with the Terrain and Climate models. This allows a planet to have multiple terrains and climates, and a terrain or climate to be associated with multiple planets.

3. **Database:** I worked with the default SQLite database that comes with Django. However, the application can be easily adapted to work with other databases like PostgreSQL, MySQL, Oracle, etc.

3. **Django Rest Framework (DRF):** I used DRF to create the RESTful endpoints for CRUD operations. The endpoints are as follows:
    - **Create:** `POST /api/v1/planets/`
    - **Read:** `GET /api/v1/planets/` and `GET /api/v1/planets/<id>/`
    - **Update:** `PUT /api/planets/<id>/` and `PATCH /api/planets/<id>/`
    - **Delete:** `DELETE /api/planets/<id>/`

## Getting Started

1. Clone this repository.
2. Install the required packages using `pip install -r requirements.txt`.
3. Run migrations using `python manage.py migrate`.
4. Fetch data from GraphQL API using `python manage.py fetch_data`.
5. Start the development server using `python manage.py runserver`.


## Future Work

While the current version addresses the challenge requirements, there are several areas for future improvement and expansion:

- **Documentation:** Create detailed documentation to help developers understand the project and its components. This includes API documentation, docstrings, and code comments.

- **Production Deployment:** Deploy the application to a production environment.

- **Unit Tests:** Implement comprehensive unit tests.

- **Error Handling:** I implemented few error handling. I would like to implement more error handling to ensure that the application is robust.

- **Continuous Integration and Continuous Deployment (CI/CD):** Set up CI/CD pipelines to automate testing and deployment processes.

- **User Authentication and Authorization:** Integrate user authentication and authorization mechanisms for secure API access.

---

**Author:** Juan Echeverri

This project was created as part of a code challenge. For more information, please contact jecheverrigutierrez@gmail.com.