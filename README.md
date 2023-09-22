SQL File Splitter
A Python script to split a large SQL file into smaller, manageable chunks. This can be particularly useful when dealing with enormous SQL dumps that need to be imported in parts or processed separately.

Features:
Splits by SQL statements, ensuring each chunk is a valid SQL file on its own.
User-defined number of chunks.
Preserves SQL statement integrity; won't cut off statements in the middle.
Automatic naming of chunks for organization.



Output:
After executing the script, you'll find multiple SQL files in the format chunk_1.sql, chunk_2.sql, etc., in the same directory.
The number of chunks is set to 6 by default. Modify the script if you need a different number of chunks.

Customization:
To adjust the number of chunks or the input SQL file name, modify these lines in the script:

python
input_sql_path = "companies.sql"  # Change to your SQL file name if different.
split_sql_file(input_sql_path, 6)  # Change '6' to your desired number of chunks.

Contributing:
Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

License:
MIT
