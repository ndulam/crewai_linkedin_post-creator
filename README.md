<p align="center">
    <img alt="img" src="img/img.png" width=400 />
    <h1 align="center">Automating LinkedIn Post</h1>
    <h3 align="center">crewAI automates my LinkedIn Posts </h3>
</p>

---

#pre-requisite
To run the code you need to have python version 3.11 and openai api key,serper api key and linkedin credentials
update the .env file with the api keys and linkedin credentials


## Description 

This repository contains a crewAI application for generating LinkedIn posts automatically. 
The crew consists of [three agents](agents.py):

1️⃣ LinkedIn Scraper Ninja 

It uses a [Selenium custom tool](tools%2Flinkedin.py) to scrape my LinkedIn profile. I need to scrape my
posts since I want some examples for the last agent to emulate my writing style. This tool needs some env variables,
defined in an `.env` file (you can see an example [here](.env)).

2️⃣ Web Researcher

It fetches relevant information about a given topic. In my case, I chose the recent release of Llama3 by Meta AI, but
you can choose whatever you want (you'll need to modify the Tasks and Agents of course ...)

3️⃣ Influencer Agent

This agent has to deal with the information gathered by the two previous agents and write a high quality and engaging 
LinkedIn post emulating my writing style.


<p align="center">
    <img alt="img" src="img/architecture.png" width=400 />
</p>


## Usage

First of all, install the necessary dependencies. Preffered to have python version 3.11

```shell
pip install -r requirements.txt
```
updated .env file with your linkedin credentials

```shell

After all the dependencies are installed, run the `main.py`.

> Keep in mind that you need to have all the necessary env variables in your `.env` file for this to work. Also, if you
want to change the topic of your LinkedIn post, you'll need to modify the Agents and Tasks.

```shell
python3 main.py
```
