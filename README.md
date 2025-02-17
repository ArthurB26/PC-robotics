
# Ollama on Github Codespaces
These are the instructions for running the Deepseek AI model on Ollama via Github.
You need to have a Github account.

    from ollama import chat
    from ollama import ChatResponse
    
    ainput = input("YOU: ")
    response: ChatResponse = chat(model='llama3.2', messages=[
      {
        'role': 'user',
        'content': ainput,
      },
    ])
    print(response.message.content)
    ]1


INSTRUCTIONS FOR ABOVE: https://github.com/ollama/ollama-python

## Recommended: Setting up Python for Github Codespaces

> Note: (These steps are not necessary but are extremely recommended as they improve the Python experience)

Github codespaces come with Python 3.12.1 pre-installed, but in order to use it properly use it we need to install some things.

## Install the Python extensions in VS Code
Click on the three squares in the left corner to open up the extensions tab, this is where you can see and install all of your extensions.
We are not going to install them this way but if you want to you can.

To install the necessary Python extensions start by clicking `CRTL + SHIFT + E` to open the explorer.
Click the little new file button and in the menu that pops up type `test.py`. Make sure the .py part is there.
Then you will get a notification asking "Do you want to install the recommended python extensions?", here you click install and wait for the extensions to install.

Now you can start writing your first Python script!

## 1.0 Make Github account
You need to have a Github account first.

