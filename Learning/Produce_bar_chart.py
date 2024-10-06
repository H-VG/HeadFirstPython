import webapp.Swimclub as Swimclub
import webapp.hfpy_utils as hfpy_utils

CHARTS = "Charts/"
def produce_bar_chart(fn):
    (swimmer,age,distance,stroke,*_) = Swimclub.read_swim_data(fn)
    title = f"{swimmer} (Under {age}) {distance} {stroke}"
    html = f"""
    <!DOCTYPE html>
    <html>
        <head>
            <title>{title}</title>
        </head>
        <body>
        <h3>{title}</h3>
    """
    *_, times ,average,converts = Swimclub.read_swim_data(fn)
    from_max = max(converts)
    times.reverse
    converts.reverse
    svgs = ""
    for n,t in enumerate(times):
        bar_width = hfpy_utils.convert2range(converts[n],0,from_max,0,350)
        svgs = svgs +f"""
        <svg height ="30" width="400">
            <rect height="30" width="{bar_width}" style="fill:rgb(0,0,255);" />
        </svg>{t}<br />
        """
    footer = f"""
                <p>Average time: {average}</p>
            </body>
        </html>
        """
    page = html+svgs+footer
    save_to = f"{CHARTS}{fn.removesuffix('.txt')}.html"
    with open(save_to,"w") as sf:
        print(page, file=sf)
        
    return save_to
