# Setting up a working environment

## Installing `conda`
We are going to install *Miniconda* using the installer from [here](https://docs.conda.io/en/latest/miniconda.html). If you are using Windows you should download the file `Miniconda3 Windows 64-bit`; if you are using MacOS you are likely to download `Miniconda3 macOS Intel x86 64-bit pkg`.

**Windows**:
- double click the `.exe` file previously downloaded, and follow the instructions on the screen - leaving the default values untouched. [More info here](https://conda.io/projects/conda/en/stable/user-guide/install/windows.html)

**MacOS**:
- double click the `.pkg` file previously downloaded, and follow the instructions on the screen - leaving the default values untouched. [More info here](https://conda.io/projects/conda/en/stable/user-guide/install/macos.html)

If the `pkg` file is not working, download the `bash` one instead, then open a terminal (through Launchpad, search for `terminal`) and in the terminal write the following command followed by Enter
`cd Download`

Next, write the following command followed by Enter, and follow the instructions:
`bash Miniconda3-latest-MacOSX-x86_64.sh`

Once installed,[start `conda` in Windows or MacOS](https://docs.conda.io/projects/conda/en/latest/user-guide/getting-started.html#starting-conda):
- Windows: From the Start menu, search for and open "Anaconda Prompt."
- MacOS: Open Launchpad, then click the terminal icon.

Verify that `conda` is installed by writing the following the terminal and then pressing Enter:

> `conda list`

If a list appears, then `conda` is working! Now install `pip` by writing the command below, followed by Enter:

> `conda install -c conda-forge pip`

Beware: the installation will take a while...

## Installing the other tools
Now that `conda` is installed, we need to install the tools for processing our data. This is done with the following command, written in the Anaconda prompt/terminal and followed by Enter:

`pip install jupyterlab beautifulsoup4 lxml yt-dlp`

Once installation is finished, write the following command:
`jupyter lab`

## Getting our data
Now that we have all the tools ready, we can download the data using `yt-dlp`:

`yt-dlp -a LIST_OF_URL.txt --write-info-json --skip-download --write-subs --write-auto-subs --sub-langs en --sub-format srv3`

and then we can extract it to XML and TXT files using the [`subs_to_xml.ipynb`](https://github.com/mdic/dh2023/blob/main/03_15032023/subs_to_xml.ipynb) script.

## Including different metadata
Metadata from the JSON file is included using the syntax exemplified in `lines 12-13` (`block 3`); try to add different metadata data-points to your final corpus!

```{python}
# Add a set of metadata points as attributes of the <text> element tag
text_tag.attrib["date"] = metadata_file["upload_date"]
text_tag.attrib["title"] = metadata_file["fulltitle"]
```

note: the basic structure is
`NAME OF THE ATTRIBUTE IN THE OUTPUT = NAME OF THE ATTRIBUTE IN THE INPUT`
