"""
Create kudos table
"""

from yoyo import step

__depends__ = {}

steps = [
    step("""
         CREATE TABLE kudos (
            id serial,
            kudo text
         );
         """),
    step("""
         INSERT INTO kudos (kudo) VALUES ('Awesome job learning AIO!');
         """),
]
