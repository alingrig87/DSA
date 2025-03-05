# Github Codespaces Setup

## Overview
This repository is designed to work with GitHub Codespaces and supports multiple programming languages. It provides a structured environment for algorithmic problem-solving with predefined project structures.

## What is GitHub Codespaces?
GitHub Codespaces is a cloud-based development environment that allows you to run and develop projects directly from your browser. It provides:
- A fully configured development environment
- Integrated VS Code experience
- Support for multiple programming languages
- Automatic setup with dependencies

## How to Use GitHub Codespaces
1. Open the GitHub repository.
2. Click on the **Code** button.
3. Select **Codespaces** and click **Create codespace on main**.
4. Wait for the environment to be initialized.
5. Start coding directly in your browser.

## What is a Fork?
A **fork** is a personal copy of a repository that allows you to experiment with changes without affecting the original project. Forking enables you to:
- Work on open-source projects
- Submit pull requests to the main repository
- Maintain your own version of a project

## How to Fork a Repository
1. Go to the original repository on GitHub.
2. Click the **Fork** button in the top-right corner.
3. Select your GitHub account as the destination.
4. Wait for GitHub to create a copy under your account.

## How to Commit Solutions for Each Exercise
To contribute solutions to exercises, follow these steps:

### 1. Create a new codespace on main
On newly create fork page go to Code -> Codespaces -> Create codespace on main
![alt text](image.png)

### 2. Create a New Branch
```sh
git checkout -b branch_name
```

### 3. Add Your Solution
Modify or create the necessary files inside the appropriate folder (e.g., `dataStructures/arrays/`).

### 4. Commit Your Changes
```sh
git add .
git commit -m "Added solution for problem X"
```

### 5. Push Your Changes
```sh
git push origin my-solution
```

### 6. Create a Pull Request
1. Go to your forked repository on GitHub.
2. Click on **Compare & pull request**.
3. Provide a description of your changes.
4. Click **Create pull request** to submit your contribution.

## Supported Languages
The following programming languages are supported:
- **C++** (`cpp`)
- **Java** (`java`)
- **JavaScript** (`js`)
- **Python** (`python`)

## Installation & Setup
To install dependencies and set up the project structure for a specific language, use the following command:

```sh
./setup.sh <cpp|java|js|python>
```

### Examples
To install the environment for C++:
```sh
./setup.sh cpp
```
For Java:
```sh
./setup.sh java
```
For JavaScript:
```sh
./setup.sh js
```
For Python:
```sh
./setup.sh python
```


## Project Structure
The project creates a structured directory system based on `project_structure.json`. The folder structure includes common data structures and complexity categories:
- `complexities/` - Examples of O(n) complexity algorithms
- `dataStructures/arrays/` - Common array problems
- `dataStructures/linkedList/` - Linked list operations
- `dataStructures/hashTables/` - Hash table implementations
- `dataStructures/sets/` - Set operations
- `dataStructures/queues/` - Queue implementations
- `dataStructures/stacks/` - Stack implementations
- `dataStructures/bst/` - Binary search tree operations
- `dataStructures/heaps/` - Heap operations

Each file inside these directories will have the appropriate extension for the chosen language (e.g., `.cpp` for C++, `.java` for Java, `.js` for JavaScript, `.py` for Python).

## Cleaning Up Project Structure
To remove all generated files and folders, use:

```sh
make clean
```

This command will delete all created directories and files based on `project_structure.json`.

## Notes
- Ensure you have `make` installed on your system.
- The script automatically installs required dependencies for the chosen language.
- Running `make clean` will remove all generated files and directories.

## Contribution
Feel free to modify `project_structure.json` to add more categories or exercises.

Happy coding! 🚀

