## Prerequisites

The `bidsme` toolkit is written in python3. In order to run it, a
[python3 interpreter](https://www.python.org/downloads/), of version 3.6 or later,
must be installed.

The tutorial uses [jupyter notebook ](https://jupyter.org/); this is 
recommended, but not strictly necessary, as all commands can 
be run in terminal directly. 

Both the python3 interpreter and Jupiter-notebook come together with the installation of 
[Anaconda](https://www.anaconda.com/products/individual-b). Anaconda allows to streamline
the usage of `bidsme` on non-terminal oriented platforms (aka Windows).

The `bidsme` should be cloned to the accessible directory, using
the standard git (or any tool of choice):

```bash
cd <working directory>
git clone https://gitlab.uliege.be/CyclotronResearchCentre/Public/bidstools/bidsme/bidsme.git
cd bidsme
```

For now, tutorial exists on `tutorial` branch, it will be merged
th the main branch at some point.
So, don't forget to switch:

```bash
git checkout tutorial
```

All needed steps for installation of dependencies are given in
[installation.ipynb](Installation/installation.ipynb).


## Structure of the tutorial

There several tutorials proposed to familiarise with `bidsme`.
These tutorials aims to introduce the different aspects
of bidsifications, and point to various difficulties that
may arrive during bidsification of a real life dataset.

A typical tutorial is composed of a set of notebooks,
that should be executed in the order,
each following notebook relies on the previous one.

Each tutorial will gide frough the full process
of bidsification, and represents my own approach
to dealling with new datasets to bidsify.

The covered steps are, in order:
  
  - data preparation
  - data mapping
  - data bidsification
  - data preparation using plugins
  - data mapping/bidsification with plugins
  - data manipulation with plugins

Each tutorial is preceeded by a `00-tutorial-paths.ipynb`
notebook.
In this notebook, all the needed paths should be defined,
and it should be run at least once.

### Installlation tutorial

The `Installation` tutorial contains instructions how
to install `bidsme` and it's dependencies,
it should be run at least once, before other tutorials.

The `bidsme_path.ipynb` notebook will define the path
to `bidsme`, together with some utility function(s)
to use with tutorials.

### MRI tutorial

`MRI_tutorial` covers a bidsification process of a
syntetic dataset, which was created to match a real
life complex dataset.

It was designed to cover the majority of isssues
that you may encounter during a bidsification,
and how approach these issues.

The tutorial is quite long, may take up to one day,
but it is important to follow it, in order to have
an extensive overview of `bidsme` features.

As explained in
[MRI_tutorial/00-tutorial-paths.ipynb](./MRI_tutorial/00-tutorial-paths.ipynb),
you need to download the dataset from
[ULiege gitlab](https://gitlab.uliege.be/CyclotronResearchCentre/Public/bidstools/bidsme/bidsme_example).

## Using virtual environments and kernels

`bidsme` will require the installation of some additional python packages, some of them
are very common, like `pandas`, and likely already present in your installation of 
python, others are less common.

In order to keep python installation clean, usage of virtual environments and/or kernels
are suggested.

If you are using \*NIX and/or (Ana)conda, then creating a new envoronment is
straightforward, in terminal you just need to:

**[NIX](https://docs.python.org/3/tutorial/venv.html)**:
```
python3 -m venv bidsme_env
source bidsme_env/bin/activate
``` 

**[Conda](https://docs.conda.io/projects/conda/en/latest/user-guide/tasks/manage-environments.html)**:
```
conda create --name bidsme_env
conda activate bidsme_env
```

In order to deactivate (return to your default) environment, you just need
`deactivate` in \*NIX or `conda deactivate` in conda.

Once the environment is activated you need to install the kernel --
a library that will link iPython/jupyter interface with environment.

Still within the terminal, and active environment, do:
```
pip install ipykernel
python -m ipykernel install --user --name bidsme_env --display-name "bidsme_env (Python)"
```

The first line will install the kernel package, and second will create a new kernel
with internal name `bidsme_env` and displayed name `Python (bidsme_env)`.
For more instructions and details, you can refer to the 
[Kernel instructions](https://ipython.readthedocs.io/en/latest/install/kernel_install.html)

Once kernel is installed, you can open a new jupyter(-lab) notebook, and check if
the new kernel of name `Python (bidsme_env)` is available.

This way all necessary packages will be installed in dedicated virtual environment
and will not create conflicts with your other python projects.

> You must insure that you run all tutorials with the same kernel/environment
