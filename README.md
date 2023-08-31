# My Python Project Template

This is a [Cookiecutter](https://github.com/cookiecutter/cookiecutter) template for setting up a new Python project. It includes a `.gitignore`, virtual environment, `.pylintrc` based on the Google Style Guide, and pre-configured settings for VSCode with pylint and black.

## Features

- `.gitignore` configured for Python
- Virtual environment creation
- pylint and black installation
- `.pylintrc` configured according to Google Style Guide
- VSCode settings for Python development
- Initial Git commit

## Requirements

- Python 3.x
- Cookiecutter
- Git
- VSCode (Optional)

## Usage

To generate a new project:

```bash
cookiecutter gh:eddieurfaust/my_python_template
```

or locally:

```bash
cookiecutter path/to/your/my_python_template
```

## Post-generation Hooks

This template utilizes a single post-generation Python script (`post_gen_project.py`) to automate several tasks:

- Create and activate a virtual environment
- Install pylint and black
- Download `pylintrc` from Google Style Guide
- Initialize a Git repository and make an initial commit

### For All Operating Systems

The `post_gen_project.py` Python script will be executed, taking care of the tasks mentioned above regardless of your operating system.

## Customization

You can modify the `cookiecutter.json` to customize default values for your project.

## Contributing

Feel free to submit a pull request or create an issue if you find a bug or have a suggestion for improving the template.

## License

MIT License - see the [LICENSE.md](LICENSE.md) file for details.
