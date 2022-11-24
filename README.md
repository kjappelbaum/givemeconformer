<!--
<p align="center">
  <img src="https://github.com/kjappelbaum/givemeconformer/raw/main/docs/source/logo.png" height="150">
</p>
-->

<h1 align="center">
  givemeconformer
</h1>

<p align="center">
    <a href="https://github.com/kjappelbaum/givemeconformer/actions?query=workflow%3ATests">
        <img alt="Tests" src="https://github.com/kjappelbaum/givemeconformer/workflows/Tests/badge.svg" />
    </a>
    <a href="https://github.com/cthoyt/cookiecutter-python-package">
        <img alt="Cookiecutter template from @cthoyt" src="https://img.shields.io/badge/Cookiecutter-python--package-yellow" /> 
    </a>
    <a href="https://pypi.org/project/givemeconformer">
        <img alt="PyPI" src="https://img.shields.io/pypi/v/givemeconformer" />
    </a>
    <a href="https://pypi.org/project/givemeconformer">
        <img alt="PyPI - Python Version" src="https://img.shields.io/pypi/pyversions/givemeconformer" />
    </a>
    <a href="https://github.com/kjappelbaum/givemeconformer/blob/main/LICENSE">
        <img alt="PyPI - License" src="https://img.shields.io/pypi/l/givemeconformer" />
    </a>
    <a href='https://givemeconformer.readthedocs.io/en/latest/?badge=latest'>
        <img src='https://readthedocs.org/projects/givemeconformer/badge/?version=latest' alt='Documentation Status' />
    </a>
    <a href='https://github.com/psf/black'>
        <img src='https://img.shields.io/badge/code%20style-black-000000.svg' alt='Code style: black' />
    </a>
</p>

Does only one thing. Only one command. That's it. 
Only helps me to have [dkoes script](https://github.com/dkoes/rdkit-scripts/blob/master/rdconf.py) as command. 

## 💪 Getting Started

> TODO show in a very small amount of space the **MOST** useful thing your package can do.
Make it as short as possible! You have an entire set of docs for later.

### Command Line Interface

The givemeconformer command line tool is automatically installed. It can
be used from the shell with the `--help` flag to show all subcommands:

```shell
$ givemeconformer --help
```


## 🚀 Installation

<!-- Uncomment this section after your first ``tox -e finish``
The most recent release can be installed from
[PyPI](https://pypi.org/project/givemeconformer/) with:

```bash
$ pip install givemeconformer
```
-->

The most recent code and data can be installed directly from GitHub with:

```bash
$ pip install git+https://github.com/kjappelbaum/givemeconformer.git
```

To install in development mode, use the following:

```bash
$ git clone git+https://github.com/kjappelbaum/givemeconformer.git
$ cd givemeconformer
$ pip install -e .
```

## 👐 Contributing

Contributions, whether filing an issue, making a pull request, or forking, are appreciated. See
[CONTRIBUTING.rst](https://github.com/kjappelbaum/givemeconformer/blob/master/CONTRIBUTING.rst) for more information on getting involved.

## 👋 Attribution
This tool is based on  [dkoes script](https://github.com/dkoes/rdkit-scripts/blob/master/rdconf.py).

### ⚖️ License

The code in this package is licensed under the MIT License.

<!--
### 📖 Citation

Citation goes here!
-->

<!--
### 🎁 Support

This project has been supported by the following organizations (in alphabetical order):

- [Harvard Program in Therapeutic Science - Laboratory of Systems Pharmacology](https://hits.harvard.edu/the-program/laboratory-of-systems-pharmacology/)

-->

<!--
### 💰 Funding

This project has been supported by the following grants:

| Funding Body | Program                                                                                                                       | Grant         |
| ------------ | ----------------------------------------------------------------------------------------------------------------------------- | ------------- |
| DARPA        | [Automating Scientific Knowledge Extraction (ASKE)](https://www.darpa.mil/program/automating-scientific-knowledge-extraction) | HR00111990009 |
-->

### 🍪 Cookiecutter

This package was created with [@audreyfeldroy](https://github.com/audreyfeldroy)'s
[cookiecutter](https://github.com/cookiecutter/cookiecutter) package using [@cthoyt](https://github.com/cthoyt)'s
[cookiecutter-snekpack](https://github.com/cthoyt/cookiecutter-snekpack) template.

## 🛠️ For Developers

<details>
  <summary>See developer instrutions</summary>

  
The final section of the README is for if you want to get involved by making a code contribution.

### ❓ Testing

After cloning the repository and installing `tox` with `pip install tox`, the unit tests in the `tests/` folder can be
run reproducibly with:

```shell
$ tox
```

Additionally, these tests are automatically re-run with each commit in a [GitHub Action](https://github.com/kjappelbaum/givemeconformer/actions?query=workflow%3ATests).

### 📦 Making a Release

After installing the package in development mode and installing
`tox` with `pip install tox`, the commands for making a new release are contained within the `finish` environment
in `tox.ini`. Run the following from the shell:

```shell
$ tox -e finish
```

This script does the following:

1. Uses BumpVersion to switch the version number in the `setup.cfg` and
   `src/givemeconformer/version.py` to not have the `-dev` suffix
2. Packages the code in both a tar archive and a wheel
3. Uploads to PyPI using `twine`. Be sure to have a `.pypirc` file configured to avoid the need for manual input at this
   step
4. Push to GitHub. You'll need to make a release going with the commit where the version was bumped.
5. Bump the version to the next patch. If you made big changes and want to bump the version by minor, you can
   use `tox -e bumpversion minor` after.
</details>
