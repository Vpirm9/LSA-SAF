# template_nb


## Description
Following template_nb.ipynb is encouraged to use for further presentations of Jupyter notebooks (NB) in the Eumetsat style.
Additional refinements are welcome. 

## Usage of notebooks
Jupyter notebooks are a set of markdown and code cells. To use them follow the next steps:

* [1. - Install jupyter or Jupyter lab](https://jupyter.org/install)
* [2. - Create environment with libraries](https://docs.conda.io/projects/conda/en/latest/user-guide/tasks/manage-environments.html)
In order to run jupyter notebooks one need to create environment from evironment.yml file 
```
conda env create -f evnironment.yml
```

In our case use the environment from Adam platform `adam_env.yml`

* [3. - Run jupyter notebook](https://docs.jupyter.org/en/latest/running.html)
Jupyter lab seems to be a more feature rich and preferd option IMHO.
```
jupyter notebook name_of_notebook.ipynb
jupyter-lab &
```

## Development

It is mostly followed by the already existing notebooks at [Eumetsat Train Hub](https://catalog.trainhub.eumetsat.int/).
It try to stick to the following *guiding principles*

### Guiding principles for preparing NB
1. **Follow the literate programming paradigm by a text/code ration of 3**
 *  evenly distribute text trough entire NB to document all code cells
 *  divide workflow into shorter subsections 
2. **Use instructional design elements to improve navigation and user experience**
 *  leverage HTML/Markdown elements that serve as instructional design elements
 *  elements to use: header, navigation pane, alert boxes ( course section and prerequisites) 
 *  add introduction section and NB outline with anchor links
3. **Modularize functions to follow best practices for scientific computing**
 *  imports at the beginning of NB,
 *  consistent code style and formatting,
 *  using meaningful names for variables and the modularization of content
 *  modularization of repetitive code i.e. downloading, pre-processing and visualization
4. **Leverage the wider Jupyter ecosystem to make content accessible**
5. **Aim for being reproducible**
 *  machine and human readable instructions for the data, computing environment and dependencies are required


For any further explanations of layout the following texts are recommended:
* [Guiding principles to NB](https://www.mdpi.com/2072-4292/14/14/3359)
* [Best practices for Collaboration vith NB](https://arxiv.org/pdf/2202.07233.pdf)
* [Benefits of NB in classroom](https://sci-hub.st/10.1145/3368308.3415397)

---

### CLEAR THE nb OUTPUT

Since the output of Jupyter notebook cells are often some graphics that change often it is not advisable to track that with git while developing.
However outputs can be added at the end of development cycle. 
There are some options how to delete output cells
 1. Inside the Jupyter lab under view chose without output and save file like that before commit.

 2. Make **pre-commit hook** that parses the output of a cell out.
```
conda install -c conda-forge pre-commit

```
To list all available commands type **pre-commit help**.
To get pre-commit hook sample type:
```
pre-commit sample-config > .pre-commit-config.yaml
```
Modify file according to your desired actions that will happen at the time of committing.
For purpose of pre commit hooks
```
# this is .pre-commit-config.yaml

repos:
- repo: https://github.com/kynan/nbstripout
  rev: 0.6.1
  hooks:
    - id: nbstripout
```

Install pre-commit 
```
pre-commit install
```
Inside .pre-commit-config.yaml we specified nbstripout that needs to be installed
```
conda  install -c conda-forge nbstripout
```

After running the commit it will execute tests defined in pre-commit-config.yaml for us i.e nbstripout
If it has to delete the outpus it modifies the staged file and the user has to add and commit again.
To ignor hook `--no-verify` flag is added.

```
git commit -am '' --no-verify
```

In case of many test exluding just one can be done with
```
SKIP=nbstripout git commit -m ''
```



### Share commits offline or via email

Idea is to update repositroy R1 with another repository R2 in case you do not have direct access for some reason.
It is possible to transfere git objects with git bundle.

Detailed info of the `bundle`, a way of transferring git objects locally is available [here](https://git-scm.com/docs/git-bundle.html)


To create a git bundle composed of several commits or just all commits on a your branch at R2 repo.
```
git bundle create name.bundle main..your_branch_name
```
To create a git bundle composed of entire directory
```
git bundle create name.bundle main..your_branch_name
```

Send or move name.bundle file to mashine with R1 repo. Just do not put it in the same repo, that contains .git directory. (can be within downloads etc..)

On R1 verify if everything is ok with .bundle

```
git bundle verify
```
Dodaš bundle kot novi remote file
```
git remote add bundle name.bundle 
```
Fetchas vse kar je novega iz bundla
```
git remote update bundle 
```
Setup remote branch locally with all updates if we use pull it will try to make merge aswell
```
git checkout --track bundle/your_branch_name
```

## Authors and acknowledgment
ARSO team:
Vid Primožič,
Ahac Pazlar,
Boštjan Muri,

