## Note!
All the software is written in the simplest DDD approach.
MongoDB is chosen over PostgreSQL for more agile and fast development (though it's subjectively).

## How to?
1. Create mongo db instance using mongo_create.sh script.
2. Start mongo db instance using mongo_start.sh script.
3. Mutate and seed initial data using `python3 cli.py db seed` command.
4. Run tests using `python3 cli.py test`. You may also use `--coverage` flag to make coverage report accordingly.
5. Start server using `python3 cli.py start` command.



