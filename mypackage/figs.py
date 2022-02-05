import pathlib
import matplotlib.pyplot as plt
import tikzplotlib

def style():
    #Can also return your own stylesheet
    return plt.style.use('default')

def figsize(width=1, height=1):
    """
    Return a tuple defining figure-size based on a standard size
    """
    standard_size = 8
    return (width*standard_size, height*standard_size)

def square(scale=1):
    """
    Return square figure. Scaled to scale
    """
    return figsize(width=scale, height=scale)

def rectangle(scale=1):
    """
    Return golden mean rectangular figure. width=1, height=0.62
    """
    return figsize(width=scale, height=0.62*scale)

def savefig(fig, name, project='./figs/'):
    """
    Save figure to as many formats as you want to project folder. 
    Consider separating figs into:
        ./figs/png_low/,
        ./figs/png_high/,
        ./figs/pdf/,
        ./figs/tikz/,
        etc
    for full flexibility of formats and quality
    """

    #Make sure tight_layout is applied
    fig.tight_layout()

    path = pathlib.Path(project)
    if path.exists:
        path.mkdir(parents=True, exist_ok=True)
    
    pdf=path.joinpath(name+'.pdf')
    png=path.joinpath(name+'.png')
    tikz=path.joinpath(name+'.tex')
    
    fig.savefig(pdf, bbox_inches='tight')
    fig.savefig(png, dpi=100) #Fast latex compilation
    tikzplotlib.save(tikz)
    return

if __name__ == '__main__':
    pass