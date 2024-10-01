# svs_to_tif_converter
A useful python based tool to convert .svs to .tif file. Currently there is an issue with the Bioformats importer in FIJI as a result it is not possible to convert the .svs file to .tif file. This tools utilizes the openslide package to do the conversion and the good part is thqt there is no compression during the conversion so no data loss issue.

# Steps to Run the SVS to TIF Converter

1. **Unzip the Elif_final.zip File**  
   Unzip the `Elif_final.zip` file to a directory of your choice. Then, open the Anaconda prompt and navigate to that directory using the following command:  
   ```bash
   cd path/to/your/folder
   ```

2. **Create the Virtual Environment**  
   Create a virtual environment using the provided `.yml` file, which contains the necessary packages. Run the following command:  
   ```bash
   conda env create -f environment.yml
   ```

3. **Copy the OpenSlide Folder**  
   From the `Elif_final` folder, copy the `openslide` folder to the C drive. After copying, copy the path of the `bin` folder inside the `openslide` folder. The path may look something like this:  
   ```
   C:\Openslide\bin
   ```  
   Open the `svs2tif.py` file in any code editor (e.g., VS Code, Spyder, Atom, Notepad++). Change the file path of the OpenSlide DLL directory in the following line:  
   ```python
   # Add the directory containing the OpenSlide DLLs to the PATH
   os.add_dll_directory(r'C:\Openslide\bin')
   ```  
   **IMPORTANT:** Make sure you save the `svs2tif.py` file after making this change.

4. **Activate Your Environment**  
   Open the Anaconda prompt and activate your environment with the following command:  
   ```bash
   conda activate svs2tif
   ```  
   **Tip:** To check the list of environments, use:  
   ```bash
   conda env list
   ```  
   To deactivate your environment, simply type:  
   ```bash
   deactivate
   ```

5. **Run the Script**  
   To run the script from the command line, navigate to the same directory as your Python script after activating the environment, and use the following command:  
   ```bash
   python svs2tif.py --input folder/path/to/input --output folder/path/to/output
   ```
