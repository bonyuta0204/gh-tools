
# gh-tools

GitHub tools for managing and exporting GitHub repository data.

## Features

- Export pull request comments to CSV format.

## Installation

You can install the required dependencies using `poetry`.

### Using poetry

```sh
poetry install
```

## Usage

Set your GitHub access token to the environment variable `GH_TOKEN`.

```sh
export GH_TOKEN=your_github_token
```

### Export Pull Request Comments

To export pull request comments from a repository, use the following command:

```sh
poetry run python3 -m gh_tools.cli pr-comment list <repository>
```

Replace `<repository>` with the repository name in the format `owner/repo`.

## Configuration

The project configuration is managed using `setup.cfg` and `pyproject.toml`.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.
