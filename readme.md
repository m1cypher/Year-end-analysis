<!-- PROJECT SHIELDS -->
<!--
*** I'm using markdown "reference style" links for readability.
*** Reference links are enclosed in brackets [ ] instead of parentheses ( ).
*** See the bottom of this document for the declaration of the reference variables
*** for contributors-url, forks-url, etc. This is an optional, concise syntax you may use.
*** https://www.markdownguide.org/basic-syntax/#reference-style-links
-->
[![Contributors][contributors-shield]][contributors-url]
[![Forks][forks-shield]][forks-url]
[![Stargazers][stars-shield]][stars-url]
[![Issues][issues-shield]][issues-url]
[![MIT License][license-shield]][license-url]
[![LinkedIn][linkedin-shield]][linkedin-url]



<!-- PROJECT LOGO -->
<br />
<div align="center">
  <a href="https://github.com/m1cypher/Year-end-analysis">
    <img src="images/logo.png" alt="Logo" width="240" height="240">
  </a>

<h3 align="center">Year End Analysis</h3>

  <p align="center">
    project_description
    <br />
    <a href="https://github.com/m1cypher/Year-end-analysis"><strong>Explore the docs »</strong></a>
    <br />
    <br />
    <a href="https://github.com/m1cypher/Year-end-analysis">View Demo</a>
    ·
    <a href="https://github.com/m1cypher/Year-end-analysis/issues">Report Bug</a>
    ·
    <a href="https://github.com/m1cypher/Year-end-analysis/issues">Request Feature</a>
  </p>
</div>



<!-- TABLE OF CONTENTS -->
<details>
  <summary>Table of Contents</summary>
  <ol>
    <li>
      <a href="#about-the-project">About The Project</a>
      <ul>
        <li><a href="#built-with">Built With</a></li>
      </ul>
    </li>
    <li>
      <a href="#getting-started">Getting Started</a>
      <ul>
        <li><a href="#prerequisites">Prerequisites</a></li>
        <li><a href="#installation">Installation</a></li>
      </ul>
    </li>
    <li><a href="#usage">Usage</a></li>
    <li><a href="#roadmap">Roadmap</a></li>
    <li><a href="#contributing">Contributing</a></li>
    <li><a href="#license">License</a></li>
    <li><a href="#contact">Contact</a></li>
    <li><a href="#acknowledgments">Acknowledgments</a></li>
  </ol>
</details>



<!-- ABOUT THE PROJECT -->
## About The Project