## 2.0 Make repository
Create a new Github repository. With a readme file
![Create a repository](https://media.geeksforgeeks.org/wp-content/uploads/20190826235103/4-155.png)

## 3.0 Make codespace for the repo 
(Make sure that the virtual machine is set to 4-core cpu and 16gb ram for better performance)
In the repository click on the code button and then code spaces.

Click the 3 dots on the top right.

Then click + New with options….
![Create a codespace](https://docs.github.com/assets/cb-49943/images/help/codespaces/who-will-pay.png)

Then select 4-core and set the region to the closest to you.
![Codespace configuration](https://docs.github.com/assets/cb-66206/images/help/codespaces/advanced-options.png)

Then click Create Codespace and you will see something like this:
![Github Codespace](https://miro.medium.com/v2/resize:fit:2000/1*pdjvVy5sFGCXnqaXewaBQw.png)


## 4.0 Open a Terminal
The terminal is at the bottom as shown below:
![Codespace terminal](https://preview.redd.it/github-codespaces-terminal-theme-v0-y2h9b1l51e6d1.png?width=985&format=png&auto=webp&s=bbfeed331981a7b038e82e9b716a58c227d487c5)


## 5.0 Install Ollama
Run this command in the terminal:

    curl -fsSL https://ollama.com/install.sh | sh

You will get:

## 6.0 Test the Installation
Run:
ollama -h

Gives:

    Usage:
      ollama [flags]
      ollama [command]
    
    Available Commands:
      serve       Start ollama
      create      Create a model from a Modelfile
      show        Show information for a model
      run         Run a model
      stop        Stop a running model
      pull        Pull a model from a registry
      push        Push a model to a registry
      list        List models
      ps          List running models
      cp          Copy a model
      rm          Remove a model
      help        Help about any command
    
    Flags:
      -h, --help      help for ollama
      -v, --version   Show version information
    
    Use "ollama [command] --help" for more information about a command.

## 7.0 Run the Ollama Server
At the command line run:

    ollama serve

You should see something like this:



Now that ollama server is running in the terminal, open another terminal. To open another terminal click on the + at the top right.

Listing the Available Models:
To get a list of the available models type:

     ollama list

    NAME             ID              SIZE      MODIFIED      
    llama3:latest    365c0bd3c000    4.7 GB    3 minutes ago    


## 8.0 Now Run the Model llama3
In the new terminal run the llama3 model by typing:

    ollama run llama3

Once its running and ready for commands you will see:



Now that its running you can type messages to it by entering them on the command line and pressing Enter. For example to say hi type:	

    hi
	
It returns:

    Hello! How may I help you today?



## 9.0 Commands You can Use in the Model
These are some commands you can use while in the model.
Type /? To see a list of commands.

	/?
	
Returns:

    Available Commands:
      /set            Set session variables
      /show           Show model information
      /load <model>   Load a session or model
      /save <model>   Save your current session
      /clear          Clear session context
      /bye            Exit
      /?, /help       Help for a command
      /? shortcuts    Help for keyboard shortcuts
    
    Use """ to begin a multi-line message.

## 9.1 Exiting the model
To exit the model type:

	 /bye

## 10.0 Using Python with Ollama on Github
You can run Python programs that interact with the model being run by OIlama.

See: https://github.com/ollama/ollama-python

## 10.1 Prerequisites
We already have Ollama running  from step 8 above.

Ollama should be installed and running
Pull a model to use with the library: `ollama pull <model>` e.g. `ollama pull llama3.2`
See ollama.com for more information on the models available.


## 10.2 First Install Ollama in Python with Pip:
Run this command in the terminal:

    pip install ollama

This will give something like this:




## 10.3 Create a new Python Program
In the VScode window click the new file icon shown below:



Type in a file name for the new file:



## 10.4 Install the Needed Python Extension
When  the popup below appears click on the Install button.



You will see the below which means it installed successfully.



Close the tab.


## 10.5 Add the Example Python Code
In this program we ask the illama3.2 model: "Why is the sky blue?"

And add the code below:

    from ollama import chat
    from ollama import ChatResponse
    
    response: ChatResponse = chat(model='llama3.2', messages=[
      {
        'role': 'user',
        'content': 'Why is the sky blue?',
      },
    ])
    print(response['message']['content'])

Or access fields directly from the response object

    print(response.message.content)


Your code window will look like this:



## 10.6 Load the llama3.2 Model as the Program uses it
We need to load the illama3.2 model. At the terminal run:

    ollama pull llama3.2

Which gives:




## 10.7 Run the Program
Run the program by clicking on the play icon on the right side as shown below:



It may take a while to run but eventually you should see something like:



The text version is:

    The sky appears blue because of a phenomenon called scattering, which occurs when sunlight interacts with the tiny molecules of gases in the Earth's atmosphere. Here's a simplified explanation:
    
    1. **Sunlight enters the atmosphere**: When sunlight enters the Earth's atmosphere, it encounters tiny molecules of gases such as nitrogen (N2) and oxygen (O2).
    2. **Scattering occurs**: These gas molecules scatter the shorter (blue) wavelengths of light more than the longer (red) wavelengths. This is known as Rayleigh scattering, named after the British physicist Lord Rayleigh, who first described it in the late 19th century.
    3. **Blue light is scattered in all directions**: As a result of the scattering, the blue light is dispersed in all directions, reaching our eyes from every part of the sky.
    4. **Red light continues straight**: Meanwhile, the longer wavelengths of light (such as red and orange) are less affected by the scattering process and continue traveling in a more direct path to our eyes.
    5. **Our eyes see the blue sky**: When we look at the sky, our eyes detect the scattered blue light, which is why it appears blue.
    
    It's worth noting that this phenomenon also explains why sunsets often appear orange or reddish: during this time, the sun's rays have to travel through more of the Earth's atmosphere, scattering off even more molecules and taking on a longer wavelength. This results in the shorter wavelengths (like blue) being absorbed, leaving mainly the longer wavelengths (like red) to reach our eyes.
    
    In conclusion, the sky appears blue because of the scattering of sunlight by tiny gas molecules in the atmosphere, which favors the shorter wavelengths of light.
    The sky appears blue because of a phenomenon called scattering, which occurs when sunlight interacts with the tiny molecules of gases in the Earth's atmosphere. Here's a simplified explanation:
    
    1. **Sunlight enters the atmosphere**: When sunlight enters the Earth's atmosphere, it encounters tiny molecules of gases such as nitrogen (N2) and oxygen (O2).
    2. **Scattering occurs**: These gas molecules scatter the shorter (blue) wavelengths of light more than the longer (red) wavelengths. This is known as Rayleigh scattering, named after the British physicist Lord Rayleigh, who first described it in the late 19th century.
    3. **Blue light is scattered in all directions**: As a result of the scattering, the blue light is dispersed in all directions, reaching our eyes from every part of the sky.
    4. **Red light continues straight**: Meanwhile, the longer wavelengths of light (such as red and orange) are less affected by the scattering process and continue traveling in a more direct path to our eyes.
    5. **Our eyes see the blue sky**: When we look at the sky, our eyes detect the scattered blue light, which is why it appears blue.
    
    It's worth noting that this phenomenon also explains why sunsets often appear orange or reddish: during this time, the sun's rays have to travel through more of the Earth's atmosphere, scattering off even more molecules and taking on a longer wavelength. This results in the shorter wavelengths (like blue) being absorbed, leaving mainly the longer wavelengths (like red) to reach our eyes.
    
    In conclusion, the sky appears blue because of the scattering of sunlight by tiny gas molecules in the atmosphere, which favors the shorter wavelengths of light.

Clear the terminal by typing:

	clear

## 10.8 Automatic ollama start and stop
Use the following code to automatically run and stop Ollama:

    from ollama import chat
    from ollama import ChatResponse
    import ollama
    import subprocess
    import atexit
    
    #Run ollama in the background
    ollama_process = subprocess.Popen(["ollama", "serve"], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
    
    
    AIinput = input("YOU: ")
    ollama.create(model='example', from_='llama3.2', system="Example prompt")
    
    
    response: ChatResponse = chat(model='example', messages=[
      {
        'role': 'user',
        'content': AIinput,
      },
    ])
    print(response.message.content)




## Clean the forwarded ports and stop ollama once the script is done

    def cleanup():
        print("\nStopping Ollama...")
        ollama_process.terminate()
        try:
            ollama_process.wait(timeout=5)
        except subprocess.TimeoutExpired:
            ollama_process.kill()
        subprocess.run("kill -9 $(lsof -t -i:11434)", shell=True, check=False)
    
    atexit.register(cleanup)
