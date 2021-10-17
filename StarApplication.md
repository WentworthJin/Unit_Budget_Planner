# User Guide for Starting the Application



## Supported System
- <b>Windows</b> [Access the Windows setup guide](#windows-setup-guide)
- <b>MacOS & Linux </b> [Access the Mac setup guide](#macos/linux-setup-guide)

## Software Requirements
- <b>Python</b>: Click [Here](https://www.python.org/downloads/) to download the latest Python
- <b>Node.js</b>: Click [Here](https://nodejs.org/en/download/) to download node.js

<hr><br>

# Windows Setup Guide
![image info](./Resources/windows_icon.png)
<br><hr><br>
## You need to download [Python](https://www.python.org/downloads/) and [Node.js](https://nodejs.org/en/download/)
<br><br>

1. <b>Search 'Power Shell' in search box, and open the Power Shell. </b>

![image info](./Resources/OpenPowershell.png)
<br><br>
2. <b>Copy the following commands in PowerShell, and start the application.</b>
<pre>

cd .\Desktop\

git clone https://github.com/WentworthJin/Unit_Budget_Planner.git

cd .\Unit_Budget_Planner\Unit_Budget\

pip3 install --upgrade pip

python3 -m venv venv

.\venv\Scripts\activate

pip3 install -r .\Python_File\requirements.txt

npm install

npm start
</pre>

3. <b>If you encountered any erroes and the application closed, just re-type 'npm start' in PowerShell</b>
<br><br>
![image info](./Resources/PowerShell_Restartnpm.png)
<br><br>

4. <b>For future use, please open the PowerShell, and copy the following commands</b>

<pre>

cd .\Desktop\Unit_Budget_Planner\Unit_Budget\

.\venv\Scripts\activate

npm start

</pre>

<br><hr><br>

# MacOS/Linux Setup Guide
![image info](./Resources/mac_icon.png) ![image info](./Resources/Linux_icon.ico)
<br><hr><br>
## You need to download [Python](https://www.python.org/downloads/) and [Node.js](https://nodejs.org/en/download/)
<br><br>

1. <b>Hold 'command + space' and search for 'Terminal', and open the Terminal </b>

![image info](./Resources/search_terminal.png)
<br><br>
2. <b>Copy the following commands in Terminal, and start the application.</b>
<pre>

cd Desktop/

git clone https://github.com/WentworthJin/Unit_Budget_Planner.git

cd Unit_Budget_Planner/Unit_Budget/

pip3 install --upgrade pip

python3 -m venv venv

source venv/bin/activate

pip3 install -r ./Python_File/requirements.txt

npm install

npm start
</pre>

3. <b>If you encountered any erroes and the application closed, just re-type 'npm start' in PowerShell</b>
<br><br>
![image info](./Resources/terminal_restart_mpm.png)
<br><br>

4. <b>For future use, please open the Terminal, and copy the following commands</b>

<pre>

cd Desktop/Unit_Budget_Planner/Unit_Budget/

source venv/bin/activate

npm start

</pre>
