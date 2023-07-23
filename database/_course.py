from database.database_connection import conn, cur


def create_table_course():
    cur.execute("""
        Create table IF NOT EXISTS course (
          course_id INTEGER PRIMARY KEY,
          title VARCHAR(255),
          description VARCHAR(255),
          location VARCHAR(255),
          date DATE,                -- YYYY-MM-DD
          start_time DATETIME,      -- HH:MM
          end_time DATETIME,        -- HH:MM
          product_id INTEGER,
          FOREIGN KEY(product_id) REFERENCES product(product_id)
        );
    """)
    conn.commit()


def add_new_course(title, description, location, date, start_time, end_time, product_id):
    cur.execute(f"""
        INSERT INTO course (course_id, title, description, location, date, start_time, end_time, product_id)
        VALUES (null, "{title}", "{description}", "{location}", "{date}", "{start_time}", "{end_time}", {product_id});
    """)
    conn.commit()


def get_all_courses() -> list:
    cur.execute("SELECT * FROM course")
    course_list = []
    for row in cur:
        course_list.append(dict(zip([c[0] for c in cur.description], row)))
    return course_list


def insert_default_courses():
    import json

    with open('./database/res/default_courses.json') as f:
        courses = json.load(f)

    for c in courses:
        add_new_course(
            c["title"],
            c["description"],
            c["location"],
            c["date"],
            c["start_time"],
            c["end_time"],
            c["product_id"]
        )