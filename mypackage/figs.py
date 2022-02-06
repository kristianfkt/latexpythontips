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
    standard_size = 6
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

    path = pathlib.Path(project)
    if path.exists:
        path.mkdir(parents=True, exist_ok=True)
    
    pdf=path.joinpath(name+'.pdf')
    png=path.joinpath(name+'.png')
    pgf=path.joinpath(name+'.pgf')

    tikz=path.joinpath(name+'.tikz')

    
    fig.savefig(pdf, bbox_inches='tight')
    fig.savefig(png, dpi=100)
    fig.savefig(pgf)

    width,height=fig.get_size_inches()
    rows = fig.get_axes()[0].get_gridspec().nrows
    cols = fig.get_axes()[0].get_gridspec().ncols

    tikzplotlib.save(tikz, 
        axis_width=f'{1/cols}\linewidth',
        axis_height=f'{(height/width)/rows}\linewidth',
        extra_groupstyle_parameters={'vertical sep=4em':None}
    )
    return

if __name__ == '__main__':
    pass