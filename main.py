# Import the transcription_module as tm
import transcription_module as tm
from dotenv import load_dotenv
load_dotenv()
# Define the input and output folders
input_folder = 'files/Scripts'      # Path name of the folder where scripts generated by the DRL-MOBTEST tool are stored
output_folder = 'files/Transcriptions' # Path name where you want the transcriptions to be saved

# Main script execution
if __name__ == "__main__":
    # Call the_world_is_our function from the transcription_module
    tm.the_world_is_our(input_folder=input_folder,
                         output_folder=output_folder)
