import gi

gi.require_version("Gtk", "3.0")
from gi.repository import Gtk

from matplotlib.figure import Figure
from matplotlib.backends.backend_gtk3agg import FigureCanvasGTK3Agg as FigureCanvas

win = Gtk.Window()
win.connect("destroy", Gtk.main_quit)

mf = Figure(figsize=(5,5), dpi=100)
# ax = mf.add_subplot(111, projection='polar')
ax.plot()

sw  = Gtk.ScrolledWindow()
win.add(sw)

can = FigureCanvas(mf)
can.set_size_request(400,400)
sw.add_with_viewport(can)

win.show_all()
Gtk.main()