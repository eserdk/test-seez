# Seez backend exercise

We would like you to solve a small problem, so we can assess among many things:

- your code style,
- how you structure code, and
- how you design your solutions

## The assignment

You are given some CSV files of cars for sale and the connected car configurations data (make, models and submodels).
A car has a make,
a make has many models, and
a model has many submodels.


1) Unpack the files and have a look around.
2) Using a database of your choice, insert the data into a schema design, that you think makes sense - you are expected to some reasonable assumptions about the underlying data model
3) Build an API using Python3 with endpoints that return JSON responses - the endpoints should include the following:
   - List all makes, models, and submodels
   - List all cars with their matching make, model and submodel names
   - Add new cars and enforce consistency of the inserted data directly in the database
   - Query cars within a certain price and mileage and return a list of matches sorted by `updated_at` (where the newest element is first)
     - Include the car names here as well
     - Make sure to validate user input and provide meaningful responses when input is wrong.
4) Unit test each of your endpoints to verify your implementation

### Notes and comments

Any external libraries, Docker, and the likes are allowed.

Please hand in _all_ code needed for the above as well as instructions on how to run and use it.
