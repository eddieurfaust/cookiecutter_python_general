# My Python Project Template

This is a [Cookiecutter](https://github.com/cookiecutter/cookiecutter) template to create a new Python project. It sets up a new project with a `.gitignore`, virtual environment, `pylintrc` from the Google Style Guide, and pre-configured settings for VSCode with pylint and black.

## Features

- `.gitignore` setup for Python
- Virtual environment creation
- pylint and black installation
- `pylintrc` setup following Google Style Guide
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
cookiecutter gh:<eddieurfaust>/my_python_template
```

or locally:

```bash
cookiecutter path/to/your/my_python_template
```

## Post-generation hooks

This template uses post-generation hooks to automate several tasks:

- Create and activate a virtual environment
- Install pylint and black
- Download `pylintrc` from Google Style Guide
- Initialize a Git repository and make an initial commit

### For Windows users

The `post_gen_project.ps1` PowerShell script will be executed. This script also downloads `pylintrc` using `Invoke-WebRequest`.

### For Linux/Mac users

The `post_gen_project.sh` shell script will be executed. This script also downloads `pylintrc` using `wget`.

## Customization

You can modify the `cookiecutter.json` to customize the default values for your project.

## Contributing

Feel free to submit a pull request or create an issue if you find a bug or have a suggestion for improving the template.

## License

MIT License - see the [LICENSE.md](LICENSE.md) file for details.
