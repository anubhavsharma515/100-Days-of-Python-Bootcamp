# Learnings

This exercise was a hoot. The Turtle module was going to be foundational to a lot of exercises in the upcoming days, but getting it to work on a Mac M1 using the system provided python runtime
was impossible. Debugging this was made easier by this error on every invocation of a python file using the Turtle module:

`DEPRECATION WARNING: The system version of Tk is deprecated and may be removed in a future release. Please don't rely on it. Set TK_SILENCE_DEPRECATION=1 to suppress this warning.`

So, tk. Digging into a few stackoverflow threads (and [this docs site](https://www.python.org/download/mac/tcltk/)), this was a known issue stemming from the tk that comes packaged with the system python version. A little more digging and trial-and-error, the following steps were able to resolve this issue:

## Install tcl-tk

A pre-requisite for this to work was first installing a working version of tcl-tk. This needed to be done before the right version of python was installed as 'python will set the version of tcl-tk already installed, and we don't want that to be the system version'.

```
$ brew install tcl-tk
```

## Install a new python version.

I learnt about `pyenv`! I arbitrarily chose to instal python@3.10.5. I then followed the instructions to set it up locally for this project.

```
$ brew install pyenv
$ pyenv install 3.10.5
$ export PYENV_ROOT="$HOME/.pyenv" \
    [[ -d $PYENV_ROOT/bin ]] && export PATH="$PYENV_ROOT/bin:$PATH" \
    eval "$(pyenv init -)"$ pyenv
$ source ~/.zshrc
```

And that's it! This was a good exercise as it pushed me to figure out an error that was pretty unclear (there wasn't really a single right answer on the internet),
instead of jumping to exercises that don't use Turtle. No Turtle can slow me down.
