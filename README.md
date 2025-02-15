
<!-- <h1 align="center">
  <br>
  <a href="http://www.amitmerchant.com/electron-markdownify"><img src="https://raw.githubusercontent.com/amitmerchant1990/electron-markdownify/master/app/img/markdownify.png" alt="Markdownify" width="200"></a>
  <br>
  Markdownify
  <br>
</h1>

<h4 align="center">A minimal Markdown Editor desktop app built on top of <a href="http://electron.atom.io" target="_blank">Electron</a>.</h4>

<p align="center">
  <a href="https://badge.fury.io/js/electron-markdownify">
    <img src="https://badge.fury.io/js/electron-markdownify.svg"
         alt="Gitter">
  </a>
  <a href="https://gitter.im/amitmerchant1990/electron-markdownify"><img src="https://badges.gitter.im/amitmerchant1990/electron-markdownify.svg"></a>
  <a href="https://saythanks.io/to/bullredeyes@gmail.com">
      <img src="https://img.shields.io/badge/SayThanks.io-%E2%98%BC-1EAEDB.svg">
  </a>
  <a href="https://www.paypal.me/AmitMerchant">
    <img src="https://img.shields.io/badge/$-donate-ff69b4.svg?maxAge=2592000&amp;style=flat">
  </a>
</p>

<p align="center">
  <a href="#key-features">Key Features</a> •
  <a href="#how-to-use">How To Use</a> •
  <a href="#download">Download</a> •
  <a href="#credits">Credits</a> •
  <a href="#related">Related</a> •
  <a href="#license">License</a>
</p>

