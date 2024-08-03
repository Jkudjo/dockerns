you can place your dockerns.py script in a directory like /usr/local/bin to make it accessible from anywhere on your system without specifying the full path. Here’s how you can do that:

Steps to Add Your Script to /usr/local/bin
Move the Script to /usr/local/bin

First, you need to move the dockerns.py script to /usr/local/bin. You can do this with the following command:

sh
Copy code
sudo mv dockerns.py /usr/local/bin/dockerns
Note that the file is being renamed to dockerns without the .py extension. This makes it easier to run the script from the terminal.

Make the Script Executable

Ensure the script has executable permissions:

sh
Copy code
sudo chmod +x /usr/local/bin/dockerns
Update the Script to Handle No .py Extension

Since the script will be executed without the .py extension, ensure it has a proper shebang line at the top:

python
Copy code
#!/usr/bin/env python3
This line tells the system to use the Python 3 interpreter to run the script.

If you need to edit the script, you can do so with:

sh
Copy code
sudo nano /usr/local/bin/dockerns
Run the Script from Anywhere

You should now be able to run the script from any terminal session without needing to specify the full path:

sh
Copy code
dockerns
Summary
Move the Script: Place the script in /usr/local/bin for global access.
Make Executable: Ensure the script is executable with chmod +x.
Update Shebang: Make sure the script starts with #!/usr/bin/env python3 for proper execution.
Run the Script: Execute the script from anywhere using its name.
By following these steps, you'll be able to conveniently run your dockerns script from any location in your terminal.
