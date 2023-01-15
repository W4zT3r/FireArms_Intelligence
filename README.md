# Firearms intelligence through MISP

## Project Description

### Contains

This repository contains the source code for a web scraping project aimed at collecting information on firearms from various online sources and representing them in the format of MISP (Malware Information Sharing Platform). The files in the [old](https://github.com/bribrizoo/FireArms_Intelligence/tree/main/old) folder are the initial JSON files we created in an attempt to represent firearms in MISP.

As we were unsure of the differences between the various data representation models on the platform, we generated a JSON file for each model representing a firearm. We first created a galaxy with three clusters representing three models of firearms. Then we created a taxonomy with examples of data. Finally, we attempted to create an object template for a firearm.

Testing and asking for feedback, we realized that the galaxy model was the best choice. Therefore, we decided to create a galaxy for each type of weapon. Each galaxy will contain [clusters](https://github.com/bribrizoo/FireArms_Intelligence/tree/main/clusters) that represent all the weapon models of the category that we were able to scrape. To automate the process we created several scripts, including one that takes as input a firearm model (described as a Python dictionary) and adds it to the corresponding cluster.

Please note that this project is for grading purposes only, and the files in the "old" folder will be removed once the project has been graded.

### Overview

This repository contains the source code for a web scraping project aimed at collecting information on firearms from various online sources. Our initial focus was on websites such as [ImpactGuns](https://www.impactguns.com/) and [ModernFirearm](https://modernfirearms.net/en/), as they proved to be the most comprehensive. However, we encountered difficulties in extracting the desired data due to the dynamic nature of the sites.

We also attempted to scrape data from the official websites of firearm manufacturers such as [Glock](https://eu.glock.com/en), [Smith & Wesson](https://www.smith-wesson.com/), and [Kalashnikov](https://en.kalashnikovgroup.ru/). However, the pages were generated with JavaScript, making it difficult to extract the information using traditional web scraping tools such as BeautifulSoup.

In addition, we also looked into other sources such as Wikipedia and national firearms registries (SIA and Canadian firearms registry) but were unable to gather the required information.

### Final decision

Despite these challenges, we plan to continue working on this project and will be using ImpactGuns as our primary source for data collection and clustering.

## Depedencies

To use our scrapping codes, you need to have python3 and the BeautifulSoup library installed on your machine. 

#### MacOS
```bash
brew install python 3.x
pip3 install BeautifulSoup
```
#### Linux
```bash
sudo apt-get install python3.x
pip3 install BeautifulSoup
```

## Usage

We recommande to launch all programs in a specific folders inspite of the high number of file generated. The generation can take an hour, be patient :)  

```python

# Launch
python3 <programs>.py