![screenshot](https://raw.githubusercontent.com/amitmerchant1990/electron-markdownify/master/app/img/markdownify.gif) -->

<h3 align="center">
  <a href="https://drive.google.com/drive/folders/1cRpE48WuzvNL2ulp7dlx_5jeWnp0vrvi?usp=sharing">Poster</a> 
  <!-- <a href="https://opendrivelab.com/e2ead/UniAD_plenary_talk_slides.pdf">Slides</a> -->
</h3>

## Google HPS Porgram

* The Google Hardware Product Sprint (HPS) program is a summer initiative designed for university students interested in hardware product design.

* The program aims to equip participants with knowledge and practical skills in the consumer electronics industry through hands-on projects, product design, system integration, and prototype testing.

<!-- [KaTeX](https://khan.github.io/KaTeX/) Support -->

## Smart Fridge
* We decided to design "Smart Fridge" as our product.
* Our smart refrigerator helps users efficiently manage food storage and reduce waste while optimizing energy consumption. By tracking expiration dates, sending timely reminders, and suggesting recipes, it ensures food is used before spoiling. Additionally, its automatic door-closing feature prevents unnecessary energy loss, making it both convenient and eco-friendly.

* ### The part I am responsible for:
    * Utilized Python to integrate with the Google Gemini API
    * Crafted professional prompts for Gemini to recognize foods accurately and return the required JSON format output
    * Received JSON information from the Food Management Control Panel and interacted with Gemini through Python to generate recommended recipes

## The Overall Structure
* `/using_gemini/test_images/` : The folder that contains images for food recognition testing. 
* `/using_gemini/vision_gemini_test.py` : The file for food recognition using Google Gemini.
* `/using_gemini/generate_recipe.py` : The file for recipe generation using Google Gemini.


## How To Use

This repository is only for the food recognition part of the project. To clone and run this application, you'll need to follow the command lines shown below: 

```bash
# Clone this repository
$ git clone https://github.com/waynechu1109/Google_HPS_Smart_Fridge_-Food-Recognition-.git

# Go into the repository
$ cd Google_HPS_Smart_Fridge_-Food-Recognition-

# Create a conda environment with Python 3.10 and activate it
$ conda create --name [env_name] python=3.10
$ conda activate [env_name]

# Install all the packages needed to run this repository
$ pip install requirements.txt

# To do food recognition using testing images
$ python3 using_gemini/vision_gemini_test.py

# To generate recipe
$ python3 using_gemini/generate_recipe.py
```
<!-- 
## Prompt
* The prompt for food recognition using Google Gemini is shown below:
```bash
prompt_text = (
    f"Below are the details extracted from an image that has already been analyzed:\n"
    f"Text in the image: {extracted_text}\n"
    f"The following foods were identified in the image: {', '.join(object_descriptions)}.\n"
    f"Please be very specific in identifying **exact food names** (such as 'scrambled egg' instead of generic terms like 'food').\n"
    f"Based on the image, provide the name of the food with **precise identification**, "
    f"and format the response as a JSON object (make sure the indentation is correct). "
    f"For each food, list the top {num_kind} kinds of food with the highest confidence percentages, along with their respective expiry dates or estimated storage days.\n"
    f"Make sure the food names are **clear and commonly recognized**, avoiding generic terms like '食物' or 'food.'\n"
    f"Moreover, include the **exact total quantity** of each kind of food, without breaking it down into different types or varieties.\n"
    f"For example, if the image contains 3 oranges, regardless of their specific types, the response should be:\n"
    f"object: [{{'text': 'orange', 'quantity': '3', 'confidence': '90%'}}]\n"
    f"For foods without packaging, provide estimated storage days based on your knowledge, treating the food as fresh. "
    f"If no expiry date is available, estimate the storage days based on general knowledge.\n"
    f"Each response should be **detailed and concise**, focusing solely on the requested information.\n"
    f"Output format:\n"
    f"1. 'object': Array of {{'text': '<name of the food>', 'quantity': '<quantity>', 'confidence': '<confidence percentage>'}}\n"
    f"2. 'expiry': Array of {{'text': '<expiry date (MUST be in the format of **MM/DD/YYYY**) or number of storage days>', 'type': 'days' or 'date', 'confidence': '<confidence percentage>'}}\n"
    f"3. 'location': Array of {{'object': {{'text': '<location description>', 'confidence': '<confidence percentage>'}}}}\n"
    f"The length of all the arrays **must be exactly {num_kind}** to match the number of top foods identified.\n"
    f"Ensure that the JSON response is structured accordingly, without any additional information beyond what is requested.\n"
    f"Additionally, please **DO NOT include** ```json and ``` at the beginning and the end of your response. Thank you.\n"
    f"Responses must be provided in Traditional Chinese and ensure there is an empty line between each section in the response.\n"
    f"Before finalizing the response, ensure that you have only included the total count for each food type, without specifying different varieties."
)

``` -->
## Poster
* You can find the poster of our Smart Fridge <a href="https://drive.google.com/drive/folders/1cRpE48WuzvNL2ulp7dlx_5jeWnp0vrvi?usp=sharing">here</a>. 


<!-- ## Download

You can [download](https://github.com/amitmerchant1990/electron-markdownify/releases/tag/v1.2.0) the latest installable version of Markdownify for Windows, macOS and Linux.

## Emailware

Markdownify is an [emailware](https://en.wiktionary.org/wiki/emailware). Meaning, if you liked using this app or it has helped you in any way, I'd like you send me an email at <bullredeyes@gmail.com> about anything you'd want to say about this software. I'd really appreciate it! -->

## Credits

<!-- This software uses the following open source packages: -->

- [Google Gemini](https://gemini.google.com/app)
<!-- - [Node.js](https://nodejs.org/)
- [Marked - a markdown parser](https://github.com/chjj/marked)
- [showdown](http://showdownjs.github.io/showdown/)
- [CodeMirror](http://codemirror.net/)
- Emojis are taken from [here](https://github.com/arvida/emoji-cheat-sheet.com)
- [highlight.js](https://highlightjs.org/) -->

<!-- ## Related

[markdownify-web](https://github.com/amitmerchant1990/markdownify-web) - Web version of Markdownify -->

<!-- ## Support

<a href="https://buymeacoffee.com/amitmerchant" target="_blank"><img src="https://www.buymeacoffee.com/assets/img/custom_images/purple_img.png" alt="Buy Me A Coffee" style="height: 41px !important;width: 174px !important;box-shadow: 0px 3px 2px 0px rgba(190, 190, 190, 0.5) !important;-webkit-box-shadow: 0px 3px 2px 0px rgba(190, 190, 190, 0.5) !important;" ></a>

<p>Or</p> 

<a href="https://www.patreon.com/amitmerchant">
	<img src="https://c5.patreon.com/external/logo/become_a_patron_button@2x.png" width="160">
</a> -->

<!-- ## You may also like...

- [Pomolectron](https://github.com/amitmerchant1990/pomolectron) - A pomodoro app
- [Correo](https://github.com/amitmerchant1990/correo) - A menubar/taskbar Gmail App for Windows and macOS

## License

MIT

---

> [amitmerchant.com](https://www.amitmerchant.com) &nbsp;&middot;&nbsp;
> GitHub [@amitmerchant1990](https://github.com/amitmerchant1990) &nbsp;&middot;&nbsp;
> Twitter [@amit_merchant](https://twitter.com/amit_merchant) -->

