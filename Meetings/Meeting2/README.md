# Class Diagram
![io-2 drawio](https://github.com/PiotrLezanski/CodeChecker/assets/91131233/584edc8a-9238-4d63-8a4c-cbdaa7ecc7ac)
# Usecase Diagram
![usecase_diagram](https://github.com/PiotrLezanski/CodeChecker/assets/45331390/6476ba4f-6685-46cf-914c-b3c0501b5870)
# Functional Description
CodeChecker – functional description 

CodeChecker is a powerful application designed to assess the quality and correctness of user’s code. It performs comprehensive code analysis and identifies various types of issues including memory leaks, wrong test outputs, compilation or runtime errors. It can additionally compare two codes in terms of issues or semantic differences. 
 
On the welcome window the user can read brief description of all functionalities and he is given the possibility to change appearance settings, such as size or theme. Additionally the welcome window allows user to upload one or two files with code, which then are stored in the application. 
Sidebar allows user to switch between different views and try other functionalities.

The views and functionalities are as follows: 

- GetOutput – app will run users code with provided input and return the output as a preview and with the possibility to download. 

- CheckEfficiency – user can input his code and a testcase. Additionally, he can choose one or more options of parameters that the program will check, which are: runtime, memory leaks and logs of compilation in general.

- CompareCode – given two codes from the user, the program executes both and gets their efficiency parameters. Differences are displayed as an output. 

- TestPass – the user passes testcases as an input. The application executes the program on these testcases, displaying results and additionally code coverage of the particular testcase. 

- CodeDifference – given two codes from the user, the program will check for semantic differences and will return every place, where the codes are different.

CodeChecker provides user-friendly interface, allowing developer to easily configure the analysis parameters and customize the rule sets according to their project requirements.
