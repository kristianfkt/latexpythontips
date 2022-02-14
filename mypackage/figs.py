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
    standard_size = 4
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

def savefig(fig, name, root='./figs/',  dir=''):
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

    root = pathlib.Path(root).resolve()
    
    pdf  = root.joinpath('pdf').joinpath(dir).joinpath(name+'.pdf')
    png  = root.joinpath('png').joinpath(dir).joinpath(name+'.png')
    pgf  = root.joinpath('pgf').joinpath(dir).joinpath(name+'.pgf')
    tikz = root.joinpath('tikz').joinpath(dir).joinpath(name+'.tikz')

    for p in [pdf, png, pgf, tikz]:
        if not p.parent.exists():
            p.parent.mkdir(parents=True, exist_ok=True)


    
    fig.savefig(pdf, bbox_inches='tight')
    fig.savefig(png, dpi=150)
    fig.savefig(pgf)

    width, height=fig.get_size_inches()
    
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