import os

def main():
    lal_data_path = os.environ.get('LAL_DATA_PATH')
    if not lal_data_path:
        lal_data_path = input('Please enter the path for LAL_DATA_PATH: ')
    
    if lal_data_path:
        try:
            # Path to esigma_utils.py
            esigma_utils_path = os.path.join(os.path.dirname(__file__), 'gwnr', 'waveform', 'esigma_utils.py')
            
            # Read the content of esigma_utils.py
            with open(esigma_utils_path, 'r') as file:
                lines = file.readlines()
            
            # Find the index where to insert the LAL_DATA_PATH line
            insert_index = None
            for index, line in enumerate(lines):
                if line.startswith('import'):
                    insert_index = index + 1
            
            if insert_index is not None:
                # Prepare the line to insert
                insert_line = f'\nimport os \nos.environ["LAL_DATA_PATH"] = "{lal_data_path}"\n\n'
                
                # Insert the line into the file content
                lines.insert(insert_index, insert_line)
                
                # Write the updated content back to esigma_utils.py
                with open(esigma_utils_path, 'w') as file:
                    file.writelines(lines)
                
                print(f'LAL_DATA_PATH has been set to: {lal_data_path} in esigma_utils.py')
            else:
                print('Could not find a suitable place to insert the LAL_DATA_PATH line.')
        except Exception as e:
            print(f'An error occurred while modifying esigma_utils.py: {e}')
    else:
        print('LAL_DATA_PATH is not set. Exiting.')

if __name__ == "__main__":
    main()
