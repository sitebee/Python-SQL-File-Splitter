def split_sql_file(input_file, num_chunks):
    """
    Split a large SQL file into smaller chunks.
    
    Args:
    - input_file (str): Path to the input SQL file.
    - num_chunks (int): Number of chunks to split the file into.
    """
    
    with open(input_file, 'r', encoding='utf-8-sig') as file:
        content = file.read()
        statements = content.split(';')  # Assuming each SQL statement ends with a semicolon

        # Calculate the number of statements per chunk
        statements_per_chunk = len(statements) // num_chunks
        
        for i in range(num_chunks):
            start_index = i * statements_per_chunk
            end_index = (i + 1) * statements_per_chunk if i != num_chunks - 1 else len(statements)
            
            chunk_content = ';'.join(statements[start_index:end_index])
            
            # Write to a new chunk file
            with open(f"chunk_{i+1}.sql", 'w', encoding='utf-8-sig') as chunk_file:
                chunk_file.write(chunk_content)

    print(f"File split into {num_chunks} chunks!")

if __name__ == "__main__":
    # Define your input SQL file name/path here:
    input_sql_path = "companies.sql"
    
    split_sql_file(input_sql_path, 6)
