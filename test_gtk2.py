from cProfile import label
import gi
import usb.core

gi.require_version("Gtk", "3.0")
from gi.repository import Gtk

class test_instrument(Gtk.Window):
    def __init__(self):
        super().__init__(title="Automated Testing")

        self.set_border_width(10)

        self.panel1 = Gtk.Frame(label="Device 1")
        self.panel2 = Gtk.Frame(label="Device 2")
        self.panel3 = Gtk.Frame(label="Device 3")
        self.panel4 = Gtk.Frame(label="Device 4")

        self.panel1.set_label_align(0.5,0.5)
        self.panel2.set_label_align(0.5,0.5)
        self.panel3.set_label_align(0.5,0.5)
        self.panel4.set_label_align(0.5,0.5)

        # self.panel1.connect("clicked", self.on_button_clicked)
        # self.panel2.connect("clicked", self.on_button_clicked)
        # self.panel3.connect("clicked", self.on_button_clicked)
        # self.panel4.connect("clicked", self.on_button_clicked)

        grid = Gtk.Grid(column_homogeneous=True,row_homogeneous=True,column_spacing=10,row_spacing=10)
        grid.attach(self.panel1,0,0,1,1)
        grid.attach(self.panel2,1,0,1,1)
        grid.attach(self.panel3,0,1,1,1)
        grid.attach(self.panel4,1,1,1,1)

        self.add(grid)

        # inside each frame
        device_list = ["OWON SPE6103","OWON HDS272S","OWON XDM2041","KOOLERTRON JDS6600","JUNTEK DPM8605","TEK MDO4104B"]

        device_combo = Gtk.ComboBoxText()
        device_combo.set_entry_text_column(0)
        # first entry not displayed if this line is placed before append()
        # device_combo.set_active(0)
        device_combo.connect("changed", self.on_name_combo_changed)
        for device in device_list:
            device_combo.append_text(device)
        # first entry displayed if this line is placed after append()
        device_combo.set_active(0)

        grid_level2 = Gtk.Grid(column_homogeneous=False,row_homogeneous=False,column_spacing=0,row_spacing=0)
        # grid_level2.attach(button,0,0,1,1)
        grid_level2.attach(device_combo,1,0,1,1)
        self.panel1.add(grid_level2)


    def on_button_clicked(self, widget):
        dev = usb.core.find(idVendor=0x5345, idProduct=0x1234)
        dev.reset()

        dev.write(0x01, b'*IDN')
        res=dev.read(0x81,64,1000)
        id=res.tobytes().decode('utf-8')
        print(id)
        self.set_label("hello")

    def on_name_combo_changed(self, combo):
        device_list=combo.get_active_iter()
        model=combo.get_model()
        id,name=model[device_list][:2]
        print("%s,%s"%(id,name))

win = test_instrument()
win.set_size_request(750,750)
win.connect("destroy", Gtk.main_quit)
win.show_all()
Gtk.main()