# pygemini

## Prerequisites

1. Python 3.10+ (can create venv)
2. Set up a Google Cloud project and enable the necessary APIs.

## Installation
Clone the repository:
```sh
git clone https://github.com/yourusername/pygemini.git
cd pygemini
```

Install the required dependencies:
```sh
pip install -e .
```

## Configuration
# Setting Environment Variables
Before running the client, you need to set your Google API key, Project ID, and Region ID. You can do this using the setenv command:

```sh
python main.py setenv --api_key "YOUR_API_KEY" --project_id "YOUR_PROJECT_ID" --region_id "YOUR_REGION_ID"
```
This command will update the .env file with the provided values.

# Loading Environment Variables
The environment variables will be loaded automatically when you run any of the commands below.

# Usage
**Generate Response from Text Prompt**
```sh
python test_function.py prompt "Tell me a story about a brave knight."
```

**Generate Response from Chat Message**
```sh
python test_function.py chat "How do I improve my coding skills?"
```


**Generate Response from Image**
You can provide either a local file path or a URL to an image.

Local file path:

```sh
python test_function.py image "path/to/image.jpg" "Describe the scene in this image."
```

URL:

```sh
python test_function.py image "http://example.com/image.jpg" "Describe the scene in this image."
```

**Generate Response from Video**
You can provide either a local file path or a URL to a video.

Local file path:

```sh
python test_function.py video "path/to/video.mp4" "Summarize the content of this video."
```
URL:

```sh
python test_function.py video "http://example.com/video.mp4" "Summarize the content of this video."
```

# Code Structure

\`**gemini.py**\`

Contains the Gemini class which provides methods for interacting with the Generative AI services.

\`**utils.py**\`

Contains utility functions for loading and setting environment variables.

\`**test_function.py**\`

Provides the command-line interface for setting environment variables and generating responses using the Gemini class.

## Contributing
1. Fork the repository
2. Create a new branch (git checkout -b feature-branch)
3. Make your changes
4. Commit your changes (git commit -am 'Add new feature')
5. Push to the branch (git push origin feature-branch)
6. Create a new Pull Request
   
## License
This project is licensed under the MIT License. See the LICENSE file for details.

## Contact
For any questions or feedback, please contact ....
