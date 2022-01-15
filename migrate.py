from yoyo import read_migrations
from yoyo import get_backend
import os
import urllib.parse as urlparse


DATABASE_URL = os.getenv("DATABASE_URL")

#url = urlparse.urlparse(DATABASE_URL)
#car_holder_bot = "/carholder"
#bot_db_path = url._replace(path=car_holder_bot)
#bot_db_path = urlparse.urlunparse(bot_db_path)


def main():

    #backend = get_backend(bot_db_path)
    backend = get_backend(DATABASE_URL)
    migrations = read_migrations("./migrations")

    with backend.lock():
        backend.apply_migrations(backend.to_apply(migrations))
    print("migrations are done")


if __name__ == "__main__":
    main()