In the year 2023, I wanted to keep track of what I did with my year, and what I did at my desk. So I coupled the time keeping I needed to do for my day job along with what I did after work. I was also inspired by [r/dataisbeautiful](https://www.reddit.com/r/dataisbeautiful/comments/193qx1v/2600_hours_at_my_desk_in_2023_with_26_lbs_lost/). 

This is a personal project that will cover my personal notes from [Obsidian](https://obsidian.md) and the time keep application [Timeular](https://https://timeular.com/). I wanted to be able to pull my own statisctics and create my own graphs for Timeular that they already provide as well as chart out some of my daily journal stats.

<img src="images/timeular summary.png" alt="Timeular Summary">
<img src="images/timeular summary per month.png" alt="Timeular Summary per month">
<img src="images/timeular summary per tag.png" alt="Timeular Summary per tag">

<p align="right">(<a href="#top">back to top</a>)</p>



### Built With

* [Python](https://www.python.org/)
* [Jupyter](https://jupyter.org/)

<p align="right">(<a href="#top">back to top</a>)</p>



<!-- GETTING STARTED -->
## Required Information

- API Key and Secret from [Timeular](https://https://timeular.com/) for the Token
  - This does require at least a personal pro account as of late 2023
  - Need the ability to export data (Stupid paywall if you have API access IMO)
- [Obsidian](https://obsidian.md) frontmatter (Now called properties) information.

## Prerequisites
This is an example of how to list things you need to use the software and how to install them.

DotEnv
```sh
pip install python-dotenv
```
Plotly
```sh
pip install plotly
```
Matplotlib
```sh
pip install matplotlib
```
FrontMatter
```sh
pip install python-frontmatter
```
Jupyter
```sh
pip install jupyter
```

## Installation
Below is an example of how you can instruct your audience on installing and setting up your app. This template doesn't rely on any external dependencies or services.

1. Get your Timeular API Key at https://app.timeular.com/#/settings/account or on the App itself and scroll down to the "API" section

2. Clone the repo
```sh
git clone https://github.com/m1cypher/Year-end-analysis.git
```

3. Install Python Modules listed above

4. Execute Jupyter 
```sh
jupyter notebook
``` 
*NOTE* You can either create a .env file to add the API information or just go through the prompts at the beginning of the note to have it all placed in for you. If a ".env" is already created, it will skip those prompts.

<p align="right">(<a href="#top">back to top</a>)</p>


Usage
You would use this to automate the create of yearly stats in your life, assuming you have been collecting them. Maybe post them to r/dataisbeautiful!

For more examples, please refer to the [Documentation](https://github.com/m1cypher/Year-end-analysis/wiki)

<p align="right">(<a href="#top">back to top</a>)</p>





<!-- ROADMAP -->
## Roadmap

- [X] Pull of data from Timeular
- [X] Pull data from Obsidian
- [X] Insert data into Jupyter
- [X] Display data as desired

See the [open issues](https://github.com/m1cypher/Year-end-analysis/issues) for a full list of proposed features (and known issues).

<p align="right">(<a href="#top">back to top</a>)</p>



<!-- CONTRIBUTING -->
## Contributing

Contributions are what make the open source community such an amazing place to learn, inspire, and create. Any contributions you make are **greatly appreciated**.

If you have a suggestion that would make this better, please fork the repo and create a pull request. You can also simply open an issue with the tag "enhancement".
Don't forget to give the project a star! Thanks again!

1. Fork the Project
2. Create your Feature Branch (`git checkout -b feature/AmazingFeature`)
3. Commit your Changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the Branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

<p align="right">(<a href="#top">back to top</a>)</p>



<!-- LICENSE -->
## License

Distributed under the MIT License. See `LICENSE.txt` for more information.

<p align="right">(<a href="#top">back to top</a>)</p>



<!-- CONTACT -->
## Contact

Your Name - [@mimircyber](https://twitter.com/mimircyber) - info@mimircyber.com

Project Link: [https://github.com/m1cypher/Year-end-analysis](https://github.com/m1cypher/Year-end-analysis)

<p align="right">(<a href="#top">back to top</a>)</p>



<!-- ACKNOWLEDGMENTS -->
## Acknowledgments

* []()
* []()
* []()

<p align="right">(<a href="#top">back to top</a>)</p>


<!-- MARKDOWN LINKS & IMAGES -->
<!-- https://www.markdownguide.org/basic-syntax/#reference-style-links -->
[contributors-shield]: https://img.shields.io/github/contributors/m1cypher/Year-end-analysis.svg?style=for-the-badge
[contributors-url]: https://github.com/m1cypher/Year-end-analysis/graphs/contributors
[forks-shield]: https://img.shields.io/github/forks/m1cypher/Year-end-analysis.svg?style=for-the-badge
[forks-url]: https://github.com/m1cypher/Year-end-analysis/network/members
[stars-shield]: https://img.shields.io/github/stars/m1cypher/Year-end-analysis.svg?style=for-the-badge
[stars-url]: https://github.com/m1cypher/Year-end-analysis/stargazers
[issues-shield]: https://img.shields.io/github/issues/m1cypher/Year-end-analysis.svg?style=for-the-badge
[issues-url]: https://github.com/m1cypher/Year-end-analysis/issues
[license-shield]: https://img.shields.io/github/license/m1cypher/Year-end-analysis.svg?style=for-the-badge
[license-url]: https://github.com/m1cypher/Year-end-analysis/blob/master/LICENSE.txt
[linkedin-shield]: https://img.shields.io/badge/-LinkedIn-black.svg?style=for-the-badge&logo=linkedin&colorB=555
[linkedin-url]: https://linkedin.com/in/garrett-e-boyd
[product-screenshot]: images/screenshot.png
